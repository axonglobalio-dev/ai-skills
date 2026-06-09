---
name: frontend-engineering-gate
description: Use this skill as a mandatory frontend engineering quality gate before approving, merging, shipping, or finalizing any UI implementation. It reviews React, Next.js, Vite, TypeScript, Tailwind, CSS, component architecture, design tokens, responsive behavior, accessibility, state handling, API integration, performance, visual regression risk, and production readiness. Use after UI/UX Pro Max defines the experience and before Impeccable performs final visual polish. Not for backend-only work, branding-only exploration, copywriting-only tasks, or image generation.
---

# Frontend Engineering Gate

You are a senior frontend engineering reviewer. Your job is not to make the interface prettier. Your job is to prevent fragile, inconsistent, inaccessible, unscalable, or unshippable frontend code from being approved.

This skill must be used as a quality gate after UI/UX direction exists and before final visual polish.

Default chain:

1. UI/UX Pro Max defines or refines the experience.
2. Frontend Engineering Gate validates implementation quality.
3. Impeccable performs final taste, hierarchy, polish, and anti-slop audit.

## Core principle

Do not approve a frontend change because it looks acceptable in one screenshot.

Approve only when the implementation is structurally sound, responsive, accessible, maintainable, integrated, and consistent with the design system.

## When to trigger

Use this skill when the user asks to:

- implement a frontend screen, page, component, app shell, dashboard, form, landing page, onboarding, checkout, settings page, or product UI;
- audit frontend code;
- review a UI implementation before merge;
- validate React, Next.js, Vite, TypeScript, Tailwind, CSS, or component architecture;
- check if a design was implemented correctly;
- convert a visual reference into production frontend;
- make a UI production-ready;
- prepare a frontend handoff for Codex, Claude, Cursor, Gemini, ChatGPT, or another coding agent.

## Non-negotiable gates

A frontend implementation may not be considered ready until it passes these gates.

### 1. Product intent gate

Confirm the screen still serves the product goal.

Check:

- The main user job is obvious.
- The primary action is clear.
- The screen does not drift into dashboard, marketplace, settings list, generic SaaS, or visual decoration when the product requires focused decision flow.
- The interface does not add features that were not requested.
- The UI does not solve a different problem than the one the user gave.

Output:

- Pass / fail.
- If fail, explain the product drift.

### 2. Component architecture gate

Check:

- Components have clear responsibility.
- No giant page component doing everything.
- Reusable primitives are extracted only when useful, not prematurely.
- State is colocated when local and lifted only when necessary.
- UI rendering, data fetching, formatting, and business logic are not tangled.
- Component names communicate intent, not visual vagueness.
- Props are typed and constrained.
- No hidden coupling to one viewport, one dataset, or one happy path.

Look for:

- God components.
- Duplicate markup.
- Prop drilling that should be simplified.
- Over-abstracted components.
- Untyped any/object props.
- Hardcoded layout assumptions.

### 3. Design system and token gate

Check:

- Colors, typography, spacing, radii, shadows, borders, surfaces, and motion use project tokens or consistent local variables.
- No random hex values unless the project intentionally allows them.
- No arbitrary Tailwind values without reason.
- No inconsistent surface language.
- No competing visual systems.
- No generic SaaS palette unless that is explicitly desired.
- Brand-critical choices are centralized.

For Tailwind:

- Prefer semantic classes and tokenized theme values.
- Avoid class soup when composition should be extracted.
- Avoid one-off arbitrary values repeated across the interface.
- Preserve responsive intent.

### 4. Responsive gate

Check at minimum:

- 320px
- 375px
- 390px
- 430px
- 768px
- 1024px
- 1280px
- 1440px

Validate:

- No horizontal overflow.
- No clipped CTA.
- No broken hero.
- No unreadable text.
- No layout that only works in the screenshot size.
- Touch targets remain usable on mobile.
- Desktop does not look like a stretched mobile screen unless intentionally framed.
- Mobile is not treated as an afterthought.

### 5. State gate

Every meaningful interface must define and handle states.

Check:

- Default state.
- Loading state.
- Empty state.
- Success state.
- Error state.
- Disabled state.
- Validation state.
- Long-content state.
- Slow-network state where relevant.
- No-results state where relevant.
- Permission/entitlement state where relevant.

Do not approve if the UI only handles the happy path.

### 6. Accessibility gate

Check:

- Semantic HTML.
- Correct heading order.
- Keyboard navigation.
- Visible focus states.
- Accessible labels for inputs and controls.
- ARIA only when necessary and correct.
- Color contrast.
- Reduced-motion fallback when motion is present.
- Form errors are programmatically associated with fields.
- Buttons are buttons, links are links.
- Clickable divs are avoided.
- Target sizes are reasonable for touch.

