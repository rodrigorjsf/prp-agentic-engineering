# MCP Dev Summit

**Summary**: Recap of the MCP Dev Summit North America 2026 (April 2-3, New York), where 1,200+ attendees confirmed MCP's production maturity and the June 2026 spec release was announced — bringing stateless transport, hardened async tasks, and enterprise auth via XAA.
**Sources**: long-live-mcp-aqfer.md, long-live-mcp-aws.md
**Last updated**: 2026-04-21

---

## Event Overview

The MCP Dev Summit North America 2026 was held April 2–3 at the New York Marriott Marquis, drawing roughly 1,200 attendees — double the prior year's numbers (source: long-live-mcp-aws.md). It was the first summit under the new **Agentic AI Foundation (AAIF)** at the Linux Foundation, after MCP was donated there in December 2025 (source: long-live-mcp-aqfer.md).

AAIF Director Jim Zemlin drew the CNCF comparison directly from the opening stage: CNCF took about 13 months to become infrastructure currency for cloud-native. MCP did the same in about 13 weeks (source: long-live-mcp-aqfer.md).

## "MCP Is Not Dead"

A central theme was refuting the online "MCP is dead" narrative. AWS's **James Hood** delivered a keynote titled "MCP @ Amazon Scale" with a Mark Twain quote: "the reports of my death have been greatly exaggerated." He stated: "There's a flurry of social media posts or articles proclaiming the death of MCP. I can tell you at Amazon, that is not true." (source: long-live-mcp-aqfer.md).

The enterprise keynote roster confirmed production use at scale: Uber, Duolingo, Datadog, Docker, Nordstrom, Bloomberg, PwC, WorkOS, Workato (source: long-live-mcp-aqfer.md).

OpenAI's **Nick Cooper** framed MCP's role: "MCP is an API for AI" — specifically designed assuming the consumer is a model, not a human developer. On CLIs versus MCP: "you clearly want both. The most powerful systems combine them." (source: long-live-mcp-aqfer.md).

As of the summit, MCP exceeds 97 million SDK downloads per month with 170+ AAIF member organizations (source: long-live-mcp-aws.md).

## June 2026 Roadmap

MCP co-creator **David Soria Parra (DSP)** laid out three features landing in the June 2026 spec release (source: long-live-mcp-aqfer.md):

1. **Stateless transport by default** — designed for serverless runtimes like AWS Lambda and Cloudflare Workers (see [[mcp-transport]])
2. **Hardened long-running tasks** — SEP-1686, for async jobs that take minutes or hours
3. **Enterprise auth via Cross-App Access (XAA)** — moves authentication off bearer tokens to workforce IdP integration

Beyond June, DSP flagged: Triggers (webhooks for MCP), Native streaming (replacing all-or-nothing tool results), **Skills over MCP** (ship skill libraries alongside MCP servers — see [[mcp-skills-interest-group]]), Interceptors (hooks for observability, policy, and telemetry), and Composability through code (see [[mcp-programmatic-tool-calling]]) (source: long-live-mcp-aqfer.md).

## The MRTR Breakthrough: Stateless Transport

**MRTR** (Multi Round-Trip Requests, SEP-2322) is the key change enabling serverless deployments (source: long-live-mcp-aqfer.md):

> **Today**: A tool call is like a phone call — the client and server stay connected the whole time. This is structurally incompatible with serverless (AWS Lambda, Cloudflare Workers).
>
> **MRTR**: Turns the phone call into an email thread. Each message carries full prior context. When the server needs to ask a question, it closes the thread; the client returns later with a new message including the full prior exchange. Any server can resume — no held connections, no sticky routing, no shared memory.

This moves features like elicitation, sampling, and long-running tasks from "impossible on serverless" to "just a normal email thread" (source: long-live-mcp-aqfer.md).

**Cornelia Davis** at Temporal noted: "Doing async over a stateful transport protocol is really tricky. I was over the moon excited this morning when I heard we want to work on a transport protocol that is stateless." (source: long-live-mcp-aqfer.md).

## SDK Roadmap

**Max Isbey** at Anthropic announced the SDK roadmap (source: long-live-mcp-aqfer.md):
- TypeScript V2 alpha is available now
- Python V2 beta is Q2 2026
- Both stable releases ship alongside the June spec

The architectural headline: a **dispatcher pattern** that cleanly separates MCP semantics from wire format and transport, making pluggable transports practical for the first time. TypeScript V2 runs natively on Cloudflare Workers. **Go** joined TypeScript, Python, and C# in the tier-1 SDK list (source: long-live-mcp-aqfer.md).

## Authentication: CIMD and XAA

Two auth mechanisms were announced (source: long-live-mcp-aqfer.md):

**CIMD** (Client ID Metadata Documents) replaces Dynamic Client Registration (DCR) with DNS-rooted trust. A client hosts a JSON metadata document at a well-known URL — that URL *is* the client ID. No registration table, no silent expiry, no impersonation risk. Claude Code shipped CIMD support two weeks before the summit.

**Cross-App Access (XAA)** is the enterprise security story. Demoed live across Claude Code and Cursor into a Figma MCP server with zero consent screens visible to the user — XAA lets the workforce IdP handle authorization centrally, ending per-app OAuth prompt fatigue.

**Aaron Parecki** (co-author of OAuth 2.1) summarized: "Most of OAuth works fine for MCP. It's three specific gaps." Client identification (CIMD). Bootstrap discovery from one URL (Protected Resource Metadata, RFC 9728). Enterprise consent fatigue (XAA) (source: long-live-mcp-aqfer.md).

## MCP Apps

MCP Apps is the first official MCP extension, shipped January 26. Servers return tool results pointing at HTML/JS/CSS bundles; the host renders them in a sandboxed iframe; UI and host communicate bidirectionally over postMessage. Within four months, every major host adopted it: Claude, ChatGPT, VS Code with Copilot, Cursor, Goose, Postman (source: long-live-mcp-aqfer.md).

## Context Bloat: A Client Problem

DSP addressed the concern that connecting an MCP server with a thousand tools blows out the context window. His answer: "that's a client problem, not a protocol problem." Claude Code already solved it with progressive tool discovery — loading tool definitions only when the model needs them — achieving about 85% reduction in token usage on real workloads (source: long-live-mcp-aqfer.md). See [[context-engineering]] for broader context management principles.

## Key Themes

1. **Interoperability**: MCP as "the API for AI" — the backbone of cross-vendor, cross-cloud agentic architectures (source: long-live-mcp-aws.md)
2. **Gateway Pattern**: Nearly all enterprise deployments rely on agent gateways and registries to govern access, security, and scalability (source: long-live-mcp-aws.md)
3. **Open Standards Stack**: AAIF's scope remains focused on agent-to-resource integration; other functions are addressed by companion standards (source: long-live-mcp-aws.md)

The next North American AAIF event is AGNTCon + MCPCon North America in San Jose on October 22–23 (source: long-live-mcp-aqfer.md).

## Related pages

- [[mcp-specification]]
- [[mcp-transport]]
- [[mcp-skills-interest-group]]
- [[mcp-programmatic-tool-calling]]
- [[mcp-typescript-sdk]]
- [[mcp-servers]]
- [[context-engineering]]
- [[agent-best-practices]]
