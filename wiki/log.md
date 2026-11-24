# Log（實際執行紀錄，2026-11-24）

## [討論] 確定範圍
- 主題：AI Agent 是什麼；對象：完全沒接觸過的人
- 決定資料來源：Anthropic Engineering Blog 6 篇（同一來源、可逐字核對）
- 先列出要回答的問題：定義？怎麼運作？和 workflow 差在哪？什麼時候不要用？

## [ingest] 取得資料
- 嘗試 7 個網站，只有 anthropic.com、github 連得到（arxiv、wikipedia、lilianweng 被網路擋）→ 改用 Anthropic 6 篇
- HTML → Markdown 清理（去掉選單、程式碼）→ raw/S1–S6

## [ingest] 建立 wiki
- 6 頁 source 摘要 + 8 頁 concept（含 index），共 14 頁 wiki + index/log

## [lint] 第 1 次：5 個問題 ✗
- 原因：內文強調用的中文「」與引用格式「…」[S#] 撞在一起，檢查程式把兩段黏成一個引用
- 另外發現：原文 HTML 轉換後出現「Agents , on the other」多一個空格，直接整句引用會比對失敗 → 改引用不含該處的片段
- 修正：引用規則改成「不可包含「」的最短片段」
## [lint] 第 2 次：15 頁、37 個引用 → 0 個問題 ✓

## [query → 產生簡報] 15 頁，每頁標註 data-wiki（出處頁）與 data-facts（需核對的事實）

## [check_slides] 第 1 次：2 個問題 ✗
- 「LLM」在第 1 頁出現，解釋在第 3 頁
- 「上下文」在第 2 頁出現，解釋在第 10 頁
- 修正：第 1、2 頁改用白話，不先丟名詞
## [check_slides] 第 2 次：15 頁 → 0 個問題 ✓（事實對照、名詞順序、桌機 1280px／手機 390px 版面皆通過）