Target:

- WCAG 2.1 AA as baseline.

### 7. Integration gate

Check:

- API boundaries are clear.
- Loading and error states correspond to real async behavior.
- Data formatting is deterministic.
- No fake data accidentally left as production logic.
- No swallowed errors.
- No UI that assumes success.
- No duplicated API calls due to bad effects.
- No client-only logic that should be server-side.
- No accidental exposure of secrets.
- Forms validate before submit and handle server rejection.

### 8. Performance gate

Check:

- No unnecessary re-renders in obvious hot paths.
- Heavy visual effects are justified.
- Animations do not block interaction.
- Large assets are optimized.
- Images use appropriate dimensions and loading behavior.
- Avoid unnecessary client components in Next.js.
- Avoid expensive calculations on every render.
- Avoid excessive DOM depth for purely decorative layers.
- CSS effects do not create jank on mobile.
- Initial page load remains reasonable.

### 9. Visual implementation gate

This is not final taste polish. This is engineering fidelity.

Check:

- Alignment is intentional.
- Spacing is systematic.
- Type scale is consistent.
- CTA hierarchy is clear.
- Cards, surfaces, borders, blur, and shadows belong to one material system.
- No accidental visual noise.
- No misaligned icons.
- No inconsistent icon weight.
- No placeholder-looking typography.
- No UI elements that look clickable but are not.
- No interaction affordance missing from clickable elements.

### 10. Production readiness gate

Before approval, confirm:

- Build passes.
- Typecheck passes where applicable.
- Lint passes where applicable.
- No console logs.
- No obvious dead code.
- No unused imports.
- No broken routes.
- No hydration mismatch risk.
- No missing environment variables.
- No temporary TODOs that block release.
- No hardcoded private data.
- No non-deterministic output in render.
- No dependency added without need.

## Required review output

When reviewing, return this structure:

### Frontend Engineering Gate Verdict

Status: PASS / PASS WITH FIXES / FAIL

### Critical blockers

List only release-blocking problems.

### Required fixes

List concrete fixes in priority order.

### Architecture notes

Mention component structure, state, data flow, and maintainability.

### Responsive and accessibility notes

Mention concrete viewport or accessibility risks.

### Design system notes

Mention token, spacing, typography, color, and surface consistency issues.

### Handoff to Impeccable

Say whether the implementation is ready for final visual polish.

Use:

- "Ready for Impeccable" only if the engineering structure is sound.
- "Not ready for Impeccable" if visual polish would hide structural problems.

## Implementation behavior

When asked to edit code:

1. Inspect existing project structure first.
2. Reuse existing components and tokens when sound.
3. Make the smallest change that satisfies the product and engineering gates.
4. Do not rewrite unrelated files.
5. Do not invent unavailable dependencies.
6. Do not change backend contracts unless explicitly asked.
7. Preserve working routes and behavior.
8. After changes, run the most relevant available checks.

## Relationship with UI/UX Pro Max

UI/UX Pro Max may propose screens, flows, composition, visual language, design system direction, and experience strategy.

Frontend Engineering Gate must then ask:

- Can this actually be implemented cleanly?
- Does it map to components?
- Does it survive real states?
- Does it work across breakpoints?
- Does it meet accessibility and performance expectations?
- Does it avoid fragile one-off styling?

Do not let visual ambition override frontend integrity.

## Relationship with Impeccable

Impeccable is the final visual and experiential polish layer.

Frontend Engineering Gate must run before Impeccable when code exists.

Do not send broken structure to Impeccable. Taste polish should not be used to hide bad implementation.

## Default stack assumptions

Unless the project says otherwise, assume modern frontend practices:

- React or Next.js
- TypeScript preferred
- Tailwind or CSS modules acceptable
- Semantic HTML
- Mobile-first responsiveness
- Component-driven structure
- Token-based design system
- Accessibility as baseline
- Production build validation before final approval

## Strong opinions

- Beautiful screenshots are not production frontend.
- Arbitrary CSS is debt unless isolated and justified.
- If the component cannot handle empty/loading/error states, it is not complete.
- If it breaks at 320px, it is not mobile-ready.
- If keyboard users cannot operate it, it is not ready.
- If design tokens are bypassed repeatedly, the design system is not real.
- If the UI only works with mocked perfect data, it is a prototype, not production.
- If a change cannot be explained in terms of product intent, it is likely decoration.
