# Translate WAKE UP / Перевести WAKE UP

**Rules artwork, 2026-10-05:** [blank rules background](../rules/README.md) is available for any language, with [Russian](../../print-and-play/ru/WAKE_UP_rules_RU.png) and [English](../../print-and-play/en/WAKE_UP_rules_EN.png) filled examples. / Для оформления перевода готов пустой фон правил и два примера заполнения. Current card texts remain in the language catalogues; the latest status approvals are recorded in [the 5 October review](../../design/reviews/2026-10-05-assets-and-freelancer-final.ru.md).

**Source approved 2026-10-04:** [latest revision](../../design/reviews/2026-10-04-event-refresh.ru.md) adds EV-315–EV-342, replaces ST-024 with Спекулянт and updates EV-034/098/143/234/278. New event EV-342 Mute prohibits all speech, including reading effects aloud. EV-335 copying does not state a mandatory expiry on status change; that case is left to players. Follow the current Russian catalogue and row notes.

**Rules update, 2026-09-30:** follow the [new Russian rules](../../game/ru/rules.md) and [decision record](../../design/reviews/2026-09-30-final-rules.ru.md). The setup player is Бывалый (Veteran in English). Use draw only for the replacement event received for playing an event; use take/gain for effect-based acquisition. Passing does not require speech. The discard restriction covers status and event cards. Bankruptcy ends when all available BABLOS are paid and the remainder of that payment is written off; do not turn it into a lasting role. Preserve the revised mode counts and EV-311 ending. The latest glossary defines these terms.

**Source update, 2026-09-29:** [latest approved decisions](../../design/reviews/2026-09-29-statuses-final-and-draw.ru.md) supersede older source notes. Recheck status timing, ST-009’s two forms, ST-017’s 200B UP payout, ST-024’s reading-only exception, ST-026’s return to the deck, and Agony’s original-hand scope with effect-based gains allowed. Do not use ordinary draw as a separate type of draw.

The template contains every current card ID with empty translation fields. The Russian text is the current source. English cards are also awaiting translation. This worksheet is not a finished printable edition.

Шаблон содержит все текущие ID и пустые поля перевода. Источник — русский каталог; английские карты ещё не переведены. Это заготовка для локализации, а не готовое печатное издание.

## Steps / Шаги

1. Copy this folder's `cards`, `rules.md` and `glossary.md` into a new `game/<language>/` folder. Use a language code: for example `hi` for Hindi, `bn` for Bengali, `ta` for Tamil. Use a regional suffix when needed, for example `pt-BR`. Add a short README with translator credit and status.
2. Open [Russian event cards](../../game/ru/cards/events.md) and [status cards](../../game/ru/cards/statuses.md). Match each row by ID and fill Title and Effect in the copied tables. Preserve amounts, conditions, timing and targets. ST-034 and EV-BLANK remain custom blank cards. ST-005 now needs a title and effect translation for «Минималист»; ST-030 has changed to «Страховой агент», and ST-028 to «Вампир» (2026-09-28). The latest revision also replaces ST-018 NPC with «Коллекционер» and gives ST-028 200B for each declined replacement draw for a played event, without a monthly cap. On 2026-09-29, ST-007 changed from «Коррупционер» to «Адвокат» (initially «Юрист»); ST-010 is now «Трудоголик» and ST-031 «Инсайдер». Check all updated source effects and translation notes before translating.
3. Fill the glossary, then translate the [rules](../../game/ru/rules.md). Explain uncertain jokes or culturally specific references in Translation notes. A changed effect is a game adaptation and needs to be marked separately from a translation.
4. Fix relative source links in copied files: from `game/<language>/cards/`, use `../../ru/cards/events.md` or `../../ru/cards/statuses.md`. From rules or glossary, use `../ru/rules.md` or `../ru/glossary.md`. Keep all IDs unchanged and refresh the worksheet if the source adds cards.
5. Have another speaker review the translation and record the source commit reviewed. Keep its status as draft until review is complete. On a computer, `python scripts/validate.py` checks IDs and file links; incomplete translations are reported as such.
6. Place translated text onto future editable card masters, sharing the artwork by ID. The supplied [blank SVGs](../cards/README.md) are basic drafting frames; existing prototype PNG lettering is not editable. Check glyph coverage, text wrapping and readability at actual card size. Support right-to-left layout when a translation requires it.
7. After layout and a print test, add the complete package to `print-and-play/<language>/` and link it from the project README. Include rules, fronts, backs, currency, blank cards, printing instructions, version and attribution from [LICENSE](../../LICENSE.md).

Можно работать прямо через браузер GitHub: открыть файл → кнопка карандаша → заполнить строку, сохраняя разделители `|` → Preview → сохранить в своей ветке. Если в самом тексте нужен символ вертикальной черты, используйте `&#124;`. Для первого перевода не требуется программировать.

Путь «вписать название и эффект → распечатать» станет полностью доступен после подготовки окончательных макетов с отдельным текстовым слоем. Сейчас уже готовы таблицы перевода и пустые рамки; полного набора иллюстрированных шаблонов пока нет.

Translations may be shared under standard [CC BY-SA 4.0](../../LICENSE.md), subject to its attribution, change-notice and ShareAlike conditions. A faithful translation is still a change to identify and may be an adaptation under CC. There is no extra price limit or mandatory box-label format. “Translation of the author edition of WAKE UP” is a suggested label for faithful translations; use “Modified edition” when changing content as well. See the [English explanation](../../legal/license.en.md) and [voluntary publishing suggestions](../../legal/publishing-guide.md).

Переводы можно распространять по стандартной CC BY-SA 4.0 с соблюдением её условий авторства, обозначения изменений и ShareAlike. Точный перевод тоже нужно обозначить как изменение; в смысле CC он может быть переработкой. Дополнительного ограничения цены и обязательного формата надписи на коробке нет. «Перевод авторской версии WAKE UP» — рекомендуемая пометка точного перевода; при изменении содержания рекомендуем «Модифицированная версия». Это добровольные примеры оформления, а не дополнительные условия лицензии.

## Worksheet files / Файлы для заполнения

- [Event cards / События](cards/events.md)
- [Status cards / Статусы](cards/statuses.md)
- [Rules / Правила](rules.md)
- [Glossary / Словарь](glossary.md)
