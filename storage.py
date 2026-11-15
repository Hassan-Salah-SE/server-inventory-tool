import os
import json
import csv
from pathlib import Path
from datetime import datetime


def load_servers(file_path):
    # start with an empty list instead of crashing if file does not exist yet
    if not file_path.exists():
        return []
    with open(file_path, 'r', encoding='utf-8') as file:
        servers = json.load(file)
    return servers


def save_servers(servers, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(servers, file, ensure_ascii=False, indent=4)


def get_data_file():
    # use the variable INVENTORY_DATAFILE if it is set, otherwise servers.json
    file_name = os.environ.get("INVENTORY_DATAFILE",
                               "servers.json")
    return Path(file_name)


def export_csv(servers):
    # creating reports folder if it does not already exist
    reports_folder = Path("reports")
    reports_folder.mkdir(exist_ok=True)

    now = datetime.now()
    file_name = f"inventory_{now:%Y-%m-%d_%H%M}.csv"
    report_file = reports_folder / file_name
    with open(report_file, 'w', newline="", encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "address", "environment",
                                                  "role", "status", "last_checked"])
        writer.writeheader()
        writer.writerows(servers)

    return report_file
