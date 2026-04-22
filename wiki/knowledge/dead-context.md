# Dead Context

**Summary**: Instructions, tool definitions, and metadata occupying the context window that aren't contributing to the current task — how dead context accumulates, what it costs, and strategies to shed it.
**Sources**: shedding-dead-context-ryan-spletzer.md, agents-md-is-a-liability-paddo.md
**Last updated**: 2026-04-21

---

Dead context is the accumulated weight of everything you've added to make your AI coding setup "better" — plugins installed, skills enabled, CLAUDE.md lines written — that consumes context window space on every session without contributing to the task at hand. It is the output of good intentions accumulating without discipline. See [[agents-md-liability]] for the research on why this degrades performance.

## How Dead Context Accumulates

Every plugin, every skill, every line in your `CLAUDE.md` occupies space in the context window. Even "lazy-loaded" tools that aren't fully active still carry a footprint — the model needs to keep a manifest of what's available, their descriptions, their trigger conditions, their tool schemas. None of that is free (source: shedding-dead-context-ryan-spletzer.md).

The pattern: install every promising MCP server, enable a bunch of skills, add a global CLAUDE.md packed with instructions, bolt on project-level configs on top. Each felt like a small addition. Together they become a tax paid on every single session.

**Observed impact:** Opening a fresh Claude Code session, typing one simple prompt, and watching 40% of a 200K context window — roughly 2 of 5 status bar segments — vanish before any real work began (source: shedding-dead-context-ryan-spletzer.md).

## Your Context Window Is RAM

The analogy: the context window is like RAM — a finite working space where the model holds everything it needs to reason about your problem. Plugins are like running programs (source: shedding-dead-context-ryan-spletzer.md).

One VS Code window with all extensions is fine alone. Open five or six with their own extension hosts and language servers, add five or six Claude Code terminals, and a browser with 100+ tabs — and suddenly your machine is sluggish, spending more resources managing tools than doing work.

The same happens to an LLM. Every plugin and instruction competes for the same finite resource the model needs to actually think about your code.

**If 40% of your context is consumed by dead weight before you start, you're beginning every session in the "dumb zone"** — the region where model reasoning degrades (source: shedding-dead-context-ryan-spletzer.md). See [[million-token-context-window]] for zone definitions and benchmarks.

## Beyond Waste: Attention Corruption

Dead context doesn't just sit there inertly. **It dilutes the signal.** The model's attention spreads across everything in the window, so the more irrelevant context you pack in, the less weight the relevant context carries. Instructions get misapplied, tool descriptions bleed into each other, and the model confidently acts on the wrong context without indication that something went sideways (source: shedding-dead-context-ryan-spletzer.md).

The analogy extends to rowhammer attacks on non-ECC memory: repeatedly accessing one row causes electrical interference that flips bits in adjacent rows. Data doesn't disappear — it *corrupts*. Similarly, overloaded context doesn't just forget things — it produces wrong answers that look plausible, ignored instructions, agents that know the right answer but say the wrong thing because the correct instruction was diluted by everything around it.

**It's not just forgetting. It's degradation** — and like a bad DIMM, you might not realize it's happening until the output is already wrong (source: shedding-dead-context-ryan-spletzer.md).

## The Bigger-Window Trap

A bigger context window is analogous to more RAM on a machine with a memory leak — it delays symptoms without fixing the cause. And it removes the pressure to be disciplined (source: shedding-dead-context-ryan-spletzer.md).

With 200K you're forced to be thoughtful about what you load. With 1M you can be sloppy, and it *appears* to work — until it doesn't. When it fails with a million tokens of context, failures are harder to diagnose because you can't easily pinpoint which tokens caused the corruption. See [[context-scarcity-end]] for analysis of how flat-rate 1M pricing changes this dynamic.

## Three Layers of the Same Problem

The problem appears simultaneously at three levels (source: shedding-dead-context-ryan-spletzer.md):

**The editor:** VS Code loaded with dozens of extensions — linters, formatters, language packs, themes, tools tried once and forgotten. Each one adds overhead.

**The AI harness:** A global CLAUDE.md grown into a sprawling instruction manual. Plugins enabled globally that only matter for specific projects. Skills accumulated without pruning.

**The human:** Running five Claude Code instances simultaneously, five VS Code windows open, a browser with a mountain of tabs — doing to your own brain exactly what you're doing to the model: overloading your own context window with competing demands.

## The Plugin Paradox

Not all plugins are dead context. Some farm out what would otherwise be a token-intensive task to deterministic tools; some actually reduce overall token consumption by fetching *precisely* what the model needs without dumping everything into the window (source: shedding-dead-context-ryan-spletzer.md):

- A plugin that `cat`'s an entire file into context: **expensive**
- A plugin that searches for the relevant function and returns just that: **saves context**

The question isn't "how many plugins do I have?" It's "what's the ROI of each one?" Some plugins add small overhead but prevent the model from doing expensive, wasteful exploration on its own — those are keepers. The ones occupying space for a capability you use once a month? Dead context.

## Memory Management Strategies

If the context window is RAM, optimizing it is memory management (source: shedding-dead-context-ryan-spletzer.md):

### Scope your editor per project
Launch VS Code with only extensions listed in a project's `.vscode/extensions.json`. Everything else disabled for that session. Each project only loads what it actually needs.

### Audit your CLAUDE.md
Global and project-level CLAUDE.md files are prime candidates for dead context. Instructions that made sense three months ago may be irrelevant now.

Ask Claude to audit your config: *"Review my CLAUDE.md and identify anything that could be removed, consolidated, or moved to a skill that only loads when needed."*

Skills are the equivalent of swapping to disk — full instructions load only when invoked, instead of sitting in memory on every session. See [[progressive-disclosure]] for the tiered loading framework.

### Scope plugins per project
Not every project needs every MCP server. Set project-level `.claude/settings.json` files that enable only the plugins relevant to that codebase. A Jekyll blog doesn't need a database plugin. An API project doesn't need a Playwright plugin.

### Revisit regularly
This is not a one-time cleanup. Context cruft accumulates the way clutter accumulates in a house — you install a new skill, try a new MCP server, add a line to your CLAUDE.md. Each one is small. Over time they add up.

## Use AI to Fix Your AI

The best tool for shedding dead context is the very AI you're trying to optimize (source: shedding-dead-context-ryan-spletzer.md):

- Ask Claude to generate your `.vscode/extensions.json` for a project
- Ask it to review your CLAUDE.md and suggest what to cut, optimize, or push into a skill
- Ask it to set up a scoped `.claude/settings.json` with only the plugins you need
- Ask it to create skills for instructions that don't need to load every session

There's a nice recursion to it: the model, operating within its own constrained context window, helping you make that context window less constrained for the next session. It won't tell you to install fewer things — you have to bring the philosophy.

## The Compaction Dread

If you've used Claude Code in a long session, you know the feeling: watching the status bar tick down, doing mental math about whether you can fit one more big ask in before the session compacts. Every token of dead context is a token stolen from that budget. All those plugin manifests and stale instructions crowd out the space needed for the actual back-and-forth of getting work done (source: shedding-dead-context-ryan-spletzer.md).

**The irony: the dead context was supposed to help.**

## Related pages

- [[agents-md-liability]]
- [[context-rot]]
- [[context-engineering]]
- [[progressive-disclosure]]
- [[million-token-context-window]]
- [[context-scarcity-end]]
- [[agent-configuration-files]]
