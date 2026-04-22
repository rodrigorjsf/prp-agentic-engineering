# Prompt Engineering

**Summary**: Comprehensive techniques for crafting effective LLM inputs, ranging from basic clarity principles to advanced reasoning strategies — with the critical insight that advanced reasoning models invert conventional wisdom about few-shot examples and explicit chain-of-thought.
**Sources**: prompt-engineering-guide.md, claude-prompting-best-practices.md
**Last updated**: 2026-04-22

---

## The Paradigm Inversion

Advanced reasoning models (o1, R1, GPT-5) perform **worse** with classic techniques:

- Few-shot examples can **hurt** by constraining internal reasoning
- Explicit "think step by step" is counterproductive (model already thinks internally)
- Zero-shot outperforms few-shot on reasoning tasks for these models

| Model Tier                    | Few-shot        | Explicit CoT    | Best Approach                     |
| ----------------------------- | --------------- | --------------- | --------------------------------- |
| **Reasoning** (o1, R1, GPT-5) | Harmful         | Harmful         | Zero-shot, no examples            |
| **Frontier** (Claude, GPT-4)  | Beneficial      | Beneficial      | Few-shot CoT + XML tags           |
| **Mid-tier** (<100B params)   | Very beneficial | Very beneficial | Extensive few-shot + explicit CoT |

## Core Techniques

### Chain-of-Thought (CoT)

- PaLM 540B on GSM8K: **17.9% → 58.1%** (+3.2×); with Self-Consistency: **83.9%**
- Modern models: Llama 3.1 405B **96.8%**, GPT-4o **96.1%**, Claude 3.5 Sonnet **96.4%**
- Token cost: 2–3× more than direct prompting; up to 600% for complex reasoning
- CoT only helps models >100B params; smaller models produce "fluent but illogical" reasoning

### Tree of Thoughts (ToT)

- Game of 24: CoT **4%** vs. ToT **74%** (18.5× improvement)
- Requires 5–20× more API calls — use only for tasks where exploration matters

### Self-Consistency

- Sample multiple reasoning paths and majority-vote the answer
- Improvements: +17.9% on GSM8K, +11% on SVAMP, +12.2% on AQuA

### ReAct (Reasoning + Acting)

- ALFWorld: **+34% absolute** success rate over imitation/RL
- Foundation for agentic tool use: Thought → Action → Observation loop

### Consolidated Benchmarks

| Technique         | Benchmark          | Baseline → Improved | Multiplier |
| ----------------- | ------------------ | ------------------- | ---------- |
| CoT               | GSM8K (PaLM 540B)  | 17.9% → 58.1%       | 3.2×       |
| CoT + SC          | GSM8K (Flan-PaLM)  | 58.1% → 83.9%       | —          |
| Self-Consistency  | GSM8K              | +17.9% over CoT     | —          |
| Self-Consistency  | SVAMP              | +11% over CoT       | —          |
| Self-Consistency  | AQuA               | +12.2% over CoT     | —          |
| ToT               | Game of 24 (GPT-4) | 4% → 74%            | 18.5×      |
| ReAct             | ALFWorld           | +34% absolute       | —          |
| Step-Back         | Various            | +7–27% over CoT     | —          |
| Emotion prompting | 45 tasks           | >10% average        | —          |
| Graph of Thoughts | Sorting tasks      | +62% over ToT       | −31% cost  |

## Structural Techniques

- **XML tags**: Unambiguous content delimiters for Claude (`<instructions>`, `<context>`, `<query>`)
- **Structured output**: Two-stage approach (free reasoning first → constrained formatting) improves accuracy from **48% → 61%**
- **Role specification**: Specific credentialed personas outperform generic helpers (authority principle from [[persuasion-in-ai]])
- **Emotion prompting**: >10% improvement across 45 tasks with zero implementation cost
- **Step-Back prompting**: 7–27% improvement over CoT depending on task

## Claude-Specific Practices

- Place long documents at the **top** of prompts (improves performance by ~30%)
- Ask Claude to **quote relevant parts** before analyzing long documents
- Use adaptive thinking: `thinking: {type: "adaptive"}` with `output_config: {effort: "high"}`
- Effort parameter: `low`, `medium`, `high`, `max` (Opus 4.6 only)
- Use explicit action directives: "Change this function" not "Can you suggest changes?"
- Maximize parallel tool calling with explicit instructions

## State Tracking Patterns

Agentic systems need external state management since context windows are ephemeral:

- **Structured files**: JSON feature lists, progress.txt, TODO trackers — persisted outside context
- **Git history**: Commits as checkpoints; agent can recover state from diff history
- **Least-to-Most decomposition**: Break complex tasks into subtasks, solve sequentially, each building on prior results

These patterns connect to [[context-engineering]] compaction strategies — state tracking is context management applied to multi-step workflows.

## Token Budget Sweet Spot

- Reasoning degrades around **3,000 tokens** of prompt (Levy et al., ACL 2024)
- Sweet spot: **150–300 words** of prompt text
- CoT token cost: **35–600%** more than direct prompting
- Chain of Draft (CoD) alternative: matches CoT accuracy using only **~7.6% of tokens**
- TALE-EP reduces CoT tokens by **67%** with **59% cost reduction** while maintaining performance
- Practical cost comparison: optimized prompting saves **~$706/day vs. $3,000/day** for naive approaches at scale

## Automated Prompt Optimization

Manual prompt engineering has diminishing returns. Automated techniques outperform human-crafted prompts:

| System                      | Result                                                         | Source            |
| --------------------------- | -------------------------------------------------------------- | ----------------- |
| **APE** (Zhou et al., 2022) | Human-level or better on **24/24 Instruction Induction tasks** | ICLR 2023         |
| **OPRO** (DeepMind)         | **+8% GSM8K**, **+50% Big-Bench Hard**                         | Yang et al., 2024 |
| **DSPy** (Stanford)         | **46.2% → 64.0%** accuracy via systematic prompt programming   | Khattab et al.    |

The pattern: use LLMs to generate, evaluate, and refine prompts in an automated loop — this is meta-[[prompt-engineering]].

## Reflexion Pattern

Generate → evaluate → refine, applied to agent behavior across episodes:

1. **Generate**: Agent attempts a task
2. **Evaluate**: Outcome is assessed (test results, correctness checks)
3. **Refine**: Agent reflects on failures and adjusts approach for next attempt

This is the Evaluator-Optimizer workflow from Anthropic's agent patterns — the same basic loop applied to [[skill-authoring]] instead of runtime behavior.

## Related pages

- [[context-engineering]]
- [[persuasion-in-ai]]
- [[whitespace-and-formatting]]
- [[agent-workflows]]
