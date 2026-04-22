# Code to Contract

**Summary**: Contract-based thinking in AI-assisted development — how specifications function as executable contracts between intent and implementation, and why treating specs as authoritative contracts (not advisory documents) is the shift that makes SDD work.
**Sources**: `docs/spec-driven-development/spec-driven-development-arxiv.md`, `docs/spec-driven-development/spec-driven-development-main.md`, `docs/spec-driven-development/spec-driven-development-variant.md`
**Last updated**: 2026-04-21

---

## The Traditional Problem: Specs as Advisory Documents

For decades, code has been the de facto source of truth in software development (source: spec-driven-development-arxiv.md):
- Requirements documents exist but drift
- Design diagrams are drawn but rot
- Tests are written after the fact
- When a developer asks "what should this function do?" the answer is "read the code"

Traditional design documents — HLD, LLD, SRS — are specifications in name but not in force. They drift from reality because **nothing enforces alignment between spec and code** (source: spec-driven-development-arxiv.md).

This is the problem that spec-driven development solves: making the specification a **contract** that both humans and machines must honor, rather than a document that advisorily suggests what code might do. See [[spec-first-ai-development]] for the paradigm, and [[spec-driven-development]] for the full framework.

---

## What Makes a Specification a Contract

A specification becomes a contract when (source: spec-driven-development-arxiv.md):

1. **It is executable** — BDD scenarios, API contract tests, or model simulations fail if code doesn't match
2. **It is enforced** — spec validation is embedded in CI/CD; drift causes immediate build failures
3. **It is authoritative** — when spec and code disagree, the spec wins; code must be fixed, not the spec ignored

The shift is conceptual: from "the spec describes what we intended to build" to "the spec defines what the software must do — period."

As Bryan Finster observed: "SDD is not a revolution… it's just BDD with branding." The branding reminds practitioners that specs should be authoritative, not advisory (source: spec-driven-development-arxiv.md).

---

## Contracts in API Development

API-first development is the most mature example of spec-as-contract in practice (source: spec-driven-development-arxiv.md):

### OpenAPI (REST)

Define REST APIs with complete endpoint specifications. The OpenAPI document is the contract:
- Generates server stubs that clients depend on
- Generates client SDKs
- Powers automated contract tests (via Specmatic, Pact)
- A build fails if the implementation deviates from the spec

**Financial services case study**: An API-first microservices team using OpenAPI + Specmatic achieved a 75% reduction in integration cycle time. Mock servers generated from specs enabled frontend and backend parallel development; any deviation caused the build to fail, preventing drift (source: spec-driven-development-arxiv.md).

### GraphQL SDL

The GraphQL schema definition is a contract between frontend and backend. Type safety enforces it at the tooling level.

### Protocol Buffers / gRPC

Service interfaces defined in `.proto` files are strict contracts — automatic generation of strongly-typed client and server code makes deviation impossible.

### Pact and Specmatic

Contract testing tools that verify live implementations match their specs. These make the contract enforcement automated and continuous (source: spec-driven-development-arxiv.md).

---

## Contracts in BDD

Behavior-Driven Development frameworks are the direct ancestor of modern SDD and implement the contract model at the feature level (source: spec-driven-development-arxiv.md).

Gherkin scenarios are executable contracts in natural language:

```gherkin
Feature: Shopping Cart
  Scenario: Adding item to empty cart
    Given the cart is empty
    When I add item "Widget" to the cart
    Then the cart should contain 1 item
    And the item should be "Widget"
```

A feature is "done" only when all scenarios pass. The scenario is not documentation of what was built — it is the contract that determines whether the feature exists at all (source: spec-driven-development-arxiv.md).

**Enterprise BDD case study**: Product managers wrote Gherkin scenarios; a feature was "done" only when all scenarios passed; reduced requirement ambiguity (source: spec-driven-development-arxiv.md).

---

## Contracts in Embedded and Safety-Critical Systems

The spec-as-source model is already standard in safety-critical domains (source: spec-driven-development-arxiv.md):

**Automotive (Simulink / ISO 26262)**:
- Engineers model control algorithms in Simulink
- Behavior is verified at the model level (the contract)
- Certified C code is auto-generated — nobody hand-edits it
- ISO 26262 certification applies to the model, not the generated code

This is the fullest expression of code-to-contract thinking: **code is not the artifact, the contract is**. Code is a derivative that must be regenerated from the contract to remain valid.

---

## Contracts as AI Inputs

When AI coding assistants receive a specification as their primary input, the spec functions as an **unambiguous, executable contract** that constrains the model's output space (source: spec-driven-development-arxiv.md). Controlled studies show error reductions of up to 50% when human-refined specs are used as AI inputs.

The contrast is stark (source: spec-driven-development-main.md):

**No contract (vibe coding):**
> "Build a rate limiter middleware for Express."
→ Model fills thousands of unstated decisions from training data

**With contract (spec-first):**
> "Implement the rate limiter defined in `.spec/features/rate-limiter.md`, which specifies a sliding window algorithm, 100 requests per minute per API key, 429 responses with Retry-After headers, and Redis-backed state for horizontal scaling."
→ Model generates code aligned with your actual requirements

The contract also enables [[agent-workflows]] patterns like parallel agent execution: with specs partitioned at the contract level, multiple agents can implement different components simultaneously without interfering with each other (source: spec-driven-development-arxiv.md).

---

## The Three Contract Levels

Contracts vary in their enforcement strength (source: spec-driven-development-arxiv.md):

| Level | Enforcement | Example |
|-------|-------------|---------|
| **Spec-first** | Human review only | Markdown spec reviewed before implementation |
| **Spec-anchored** | Automated tests in CI/CD | BDD scenarios, OpenAPI + Specmatic |
| **Spec-as-source** | Code regenerated from contract | Simulink, Tessl, OpenAPI server stubs |

Each higher level eliminates a category of drift: spec-anchored eliminates undetected drift; spec-as-source eliminates drift by construction.

---

## What SDD Actually Adds Over Traditional Design Documents

Three concrete additions that transform specs from documentation into contracts (source: spec-driven-development-arxiv.md):

1. **Executable specifications** — BDD scenarios, API contract tests, or model simulations fail if code doesn't match; the spec is enforced, not merely suggested
2. **CI/CD integration** — spec validation embedded in continuous integration catches drift immediately; breaking the contract breaks the build
3. **AI consumption** — SDD specs are structured so AI coding assistants can consume them, generating code from contracts rather than guessing from vague prompts

---

## Contract Enforcement Pitfalls

Even with executable contracts, several failure modes persist (source: spec-driven-development-arxiv.md):

- **False confidence**: a passing contract test guarantees the software matches the spec, not that the spec itself is correct — if the contract is wrong, the implementation will be wrong too
- **Over-specification**: contracts that read like pseudo-code constrain implementation unnecessarily and become brittle
- **Spec rot / [[context-rot]]**: contracts drift from reality when not updated; automated enforcement is the only reliable prevention

And from hands-on tool evaluation (source: spec-driven-development-variant.md):
- **AI non-determinism**: even with a detailed contract, agents sometimes ignore directives or over-interpret them; the contract improves consistency but does not eliminate non-determinism
- **Separation confusion**: keeping functional contracts (what the software does) cleanly separated from technical constraints (how it does it) is harder in practice than in theory

---

## Related pages

- [[spec-driven-development]]
- [[spec-first-ai-development]]
- [[spec-driven-development-practice]]
- [[spec-driven-development-critique]]
- [[context-engineering]]
- [[agent-workflows]]
- [[agentic-engineering-workflow]]
- [[agent-best-practices]]
- [[context-rot]]
