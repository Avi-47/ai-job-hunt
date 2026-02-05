import csv
import os
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "actions_log.csv")

def log_action(action, details: dict):
    os.makedirs(LOG_DIR, exist_ok=True)

    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        # Write header only once
        if not file_exists:
            writer.writerow(["timestamp", "action", "details"])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            action,
            str(details)
        ])
