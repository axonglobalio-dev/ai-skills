# Frontend Engineering Gate

When working on frontend code, use this rule as a mandatory quality gate before approval.

Run this after UI/UX direction is defined and before final visual polish.

Validate:
- product intent
- component architecture
- design tokens
- responsive behavior
- accessibility
- loading, empty, error, success, disabled, validation, and long-content states
- API integration
- performance
- maintainability
- build/typecheck/lint readiness
- visual engineering fidelity

Do not approve a UI because it looks good in one screenshot. Approve only if it is structurally sound, responsive, accessible, maintainable, integrated, and production-ready.

Final verdict must be:
PASS, PASS WITH FIXES, or FAIL.

If code exists, do not hand off to visual polish until the implementation passes the engineering gate.
