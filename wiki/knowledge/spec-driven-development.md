# Spec-Driven Development

**Summary**: Academic overview of Spec-Driven Development (SDD) — the practice of treating specifications as the primary artifact of software development, with code as a generated or verified secondary artifact, especially in the AI coding era.
**Sources**: `docs/spec-driven-development/spec-driven-development-arxiv.md`
**Last updated**: 2026-04-22

---

## What Is SDD?

Spec-Driven Development (SDD) inverts the traditional workflow: instead of writing code first and documenting later (or never), teams write clear specifications of intended behavior, then generate, implement, or verify code against those specifications (source: spec-driven-development-arxiv.md).

> **Core Principle:** In spec-driven development, code is the implementation detail of the specification — not the other way around. The spec declares intent; the code realizes it. (source: spec-driven-development-arxiv.md)

The AI catalyst is key: language models are excellent at pattern completion but poor at mind reading. A vague prompt like "Add photo sharing to my app" leaves dozens of decisions to the model. A precise spec — "Users can upload JPEG or PNG photos up to 10MB, stored in S3 with user-ID-prefixed keys, resized to 1024px max on upload" — eliminates guesswork and dramatically improves output quality (source: spec-driven-development-arxiv.md).

This connects directly to [[context-engineering]], where structured specs act as rich context that improves [[agent-workflows]].

---

## The Specification Spectrum

SDD is not one approach — it exists on a spectrum of rigor (source: spec-driven-development-arxiv.md):

### Spec-First

A specification is written before coding to guide initial implementation. Once code exists, the spec may or may not be maintained. Works well for initial AI-assisted feature development and prototypes. Does **not** protect against long-term drift.

### Spec-Anchored

The specification is maintained alongside code throughout the system's lifecycle. Changes to behavior require updating both spec and code. BDD frameworks like Cucumber and API contract testing tools like Specmatic exemplify this approach. This is the **sweet spot for most production systems** (source: spec-driven-development-arxiv.md).

### Spec-as-Source

The specification is the only artifact humans edit. Code is entirely generated from the spec and should never be manually modified. Already standard in domains like API stub generation (OpenAPI), and automotive embedded systems (Simulink/ISO 26262). Tools like Tessl aim to extend this to general software (source: spec-driven-development-arxiv.md).

---

## The SDD Workflow

A four-phase workflow applies across all SDD approaches (source: spec-driven-development-arxiv.md):

1. **Specify** — What should the software do? Produces a behavior-focused, testable, unambiguous functional specification.
2. **Plan** — How should we build it? Architecture, data models, interfaces, technology choices. Gives AI agents context on system structure and conventions.
3. **Implement** — Working code in small, validated increments. Specs act as "super-prompts" that break problems into modular components aligned with agents' context windows.
4. **Validate** — Does the code meet the spec? Combines automated tests and stakeholder review. The spec remains the authority; if gaps appear, either fix code or revise spec.

This maps closely to the [[rpi-workflow]] (Research-Plan-Implement) and [[rpir-workflow]] patterns used in [[agentic-engineering-workflow]].

---

## SDD and AI Coding Agents

Empirical studies suggest human-refined specs significantly improve LLM-generated code quality, with controlled studies showing **error reductions of up to 50%** (source: spec-driven-development-arxiv.md).

Additional benefits:
- **Parallel agent execution**: teams can partition work at the spec level, allowing multiple AI agents to implement different components simultaneously without interference
- **Property-based testing (PBT)**: addresses LLM non-determinism by verifying spec invariants hold regardless of implementation variation
- **Self-spec methods**: LLMs can author their own specifications from a high-level prompt, which humans then review and refine before implementation (source: spec-driven-development-arxiv.md)

See [[agent-best-practices]] for related guidance on structuring AI coding workflows.

---

## Tools and Frameworks

### BDD Frameworks

Gherkin-based executable specs using Given/When/Then format (source: spec-driven-development-arxiv.md):
- **Cucumber** (Ruby, Java, JavaScript)
- **SpecFlow / Reqnroll** (.NET)
- **Behave** (Python)

