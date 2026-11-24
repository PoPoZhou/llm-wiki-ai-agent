"""檢查簡報：(1) 每頁 data-facts 都能在其引用的 wiki 頁找到 (2) 專有名詞先解釋後使用 (3) 版面不溢出"""
import re, glob, os, sys, html
from bs4 import BeautifulSoup
pages = {os.path.basename(f)[:-3]: open(f).read() for f in glob.glob("wiki/**/*.md", recursive=True)}
soup = BeautifulSoup(open("slides/index.html"), "html.parser")
secs = soup.find_all("section"); errors = []
for n, s in enumerate(secs, 1):
    w = s.get("data-wiki")
    if w not in pages: errors.append(f"第{n}頁 引用的 wiki 頁不存在：{w}"); continue
    for fact in filter(None, (s.get("data-facts") or "").split("|")):
        if fact not in pages[w]: errors.append(f"第{n}頁 事實不在 wiki[{w}]：{fact}")
# 專有名詞：第一次出現的那一頁，必須同時有解釋（「＝」或「：」緊接在後）
terms = {"LLM": r"LLM（大型語言模型）", "token": r"token</b> 是", "上下文": r"上下文（context）</b>＝"}
texts = [str(s) for s in secs]
for t, pat in terms.items():
    first = next((k for k, x in enumerate(texts) if t in BeautifulSoup(x, "html.parser").get_text()), None)
    defn = next((k for k, x in enumerate(texts) if re.search(pat, x)), None)
    if defn is None or (first is not None and first < defn):
        errors.append(f"名詞「{t}」在第{(first or 0)+1}頁先出現，但解釋在第{(defn or -1)+1}頁")
# 版面：用瀏覽器檢查每頁在桌機與手機寬度下是否溢出
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium") if os.path.exists("/opt/pw-browsers/chromium") and os.path.isfile("/opt/pw-browsers/chromium") else p.chromium.launch()
    for w, h in ((1280, 800), (390, 844)):
        pg = b.new_page(viewport={"width": w, "height": h}); pg.goto("file://" + os.path.abspath("slides/index.html"))
        for n in range(len(secs)):
            bad = pg.evaluate("()=>{const s=document.querySelector('section.on');return [document.documentElement.scrollWidth>innerWidth, s.scrollWidth>s.clientWidth+1]}")
            if any(bad): errors.append(f"第{n+1}頁 在 {w}px 寬度橫向溢出")
            pg.keyboard.press("ArrowRight")
        if w == 1280: pg.screenshot(path="slides/_last.png")
    b.close()
print(f"檢查 {len(secs)} 頁投影片 → {len(errors)} 個問題")
for e in errors: print("  ✗", e)
sys.exit(1 if errors else 0)
