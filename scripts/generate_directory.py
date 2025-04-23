import json
from pathlib import Path

# Load all lounge files
lounges = []
for file in Path("data/lounges").glob("*.json"):
    try:
        with open(file) as f:
            data = json.load(f)
            lounges.append(data)
    except json.JSONDecodeError as e:
        print(f"Error in file: {file.name}")
        print(f"Error details: {str(e)}")

# Generate Markdown table
markdown = """# SkyTeam Lounges Directory
| Airport | Lounge Name | Terminal | Access Rules | Key Amenities |
|---------|-------------|----------|--------------|---------------|
"""
for lounge in sorted(lounges, key=lambda x: x["airport"]):
    access_rules = ", ".join([rule["rule"] for rule in lounge["access"]])
    amenities = ", ".join(lounge["amenities"][:3]) + "..."  # Show first 3
    markdown += f"| {lounge['airport']} | [{lounge['name']}](data/lounges/{lounge['id']}.json) | {lounge['terminal']} | {access_rules} | {amenities} |\n"

# Write to file
with open("LOUNGES.md", "w") as f:
    f.write(markdown)