# S1 Building effective agents（Anthropic）
原始檔：raw/01_building-effective-agents.md

## 重點
- 區分兩種「agentic system」：workflow（流程由程式寫死）與 agent（由 LLM 自己決定下一步）。
  - 「Workflows are systems where LLMs and tools are orchestrated through predefined code paths.」[S1]
  - 「are systems where LLMs dynamically direct their own processes and tool usage」[S1]
- Agent 的本質很單純：「They are typically just LLMs using tools based on environmental feedback in a loop.」[S1]
- 基本積木是「強化版 LLM」：「Building block: The augmented LLM」[S1]
- 五種常見 workflow：prompt chaining、routing、parallelization、orchestrator-workers、evaluator-optimizer。
- 建議先從最簡單的做法開始：「we recommend finding the simplest solution possible, and only increasing complexity when needed」[S1]
相關：[[什麼是AI-Agent]]、[[Workflow與Agent的差別]]、[[五種Workflow模式]]
