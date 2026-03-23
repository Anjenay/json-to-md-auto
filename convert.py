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

def text_to_md(content):
    lines = content.splitlines()
    md = ""
    for line in lines:
        line = line.strip()
        if not line:
            continue
        md += f"- {line}\n"
    return md

for file in Path(".").rglob("*"):
    if file.suffix.lower() in [".txt", ".json"]:
        try:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()

            # ❌ REMOVED SKIP LOGIC

            try:
                data = json.loads(content)
                md = json_to_md(data)
                print(f"JSON Converted: {file}")
            except:
                md = text_to_md(content)
                print(f"Text Converted: {file}")

            with open(file, "w", encoding="utf-8") as f:
                f.write(md)

        except Exception as e:
            print(f"Error processing {file}: {e}")