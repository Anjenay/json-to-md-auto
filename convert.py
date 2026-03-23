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

for file in Path(".").rglob("*"):
    if file.suffix in [".txt", ".json"]:
        try:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()

            # Skip already converted files
            if content.strip().startswith("#"):
                print(f"Skipped (already MD): {file}")
                continue

            data = json.loads(content)

            md = json_to_md(data)

            with open(file, "w", encoding="utf-8") as f:
                f.write(md)

            print(f"Converted: {file}")

        except Exception as e:
            print(f"Skipped {file}: {e}")