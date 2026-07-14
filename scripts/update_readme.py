"""Updates the GET /nava/activity section of the profile README.

Runs daily via GitHub Actions. Fetches recent public events from the
GitHub API and rewrites the block between the ACTIVITY markers.
"""

import json
import re
import urllib.request
from datetime import datetime, timezone

USERNAME = "navashri103"
README_PATH = "README.md"
START = "<!--ACTIVITY:START-->"
END = "<!--ACTIVITY:END-->"


def fetch_events():
    url = f"https://api.github.com/users/{USERNAME}/events/public?per_page=30"
    req = urllib.request.Request(url, headers={"User-Agent": USERNAME})
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def summarize(events):
    commits = []
    repos = set()
    for event in events:
        repo = event["repo"]["name"]
        repos.add(repo)
        if event["type"] == "PushEvent":
            for c in event["payload"].get("commits", []):
                commits.append({"repo": repo, "message": c["message"].split("\n")[0]})
    return {
        "last_updated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "recent_commits": commits[:5] or ["quiet week — probably studying or building offline"],
        "active_repos": sorted(repos)[:5],
        "commits_fetched": len(commits),
    }


def main():
    try:
        activity = summarize(fetch_events())
    except Exception as exc:  # keep README valid even if the API hiccups
        activity = {"error": f"activity fetch failed: {exc}", "status": 503}

    block = f"{START}\n{json.dumps(activity, indent=2, ensure_ascii=False)}\n{END}"

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    content = re.sub(
        f"{re.escape(START)}.*?{re.escape(END)}",
        lambda _: block,  # lambda so backslashes in JSON aren't treated as escapes
        content,
        flags=re.DOTALL,
    )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print("README updated.")


if __name__ == "__main__":
    main()
