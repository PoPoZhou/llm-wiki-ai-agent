# S6 Effective harnesses for long-running agents（Anthropic）
原始檔：raw/06_effective-harnesses.md

## 重點
- 長時間任務會跨越多個上下文視窗，用兩種角色解決：「an initializer agent that sets up the environment on the first run」[S6]
- 常見失敗：太早宣布完成：「see that progress had been made, and declare the job done」[S6]
- 對策是每次只做一點並留紀錄：「Every subsequent session asks the model to make incremental progress, then leave structured updates.」[S6]
相關：[[長時間任務]]、[[Agent迴圈]]
