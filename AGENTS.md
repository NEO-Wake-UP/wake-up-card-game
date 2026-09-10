# Working on WAKE UP

This is a tabletop card-game repository, not an application. Keep it easy to edit through GitHub's browser UI.

- Start with README.md, design/project-state.md and design/open-questions.md, then read the current affected rules/cards. The state document is dated; current files and user instructions take precedence.
- Current Russian gameplay wording lives in game/ru/rules.md and game/ru/cards/*.md. English rules were imported from the old README; English card worksheets start untranslated. Never describe missing translations or empty print folders as complete.
- game/deck.md owns shared IDs and provisional copy counts. IDs are stable across languages and artwork. Preserve duplicate source entries until the author decides their disposition. The 331-versus-340 event-card discrepancy is unresolved.
- Keep rules, flavor, artwork briefs and philosophical notes separate. Preserve the satirical, playful intent and the final-card concept. A folder reorganization is not permission to silently rebalance cards.
- Keep original binary assets unchanged during moves. Store new text-free art separately from editable localized lettering. Existing prototype PNGs have baked-in text.
- archive/2026-09-10 holds historical snapshots. Edit current files rather than treating archive as a second source of truth. LICENSE.md and author credit remain the author's existing wording.
- For new languages, follow templates/translation/README.md; keep all card IDs and identify incomplete/reviewed status.
- Run python scripts/validate.py after structural or catalogue changes. For migration work, also compare original blobs and card text against the baseline. Rendering/proofing is required before claiming print readiness.
- Explain changes to the user in plain Russian unless they request another language. Describe open questions as questions, not newly adopted rules.
