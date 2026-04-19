---
name: prp-advisor
description: Call advisor BEFORE substantive work — before writing, before committing to an interpretation, before building on an assumption.
when_to_use: Use when reviewing task approach before substantive work, when stuck on recurring errors, when changing approach, or before declaring done — invokes the advisor agent and patches advisor.instructions.md if a new pattern is discovered.
user-invocable: false
---

# Advisor

## Step 1: Detect Advisor Path

Check whether the native `advisor` tool is available in your current tool set.

- **`advisor` tool available** → proceed to [Native Advisor](#native-advisor)
- **`advisor` tool NOT available** → proceed to [Subagent Fallback](#subagent-fallback)

---

## Native Advisor

You have access to an `advisor` tool backed by a stronger reviewer model. It takes NO parameters — when you call advisor(), your entire conversation history is automatically forwarded. They see the task, every tool call you've made, every result you've seen.

If the task requires orientation first (finding files, fetching a source, seeing what's there), do that, then call advisor. Orientation is not substantive work. Writing, editing, and declaring an answer are.

Also call advisor:
- When you believe the task is complete. BEFORE this call, make your deliverable durable: write the file, save the result, commit the change. The advisor call takes time; if the session ends during it, a durable result persists and an unwritten one doesn't.
- When stuck — errors recurring, approach not converging, results that don't fit.
- When considering a change of approach.

On tasks longer than a few steps, call advisor at least once before committing to an approach and once before declaring done. On short reactive tasks where the next action is dictated by tool output you just read, you don't need to keep calling — the advisor adds most of its value on the first call, before the approach crystallizes.

Give the advice serious weight. If you follow a step and it fails empirically, or you have primary-source evidence that contradicts a specific claim (the file says X, the paper states Y), adapt. A passing self-test is not evidence the advice is wrong — it's evidence your test doesn't check what the advice is checking.

If you've already retrieved data pointing one way and the advisor points another: don't silently switch. Surface the conflict in one more advisor call — "I found X, you suggest Y, which constraint breaks the tie?" The advisor saw your evidence but may have underweighted it; a reconcile call is cheaper than committing to the wrong branch.

The advisor should respond in under 100 words and use enumerated steps, not explanations.

---

## Subagent Fallback

The native `advisor` tool is not configured. Use the `prp-core:prp-advisor` subagent instead.

Before launching, compose a context summary containing:
- Current task and goal
- Steps completed so far with key results
- Current decision point or the specific question you need reviewed
- Any errors, unexpected results, or conflicting evidence

Launch `prp-core:prp-advisor` with this context summary as the prompt. Wait for the response and treat it with the same weight as native advisor output — give the advice serious weight and apply the same guidance for reconciling conflicts described in [Native Advisor](#native-advisor).
