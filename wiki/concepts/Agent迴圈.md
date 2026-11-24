# Agent 迴圈（Agent Loop）
Agent 的核心是一個重複的迴圈：
1. 蒐集資訊（gather context）
2. 採取行動（take action，例如呼叫工具）
3. 檢查結果（verify work）
4. 重複，直到完成
- 「gather context -> take action -> verify work -> repeat」[S5]
- 「environmental feedback in a loop」[S1]：每一輪都根據「環境回饋」（工具結果、錯誤訊息）調整。
**比喻：** 像學生寫作業：查資料→寫→對答案→改錯，再繼續。
延伸：[[工具Tools]]、[[長時間任務]]
