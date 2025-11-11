# COREPACT-AI-PUBLIC — Public Repo Guardrails

This repository is a public-facing showcase for CORE PACT. It must remain high-level, safe, and implementation-agnostic. When in doubt: exclude sensitive details.

Hard Restrictions (Do Not Break)
1) No proprietary protocol internals
   - No internal constitutions/working drafts.
   - No internal control logic or arbitration details.
   - No scoring, weighting, or consensus resolution algorithms.
   - No thermodynamic/compression/token-optimization implementation details.

2) No confidential or legal-sensitive content
   - No patent drafts, provisional language, claim sets, or invention disclosures.
   - No NDAs, term sheets, investor lists, emails, DMs, or private correspondence.
   - No internal logs or raw traces from private runs.

3) No credentials or infrastructure details
   - No API keys, secrets, tokens, or webhooks.
   - No server IPs, internal hostnames, database URIs, or deployment topology with exploitable detail.
   - No `.env` or secret mounts.

4) No direct copies from private repos
   - Do not mirror closed-source code.
   - Do not paste files marked private, internal-only, or patent-related.

Allowed Content (Encouraged)
- Narrative overviews and use cases
- Conceptual architecture diagrams (high-level only)
- Example pseudo-flows and prompts illustrating philosophy (no secret sauce)
- Generic helper tools/demos that do not expose internal logic
- Public-safe docs: README, FAQ, CONTRIBUTING, CODE_OF_CONDUCT, sanitized roadmap

Safety Check (for contributors)
1) Could this expose implementation-level mechanics unique to CORE PACT? If yes, don’t commit; summarize instead.
2) Does this contain content from private chats/logs/deals/patents? If yes, strip or rewrite.
3) Could this help reconstruct proprietary scoring/arbitration/orchestration? If yes, abstract further.
4) Would this be problematic if posted publicly? If yes, it does not belong here.

Intent
- Treat this repo as the polished lobby. Keep it clear, professional, and public-safe.

