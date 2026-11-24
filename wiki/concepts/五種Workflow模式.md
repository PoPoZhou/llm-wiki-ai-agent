# 五種 Workflow 模式（S1）
1. **Prompt chaining（串接）**：一步接一步，上一步輸出是下一步輸入。像工廠流水線。
2. **Routing（分流）**：先分類，再交給專門處理的流程。像客服總機。
3. **Parallelization（平行）**：同時做多件事再合併。
4. **Orchestrator-workers（指揮者＋工人）**：一個 LLM 拆任務、分派給其他 LLM。[[多代理系統]]就是這種。
5. **Evaluator-optimizer（評審＋改進）**：一個寫、一個評，反覆修改。
- 「Building block: The augmented LLM」[S1]——以上都建立在「LLM＋檢索＋工具＋記憶」這個積木上。
延伸：[[Workflow與Agent的差別]]
