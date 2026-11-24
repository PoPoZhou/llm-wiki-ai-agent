# AI Agent 是什麼？— LLM Wiki 教學簡報

- 教學簡報：https://popozhou.github.io/llm-wiki-ai-agent/slides/
- Wiki 網頁：https://popozhou.github.io/llm-wiki-ai-agent/wiki_site.html

## 結構
| 路徑 | 說明 |
|---|---|
| `SCHEMA.md` | Wiki 維護規則（ingest / query / lint） |
| `raw/` | 6 篇原始資料（Anthropic Engineering Blog），只讀 |
| `wiki/` | LLM 整理的 wiki：`sources/` 資料摘要、`concepts/` 概念頁、`index.md`、`log.md` 執行紀錄 |
| `lint_wiki.py` | 檢查①：引用是否逐字存在於原文、連結是否斷掉、孤立頁 |
| `check_slides.py` | 檢查②：簡報事實是否出自 wiki、名詞是否先解釋、版面是否溢出 |
| `slides/index.html` | 教學 HTML 簡報（← → 換頁） |

## Loop / Graph
```
討論 → 取得資料 → 整理成 wiki ⟲(每篇)
     → lint_wiki ─✗→ 回到整理 wiki
     → 查詢 wiki 產生簡報
     → check_slides ─✗→ 只重新生成有問題的頁
     → 發布
```
執行紀錄見 [wiki/log.md](wiki/log.md)。