### API Specification Tools

- **OpenAPI** — REST API contracts; generates server stubs, client SDKs, documentation
- **GraphQL SDL** — schema as contract between frontend and backend
- **AsyncAPI** — event-driven architectures
- **Protocol Buffers / gRPC** — strongly typed service interfaces
- **Pact / Specmatic** — automated contract testing against live implementations

### AI-Assisted SDD Tools (2025–2026)

| Tool | Level | Approach |
|------|-------|----------|
| **GitHub Spec Kit** | Spec-first (aspiring anchored) | CLI; `/specify` → `/plan` → `/tasks` → implement; constitutional foundation |
| **Amazon Kiro** | Spec-first | VS Code extension; 3-document workflow: requirements, design, tasks |
| **Tessl** | Spec-anchored / spec-as-source | Code marked `// GENERATED FROM SPEC - DO NOT EDIT`; 1:1 spec-to-file mapping |

(source: spec-driven-development-arxiv.md)

---

## Case Studies

### API-First Microservices — Financial Services

- **Pattern**: Spec-anchored with OpenAPI + Specmatic
- **Outcome**: 75% reduction in integration cycle time; mock servers from specs enabled frontend/backend parallel development; drift caused immediate build failures (source: spec-driven-development-arxiv.md)

### BDD for Enterprise Features — Project Management Software

- **Pattern**: Spec-anchored with Cucumber
- **Outcome**: Product managers wrote Gherkin scenarios; a feature was "done" only when all scenarios passed; reduced requirement ambiguity (source: spec-driven-development-arxiv.md)

### Model-Based Embedded Development — Automotive

- **Pattern**: Spec-as-source with Simulink (ISO 26262 certified)
- **Outcome**: Engineers model control algorithms, verify at model level, auto-generate certified C code no one hand-edits (source: spec-driven-development-arxiv.md)

---

## When to Use SDD

**SDD adds clear value when** (source: spec-driven-development-arxiv.md):
- Using AI coding assistants (specs dramatically improve output quality)
- Dealing with complex or regulated requirements
- Systems with multiple maintainers (specs serve as documentation)
- Integration-heavy systems (API specs enable parallel development)
- Legacy modernization (specs for existing behavior enable clean reimplementation)

**SDD may be overkill when**:
- Throwaway prototypes or exploratory coding
- Solo, short-lived projects
- Simple CRUD with obvious requirements

> **The Golden Rule:** Use the minimum level of specification rigor that removes ambiguity for your context. (source: spec-driven-development-arxiv.md)

---

## Common Pitfalls

1. **Over-specification** — specs that read like pseudo-code, constraining implementation unnecessarily
2. **Specification rot** — specs drift from reality when not updated as code changes; see [[context-rot]]
3. **Specification as bureaucracy** — forms to fill rather than tools for clarity
4. **Tooling complexity** — drowning in generated artifacts without demonstrable value
5. **False confidence** — a passing spec test only guarantees the software matches the spec, not that the spec itself is correct

(source: spec-driven-development-arxiv.md)

---

## Relationship to Existing Practices

- **TDD**: SDD at the unit level — extended to features, systems, architectures
- **BDD**: The most direct ancestor — Gherkin scenarios are executable specifications
- **DDD**: Aligns through ubiquitous language — specs written in terms both developers and stakeholders understand
- **Agile**: User stories with acceptance criteria are specifications; SDD treats them as authoritative rather than advisory

(source: spec-driven-development-arxiv.md)

As Bryan Finster observed: "SDD is not a revolution… it's just BDD with branding." What's new is the tooling, CI/CD maturity, and AI as a spec consumer.

---

## Related pages

- [[spec-driven-development-practice]]
- [[spec-driven-development-critique]]
- [[spec-first-ai-development]]
- [[code-to-contract]]
- [[context-engineering]]
- [[agent-workflows]]
- [[rpi-workflow]]
- [[rpir-workflow]]
- [[agentic-engineering-workflow]]
- [[agent-best-practices]]
- [[context-rot]]
