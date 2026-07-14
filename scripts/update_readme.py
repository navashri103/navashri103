"""Updates the Recent Activity section of the profile README.

Runs daily via GitHub Actions. Fetches recent public events from the
GitHub API and rewrites the block between the ACTIVITY markers.
"""

import json
import os
import re
import urllib.request
from datetime import datetime, timezone

USERNAME = "navashri103"
README_PATH = "README.md"
START = "<!--ACTIVITY:START-->"
END = "<!--ACTIVITY:END-->"


def fetch_events():
    url = f"https://api.github.com/users/{USERNAME}/events/public?per_page=30"
    headers = {"User-Agent": USERNAME}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def summarize(events):
    lines = []
    for event in events:
        repo = event["repo"]["name"].split("/")[-1]
        etype = event["type"]
        if etype == "PushEvent":
            for c in event["payload"].get("commits", [])[:2]:
                msg = c["message"].split("\n")[0][:70]
                lines.append(f"- 🚀 Pushed `{msg}` to **{repo}**")
        elif etype == "CreateEvent" and event["payload"].get("ref_type") == "repository":
            lines.append(f"- ✨ Created a new repo: **{repo}**")
        elif etype == "PullRequestEvent":
            action = event["payload"]["action"]
            lines.append(f"- 🔀 {action.capitalize()} a pull request in **{repo}**")
        elif etype == "IssuesEvent":
            action = event["payload"]["action"]
            lines.append(f"- 🐛 {action.capitalize()} an issue in **{repo}**")
        elif etype == "WatchEvent":
            lines.append(f"- ⭐ Starred **{event['repo']['name']}**")
        if len(lines) >= 6:
            break

    if not lines:
        lines = ["- 🌱 Quiet week — probably studying or building offline"]

    stamp = datetime.now(timezone.utc).strftime("%d %b %Y, %H:%M UTC")
    lines.append(f"\n<sub>Last updated: {stamp}</sub>")
    return "\n".join(lines)


def main():
    try:
        body = summarize(fetch_events())
    except Exception as exc:  # keep README valid even if the API hiccups
        body = f"- ⚠️ Activity fetch failed ({exc}) — will retry tomorrow"

    block = f"{START}\n{body}\n{END}"

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    content = re.sub(
        f"{re.escape(START)}.*?{re.escape(END)}",
        lambda _: block,  # lambda so backslashes in text aren't treated as escapes
        content,
        flags=re.DOTALL,
    )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print("README updated.")


if __name__ == "__main__":
    main()
