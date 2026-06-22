---
name: Gap Demo Auth Guard
description: Verify authorization guards on checkout and payment flows.
applies-to:
  - "**/auth/**"
---

GAP-DEMO-SKILL-LOADED

- Every checkout or payment endpoint must enforce authentication before processing.
- Verify that unauthenticated requests to /checkout, /payment, /order receive 401.
- Check that session tokens are validated server-side, not just client-side.
- Flag any direct database writes to orders/payments without prior auth check.