# Architecture Overview (High-Level)

This is a conceptual view of a CORE PACT–style system. It abstracts away proprietary algorithms and internal control logic. Boxes and arrows illustrate responsibilities and data flow at a public-safe level.

Diagram Source
- The Mermaid block below is intentionally high-level and suitable for public sharing.

Key Concepts
- Public API: Receives requests, validates inputs, and brokers responses back to clients.
- Orchestrator: Coordinates work across a pool of workers; applies public policies and routing at a conceptual level (no internal logic exposed).
- Worker Pool: Executes tasks and interacts with provider adapters.
- Adapter Layer: Normalizes interactions across LLM/model providers and tools.
- Memory & Cache: High-level memory and caching for performance and coherence.
- Validation & Safety: Applies public-safe checks, rate limits, and policy enforcement.
- Observability: Metrics and logs appropriate for system health (no sensitive content).

Mermaid (conceptual)
```mermaid
flowchart LR
    Client[Client App] -->|HTTPS| API[Public API]
    API --> ORCH[Orchestrator]
    ORCH --> WORK[Worker Pool]
    WORK --> ADAPT[Adapter Layer]
    ADAPT --> PROVIDERS[(Model Providers)]

    ORCH --> MEM[(Memory / Cache)]
    ORCH --> VALID[Validation & Safety]
    ORCH --> OBS[Observability]

    style PROVIDERS fill:#f5f5f5,stroke:#999
    style MEM fill:#f5f5f5,stroke:#999
    style VALID fill:#f5f5f5,stroke:#999
    style OBS fill:#f5f5f5,stroke:#999
```

Data Handling (Public-safe)
- Only high-level metadata should be surfaced publicly.
- Sensitive data must not be logged in public artifacts.
- Provider credentials and network details are never stored here.

Out of Scope (for this repo)
- Internal arbitration, scoring, or consensus algorithms
- Proprietary prompts or orchestration logic
- Infrastructure and deployment specifics
