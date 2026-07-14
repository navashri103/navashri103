<div align="center">

# `nava.dev` — Profile API `v1.0`

**Base URL:** `https://github.com/navashri103`
Status: 🟢 `200 OK` · Uptime: since 2024 · Auth: none required, I'm friendly

</div>

---

### `GET /nava/about`

```json
{
  "name": "Nava",
  "role": "backend developer (in progress)",
  "status": "college student, building real things anyway",
  "location": "Chennai, India",
  "currently_building": "a food-waste startup with a 12-person team",
  "portfolio": "https://portfolio-nava.vercel.app"
}
```

---

### `GET /nava/skills`

```json
{
  "primary": "Python",
  "backend_roadmap": ["FastAPI", "Django", "databases", "APIs", "deployment"],
  "also_speaks": ["JavaScript", "React", "Git"],
  "testing": ["Vitest", "Playwright"],
  "tools": ["Claude Code", "VS Code", "GitHub Actions"]
}
```

---

### `GET /nava/projects`

```json
[
  {
    "name": "Kanban Board",
    "stack": ["React", "Vitest", "Playwright"],
    "context": "Agentic Engineering course — built and usability-tested",
    "endpoint": "https://github.com/navashri103"
  },
  {
    "name": "Portfolio",
    "stack": ["Next.js", "Vercel"],
    "live": "https://portfolio-nava.vercel.app"
  },
  {
    "name": "Food-Waste Startup",
    "stack": ["ideas", "market research", "stubbornness"],
    "status": "stress-testing the business model"
  }
]
```

---

### `GET /nava/activity` <sub>🔄 auto-updates daily via GitHub Actions</sub>

```json
<!--ACTIVITY:START-->
{
  "last_updated": "2026-07-14 03:13 UTC",
  "recent_commits": [
    "quiet week — probably studying or building offline"
  ],
  "active_repos": [
    "navashri103/leetcode-python",
    "navashri103/portfolio-v2",
    "navashri103/prelegal-",
    "navashri103/studytimerr"
  ],
  "commits_fetched": 0
}
<!--ACTIVITY:END-->
```

---

### `POST /nava/connect`

```json
{
  "accepted_payloads": ["collab ideas", "startup talk", "backend questions", "opportunities"],
  "response_time": "fast",
  "endpoints": {
    "github": "https://github.com/navashri103",
    "portfolio": "https://portfolio-nava.vercel.app"
  }
}
```

---

### `GET /nava/errors`

```json
{
  "404": "social life not found (currently building)",
  "429": "too many ideas, rate limit exceeded",
  "418": "I'm a teapot ☕ (and a student)"
}
```

<div align="center">
<sub>This profile is a REST API because I'm becoming a backend dev. The docs <i>are</i> the personality.</sub>
</div>
