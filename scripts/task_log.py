"""Task logger for BUd - append entries to the structured task log."""
import json
import sys
from datetime import datetime, timezone

LOG_PATH = r"C:\Users\super\Documents\My Workspace (1)\bud\logs\task_log.json"

def log_task(task_id: str, phase: str, task: str, status: str, note: str = ""):
    try:
        with open(LOG_PATH, "r") as f:
            log = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        log = {"entries": []}

    entry = {
        "id": task_id,
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "phase": phase,
        "task": task,
        "status": status,
        "note": note
    }
    log["entries"].append(entry)

    with open(LOG_PATH, "w") as f:
        json.dump(log, f, indent=2)

    print(f"Logged [{task_id}]: {task} -> {status}")

def list_pending():
    try:
        with open(LOG_PATH, "r") as f:
            log = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No task log found.")
        return

    pending = [e for e in log["entries"] if e["status"] == "pending"]
    if not pending:
        print("No pending tasks. All clear!")
    else:
        print(f"Pending tasks ({len(pending)}):")
        for e in pending:
            print(f"  [{e['id']}] {e['task']} - {e['note']}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "list-pending":
        list_pending()
    elif len(sys.argv) >= 5:
        log_task(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5] if len(sys.argv) > 5 else "")
    else:
        print("Usage:")
        print("  python task_log.py <id> <phase> <task> <status> [note]")
        print("  python task_log.py list-pending")
