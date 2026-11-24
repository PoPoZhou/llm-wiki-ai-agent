"""lint：檢查 wiki 引用是否逐字存在於 raw、[[連結]] 是否存在、是否有孤立頁"""
import re, glob, os, sys
raw = {f"S{int(os.path.basename(f)[:2])}": open(f).read() for f in glob.glob("raw/*.md")}
pages = {os.path.basename(f)[:-3]: open(f).read() for f in glob.glob("wiki/**/*.md", recursive=True)}
names = {n.split("_")[0] if n.startswith("S") and "_" in n else n: n for n in pages}
errors, n_quotes = [], 0
for name, txt in pages.items():
    for q, s in re.findall(r"「([^「」]+)」\[(S\d)\]", txt):
        n_quotes += 1
        if q not in raw.get(s, ""):
            errors.append(f"引用找不到  {name} → [{s}] {q[:60]}")
    for link in re.findall(r"\[\[(.+?)\]\]", txt):
        if link not in pages:
            errors.append(f"斷掉的連結  {name} → [[{link}]]")
linked = set(re.findall(r"\[\[(.+?)\]\]", "".join(pages.values())))
for n in pages:
    if n not in linked and n not in ("index", "log"):
        errors.append(f"孤立頁面    {n}")
print(f"檢查 {len(pages)} 頁、{n_quotes} 個引用 → {len(errors)} 個問題")
for e in errors: print("  ✗", e)
sys.exit(1 if errors else 0)
