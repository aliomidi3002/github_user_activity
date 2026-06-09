# GitHub User Activity CLI

A simple command-line tool to fetch and display the recent public activity of any GitHub user — built with pure Python, no external libraries.

> This project is part of the [roadmap.sh Backend Projects](https://roadmap.sh/projects/github-user-activity).

---

## Features

- Fetch recent public activity of any GitHub user
- Human-readable output for common event types
- Graceful error handling for invalid usernames, network issues, and empty activity

---

## Usage

```bash
python github_activity.py <username>
```

**Example:**

```bash
python github_activity.py jadijadi
```

**Output:**

```
Fetching activity for: jadijadi

- Pushed to jadijadi/gittutorial
- Commented on an issue in jadijadi/gittutorial
- Created jadijadi/some-repo
- Starred torvalds/linux
```

---

## License

MIT
