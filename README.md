# Allocator.os — Portfolio Control for the Agent Economy

**Katrina Li** · [Live system demo](https://agent-allocator-landing-3b12ae.gitlab.io/) · [LinkedIn](https://www.linkedin.com/in/katrinacolumbia/)

This repository contains the interactive research demo for the thesis developed in Katrina Li's July 2026 working paper, **_Allocating Intelligence: Risk-Weighted Harnesses and Portfolio-Level Control for the Agent Economy_**.

Allocator.os is not presented as another service that selects an LLM for a prompt. It is a proposed control plane for a digital workforce: every agent has an identity, mandate, budget, reliability target, permissions, and decision history; capital, compute, verification, and autonomy move toward the agents producing the most **verified value per dollar**.

## The thesis

Long-horizon agent work fails differently from a single model call. Errors compound across dependent steps, while the cost of running every step on the strongest model becomes untenable as background and multi-agent workloads multiply token demand.

The missing primitive is a **live price on being wrong**.

The cost of an error is not merely the price of the call that produced it. It is the value of every downstream claim, action, and decision that the error can invalidate. Allocator represents work as a causal execution graph and treats that downstream exposure as the decision's **blast radius**. Verification spend then follows consequence:

- High-blast-radius decisions receive stronger models, independent re-derivation, extra compute, or human review.
- Low-blast-radius work can use open-source or local models, cached context, and lighter checks.
- Failed verification freezes the affected downstream frontier before the error compounds.
- Outcomes update the responsible agent's future budget, permissions, and autonomy.

The objective is not minimum token price. It is **cost per verified successful outcome**, adjusted for latency, recovery cost, downstream impact, and human intervention.

## What the interactive demo shows

The site turns that thesis into a visual operating system:

1. A market-style `ROUT NVDA US EQUITY <GO>` order decomposes one long-horizon job into six agent-owned steps.
2. Each step receives an identity, mandate, model tier, risk level, latency estimate, and metered budget.
3. Expensive intelligence and independent verification concentrate on the steps capable of invalidating the full task.
4. The execution ledger demonstrates operational responses — halt, revalidate, reroute, and escalate — rather than passive trace collection.
5. The fleet and operations views expose agent load, reliability, autonomy, spend, cache economics, and cost per verified result as one portfolio.

The paper's recorded six-step demonstration closes at **$7.58 versus an $18.40 all-frontier baseline**, a 59% reduction for the same stated verification target. The deeper claim is not the savings from model-tier arbitrage: it is that a causal ledger can contain failures and re-run only the affected blast radius instead of repeating an entire expensive workflow.

## Why this is above model routing

| Per-request routing | Allocator.os |
| --- | --- |
| Optimizes one API call | Optimizes a long-horizon verified outcome |
| Prices tokens and latency | Prices downstream error impact and recovery |
| Treats calls as independent | Preserves dependencies in a causal ledger |
| Chooses a model | Allocates models, verification, budgets, permissions, and autonomy |
| Emits a trace after failure | Can halt and revalidate the affected execution frontier |
| Has no worker-level memory | Maintains performance and decision continuity per agent |

Model selection is one actuator inside this architecture. The durable product is the allocation and control layer above it.

## Repository scope

This repository is a static, browser-based research and product demonstration:

- `index.html` defines the narrative, console, fleet, and operations surfaces.
- `css/` contains the responsive terminal and system-map design.
- `js/` drives the scroll choreography, 3D scenes, task decomposition, agent minting, simulated fleet telemetry, and operations traces.
- The NVDA terminal uses a public market-data request for the displayed quote where available; operational portfolio telemetry is demonstrative.
- `server.js` is only a local development convenience. GitHub Pages and GitLab Pages serve the static files directly.

The interface demonstrates the control-plane architecture and recorded research scenario; it is not itself the complete production causal-ledger backend.

## Run locally

```bash
npm start
```

Then open `http://localhost:3000`.

## Research direction

The implementation path described by the paper is:

`task decomposition → causal dependency graph → blast-radius scoring → risk-weighted execution and verification → operational ledger → portfolio-level budgets and earned autonomy`

The long-term goal is a system of record for the digital workforce: the place where an enterprise allocates intelligence, measures verified performance, governs autonomy, and preserves institutional trust even as the underlying models change.

## Ownership

Research thesis, original modifications, written content, branding, and visual customizations by **Katrina Li**. See `COPYRIGHT.md`, `NOTICE`, and `SECURITY.md` for the repository's ownership and integrity records.
