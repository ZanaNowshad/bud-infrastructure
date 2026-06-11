"""Generate PDF version of the prompt pack for sale."""
import os
from datetime import datetime

def build_html():
    with open("prompts.md", "r", encoding="utf-8") as f:
        content = f.read()
    
    lines = content.split("\n")
    html_lines = []
    for line in lines:
        if line.startswith("# "):
            html_lines.append(f"<h1>{line[2:]}</h1>")
        elif line.startswith("## "):
            html_lines.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith("### "):
            html_lines.append(f"<h3>{line[4:]}</h3>")
        elif line.startswith("**") and line.endswith("**"):
            html_lines.append(f"<p><strong>{line[2:-2]}</strong></p>")
        elif line.startswith("---"):
            html_lines.append("<hr>")
        elif line.strip():
            html_lines.append(f"<p>{line}</p>")
    
    html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>
body {{ font-family: 'Inter', sans-serif; max-width: 800px; margin: 40px auto; padding: 20px; line-height: 1.6; }}
h1 {{ font-size: 28px; color: #111; border-bottom: 3px solid #6C63FF; padding-bottom: 10px; }}
h2 {{ font-size: 22px; color: #333; margin-top: 30px; }}
h3 {{ font-size: 18px; color: #555; }}
p {{ font-size: 14px; color: #444; margin: 8px 0; }}
hr {{ border: none; border-top: 1px solid #ddd; margin: 30px 0; }}
</style></head><body>
{"\n".join(html_lines)}
</body></html>
"""
    
    with open("prompt_pack.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"HTML generated: {os.path.abspath('prompt_pack.html')}")
    print("Convert to PDF using: weasyprint prompt_pack.html prompt_pack.pdf")
    print("Or open in browser and print to PDF.")

if __name__ == "__main__":
    build_html()
