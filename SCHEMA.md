# LLM Wiki 規則（SCHEMA）

主題：AI Agent 是什麼？——給完全沒接觸過的人
維護者：LLM（依本檔規則維護），人類負責選資料與審核

## 資料夾
- `raw/`：原始資料，只讀不改（S1–S6）
- `wiki/sources/`：每篇資料一頁摘要
- `wiki/concepts/`：概念頁，整合多篇資料
- `wiki/index.md`：所有頁面目錄；`wiki/log.md`：每次操作紀錄

## 寫作規則
1. 每個重要論點要附原文引用，格式：「英文原句片段」[S編號]，片段必須能在 raw/ 中逐字找到。
2. 頁面之間用 [[頁面名稱]] 互連，連結目標必須存在。
3. 第一次出現的專有名詞要用一句白話解釋。
4. 新資料 ingest 時：寫 source 頁 → 更新相關 concept 頁 → 更新 index → 寫 log。

## 三種操作
- ingest：讀一篇 raw → 更新 wiki
- query：從 wiki（不是 raw）回答問題或產生簡報
- lint：檢查引用是否存在、連結是否斷掉、是否有孤立頁面
