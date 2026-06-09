#!/usr/bin/env python3
"""
Parse index.md to add/overwrite `ogrenci_no` property in each student's note frontmatter.
"""
import os
import re

BASE_DIR = "/home/eofdred/Documents/VBA-GBT/Finaller/Öğrenci raporları"
INDEX_FILE = "/home/eofdred/Documents/VBA-GBT/Finaller/index.md"

students = []
with open(INDEX_FILE, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line.startswith("|") and "---" not in line and "Öğrenci No" not in line:
            cols = [c.strip() for c in line.split("|") if c.strip()]
            # Expected columns: index, Ögrenci No, Adı Soyadı, Görev13, Final
            if len(cols) >= 5:
                # cols[0] is row number (e.g., 1)
                row_no = cols[0]
                ogr_no = cols[1]
                raw_name = cols[2]
                name = raw_name.replace("[[", "").replace("]]", "").strip()
                students.append((name, ogr_no))

print(f"Found {len(students)} entries with student numbers.")

for name, ogr_no in students:
    filepath = os.path.join(BASE_DIR, f"{name}.md")
    if not os.path.exists(filepath):
        print(f"⚠️ Missing file for {name}, skipping.")
        continue
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    # Prepare new property line
    new_prop = f"ogrenci_no: {ogr_no}"
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            existing_fm = parts[1].strip()
            body = parts[2]
            # Convert existing frontmatter to dict
            fm_dict = {}
            for line in existing_fm.split("\n"):
                if ":" in line:
                    k, v = line.split(":", 1)
                    fm_dict[k.strip()] = v.strip()
            # Update/add ogrenci_no
            fm_dict["ogrenci_no"] = ogr_no
            # Rebuild frontmatter preserving order (put ogrenci_no after existing keys)
            new_fm_lines = [f"{k}: {v}" for k, v in fm_dict.items()]
            new_fm = "---\n" + "\n".join(new_fm_lines) + "\n---"
            new_content = new_fm + body
        else:
            # Unexpected format, just prepend
            new_content = f"---\n{new_prop}\n---\n" + content
    else:
        # No frontmatter, prepend both property and a separator
        new_content = f"---\n{new_prop}\n---\n" + content
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"✅ Updated {name}.md with ogrenci_no={ogr_no}")

print("Done.")
