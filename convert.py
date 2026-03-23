import json
from pathlib import Path

def json_to_md(data, level=1):
    md = ""
    if isinstance(data, dict):
        for k, v in data.items():
            md += f"{'#'*level} {k}\n"
            md += json_to_md(v, level+1)
    elif isinstance(data, list):
        for i in data:
            md += f"- {i}\n"
    else:
        md += f"{data}\n\n"
    return md

# Scan all txt/json files
for file in Path(".").rglob("*"):
    if file.suffix in [".txt", ".json"]:
        try:
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)

            md = json_to_md(data)

            # overwrite same file (no extension change)
            with open(file, "w", encoding="utf-8") as f:
                f.write(md)

            print(f"Converted: {file}")

        except Exception:
            continue