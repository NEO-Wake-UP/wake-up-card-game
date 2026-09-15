# Translate WAKE UP / Перевести WAKE UP

The template contains every current card ID with empty translation fields. The Russian text is the current source. English cards are also awaiting translation. This worksheet is not a finished printable edition.

Шаблон содержит все текущие ID и пустые поля перевода. Источник — русский каталог; английские карты ещё не переведены. Это заготовка для локализации, а не готовое печатное издание.

## Steps / Шаги

1. Copy this folder's `cards`, `rules.md` and `glossary.md` into a new `game/<language>/` folder. Use a language code: for example `hi` for Hindi, `bn` for Bengali, `ta` for Tamil. Use a regional suffix when needed, for example `pt-BR`. Add a short README with translator credit and status.
2. Open [Russian event cards](../../game/ru/cards/events.md) and [status cards](../../game/ru/cards/statuses.md). Match each row by ID and fill Title and Effect in the copied tables. Preserve amounts, conditions, timing and targets. ST-005 and EV-BLANK remain custom blank cards.
3. Fill the glossary, then translate the [rules](../../game/ru/rules.md). Explain uncertain jokes or culturally specific references in Translation notes. A changed effect is a game adaptation and needs to be marked separately from a translation.
4. Fix relative source links in copied files: from `game/<language>/cards/`, use `../../ru/cards/events.md` or `../../ru/cards/statuses.md`. From rules or glossary, use `../ru/rules.md` or `../ru/glossary.md`. Keep all IDs unchanged and refresh the worksheet if the source adds cards.
5. Have another speaker review the translation and record the source commit reviewed. Keep its status as draft until review is complete. On a computer, `python scripts/validate.py` checks IDs and file links; incomplete translations are reported as such.
6. Place translated text onto future editable card masters, sharing the artwork by ID. The supplied [blank SVGs](../cards/README.md) are basic drafting frames; existing prototype PNG lettering is not editable. Check glyph coverage, text wrapping and readability at actual card size. Support right-to-left layout when a translation requires it.
7. After layout and a print test, add the complete package to `print-and-play/<language>/` and link it from the project README. Include rules, fronts, backs, currency, blank cards, printing instructions, version and attribution from [LICENSE](../../LICENSE.md).

Можно работать прямо через браузер GitHub: открыть файл → кнопка карандаша → заполнить строку, сохраняя разделители `|` → Preview → сохранить в своей ветке. Если в самом тексте нужен символ вертикальной черты, используйте `&#124;`. Для первого перевода не требуется программировать.

Путь «вписать название и эффект → распечатать» станет полностью доступен после подготовки окончательных макетов с отдельным текстовым слоем. Сейчас уже готовы таблицы перевода и пустые рамки; полного набора иллюстрированных шаблонов пока нет.

## Worksheet files / Файлы для заполнения

- [Event cards / Карты событий](cards/events.md)
- [Status cards / Статусы](cards/statuses.md)
- [Rules / Правила](rules.md)
- [Glossary / Словарь](glossary.md)
