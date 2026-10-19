# Working on WAKE UP

Read START_HERE.ru.md first, then current game/ru/rules.md, game/ru/cards/*.md and game/deck.md for the task. Current cards and latest author instructions override historical reviews. Speak Russian; user is Дима, assistant is Лис. Legal author name is Лучинкин Дмитрий Олегович.

## Current task and permissions

Latest author instruction (2026-10-19): apply only five accepted delayed-discard annotations and Sabotage's one-minute viewing/selection limit, then reorder all 331 physical events and merge with main. The earlier batch is merged in PR #42. The accepted old→new numbers are listed in design/reviews/2026-10-19-event-order.ru.md. Other audit suggestions are not authorised. No player-facing timing-orientation instructions, current-month reminders, retrospective tracking aids or other memory aids are added. The author explicitly authorises this numbering migration as an exception to the former permanent-ID policy. This merge permission covers only this batch; verify the actual merge before reporting.

## Current numbers and inventory

- Events have physical numbers EV-001–EV-331 in RU, EN, blank worksheets, inventory and the current illustration index. EV-001–EV-030 are the same 30 Coffee copies, one physical copy per number. EV-330 is WAKE UP; EV-331 is the custom blank. Statuses keep ST-001–ST-034; ST-034 is blank.
- Inventory: 301 distinct nonblank event types, 330 nonblank physical events plus one blank = 331 events; 34 statuses, 300 banknotes and one coin = 666 components. No additional cull is pending.
- All pre-migration EV references belong to the LEGACY namespace. Consult game/event-numbering.md and game/event-numbering.json against legacy commit ae5afb42e89d9c16a2f776c86db843dbbcb55433. Numbers may overlap between systems with different meanings. Retired legacy cards remain retired. Do not reinterpret an old review as current numbered text or renumber again without a new author instruction.

## Authoring rules

- Preserve mechanics, physical numbers, copy counts and original binaries unless explicitly authorised. The numbering migration changes representation, not the Coffee quantity or other mechanics beyond the six approved effects.
- Current style: deck/Bank acquisition получите, discard возьмите, taking from players заберите. Preserve select/exchange/transfer/return/draw verbs and previous exceptions. Use BABLOS, 100B, no +. Timing first when natural, другой выбранный игрок, explicit choice, short ordered sentences. Never add other-player restrictions or reorder actions without approval.
- Bold every monetary amount WITH its B in Russian and English effects and exact Russian quotations. All 58 current discard annotations stay bold with the same timing in both languages. Delayed discard also delays replacement draw. Mortgage and Rent have no replacement draw during play. Add no other delayed discard without approval. See START_HERE for settled interactions.
- Gameplay text lives in game/ru/cards; sync exact effect quotations and physical numbers in design/event-illustration-ideas.ru.md. All 30 Coffee rows share the same effect and scene. Scenes remain proposals; preserve canonical author art listed in START_HERE. Separate short effects, artistic meanings and developer explanations.
- English card titles/effects have a full translation draft aligned with current RU; independent English review remains pending. Use draw only for replacement draws and gain a new event for effect gains. Other-language templates remain blank, with the same physical numbers.
- Keep RU/EN rules and published print texts synchronised when authorised. The author handles the pending rules PNG word edit himself; the old A5 PDF is retired. Render and inspect before claiming print readiness.
- After catalogue changes run scripts/validate.py and compare against the baseline via the number map: no lost events, changed scenes, copy inflation or cross-language mismatch. The validator checks EV-001–EV-331, the Coffee block, ending, blank and illustration correspondence. No claim of tested balance from a few model games.
- Standard CC BY-SA 4.0 is the author's chosen licence. No former price cap or extra obligations; preserve legal originals and previously granted rights.
- Save approved changes to a working branch; merge only when requested. Verify actual merge before reporting. Keep summaries concise, retain dated decisions and immutable history. Do not carry a completed merge permission into a later batch.

## History

Pre-migration reviews and design/event-design-notes.ru.md retain legacy EV numbers. Use the number map first. Earlier AGENTS/project summaries are linked in design/reviews/2026-10-17-documentation-cleanup.ru.md. Cancelled rules and historical approvals are not new authority.
