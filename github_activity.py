import sys
import urllib.request
import json


def fetch_events(username):
    """Fetch GitHub events for a given username."""
    url = f"https://api.github.com/users/{username}/events"
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            return json.loads(data)
    except urllib.error.HTTPError as e:
        print(f"Error: {e.code} - User not found or API error")
        return None


def format_event(event):
    """Convert a GitHub event to human-readable format."""
    event_type = event.get("type", "Unknown")
    repo_name = event.get("repo", {}).get("name", "Unknown")
    
    # Map event types to readable descriptions
    type_map = {
        "PushEvent": "Pushed to",
        "PullRequestEvent": "Made a pull request in",
        "IssueCommentEvent": "Commented on an issue in",
        "CreateEvent": "Created",
        "DeleteEvent": "Deleted",
        "ForkEvent": "Forked",
        "WatchEvent": "Starred",
    }
    
    action = type_map.get(event_type, event_type)
    return f"- {action} {repo_name}"


def print_events(events):
    """Print formatted GitHub events."""
    if not events:
        print("No events found.")
        return
    
    for event in events:
        print(format_event(event))


def main():
    if len(sys.argv) != 2:
        print("Usage: github-activity <username>")
        sys.exit(1)

    username = sys.argv[1]
    print(f"Fetching activity for: {username}\n")
    
    events = fetch_events(username)
    if events:
        print_events(events)


if __name__ == "__main__":
    main()