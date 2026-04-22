# MCP Skills vs MCP

**Summary**: Skills and MCP are complementary layers — Skills encode *how* to do things (static institutional knowledge as markdown instructions), while MCP encodes the *ability* to do things (live authenticated service access) — and most enterprise agents need both.
**Sources**: skills-vs-mcp-speakeasy.md
**Last updated**: 2026-04-21

---

## The Core Distinction

Skills and MCP are not competing technologies. They solve different problems at different layers of an agentic stack (source: skills-vs-mcp-speakeasy.md):

- **Skills = Institutional knowledge, encoded** — the *how*
- **MCP = Authenticated capability access** — the *ability*

Without skills, an agent with MCP access is like a brilliant intern with system access but no onboarding — they can do things, but they don't know your organization's way of doing them. Without MCP, an agent with skills is like a highly knowledgeable consultant who can't access any of your systems (source: skills-vs-mcp-speakeasy.md).

## What Are Skills?

Skills are static, reusable instructions that tell an agent how to perform specific tasks. They are sophisticated system prompt components encoding (source: skills-vs-mcp-speakeasy.md):

- Step-by-step workflows
- Best practices and patterns
- Error handling procedures
- Domain knowledge
- Team conventions

**Skills are fundamentally knowledge artifacts.** They don't execute code or make API calls — they tell the agent how to use the tools it already has. Think of skills as your team's institutional knowledge, distilled into machine-readable form (source: skills-vs-mcp-speakeasy.md).

See [[claude-code-skills]] for the Claude Code implementation of this concept.

A skill example:

```markdown
# Deploy Service to Staging
## Prerequisites
- kubectl access configured for staging cluster
## Steps
1. Verify: `kubectl get deployment {service-name} -n staging`
2. Update: `kubectl set image deployment/{service-name} ...`
3. Watch: `kubectl rollout status deployment/{service-name} -n staging`
4. Verify health: `curl https://staging.internal/{service-name}/health`
```

## What Is MCP?

MCP (Model Context Protocol) gives agents *capability* — the ability to interact with external systems, APIs, and data sources. Through MCP, agents can (source: skills-vs-mcp-speakeasy.md):

- **Read and write data**: Query databases, read files, update records
- **Call APIs**: Make authenticated requests to external services
- **Execute actions**: Run commands, trigger workflows, deploy changes

**MCP is fundamentally about capability access.** It provides the authenticated, governed connections that let agents move from thinking to doing (source: skills-vs-mcp-speakeasy.md). See [[mcp-specification]] for the full protocol definition.

## The Two-Layer Architecture

Skills and MCP work best together in a two-layer architecture (source: skills-vs-mcp-speakeasy.md):

```
┌─────────────────────────────────────────────────────────────────┐
│                          AI AGENT                               │
│                                                                 │
│  ┌─────────────────────┐    ┌────────────────────────────────┐  │
│  │       SKILLS        │    │             MCP                │  │
│  │  (How to do things) │    │   (Ability to do things)       │  │
│  │                     │    │                                │  │
│  │ • Workflows         │    │ • Database connections         │  │
│  │ • Best practices    │    │ • API access                  │  │
│  │ • Domain knowledge  │    │ • File system access          │  │
│  │ • Team conventions  │    │ • External service calls      │  │
│  │ • Error handling    │    │ • Authenticated operations    │  │
│  └─────────────────────┘    └────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

**Skills tell the agent what steps to follow. MCP gives the agent the tools to execute those steps.** (source: skills-vs-mcp-speakeasy.md)

## Real-World Example: Customer Support Agent

A refund request agent demonstrates the two layers clearly (source: skills-vs-mcp-speakeasy.md):

**The MCP Layer provides:**
- Access to the orders database
- Connection to the payment processing API
- Ability to update customer records
- Integration with the ticketing system

**The Skills Layer provides:**
- "Refund Request Handling" skill: check order age, verify payment, calculate amount, apply retention offer for high-value customers, process refund, send confirmation, update ticket

The agent uses the skill to know *how* to handle refunds, and uses MCP to actually *execute* each step.

## Decision Framework

| Question | If Yes, Use... |
|----------|----------------|
| Does the agent need institutional knowledge? | Skills |
| Does the agent need access to live data? | MCP |
| Are you encoding team workflows? | Skills |
| Are you connecting to external APIs? | MCP |
| Do you need auditable access trails? | MCP |
| Are you encoding domain expertise? | Skills |
| Do you need authentication/authorization? | MCP |
| Are you building reusable procedures? | Skills |

**For most enterprise agents: use both.** (source: skills-vs-mcp-speakeasy.md)

## Implementing the Two-Layer Architecture

**Step 1: Define your MCP servers** — what systems does your agent need access to?

```typescript
const server = new McpServer({ name: "company-tools", version: "1.0.0" });
server.tool("get_order", { orderId: z.string() }, async ({ orderId }) => {
  const order = await db.orders.findById(orderId);
  return { content: [{ type: "text", text: JSON.stringify(order) }] };
});
```

**Step 2: Write skills for your domain** — what does your agent need to know? (markdown files)

**Step 3: Wire them together** — serve skills from your MCP server via the Prompts primitive:

```typescript
server.prompt("refund_handling", () => ({
  messages: [{ role: "user", content: { type: "text", text: fs.readFileSync("./skills/refund-handling.md", "utf-8") } }]
}));
```

(source: skills-vs-mcp-speakeasy.md)

## Common Misconceptions

- **"Skills are just system prompts"** — Skills are more structured and reusable; they can be versioned, shared, and loaded conditionally.
- **"MCP replaces the need for skills"** — MCP gives capabilities; skills provide judgment about when and how to use those capabilities.
- **"I should choose one or the other"** — They solve different problems; you almost always want both. (source: skills-vs-mcp-speakeasy.md)

See [[mcp-skills-interest-group]] for the working group standardizing skills delivery over MCP, and [[agent-best-practices]] for broader agent design guidance.

## Related pages

- [[mcp-specification]]
- [[mcp-skills-interest-group]]
- [[claude-code-skills]]
- [[mcp-typescript-sdk]]
- [[agent-best-practices]]
- [[agent-workflows]]
- [[context-engineering]]
