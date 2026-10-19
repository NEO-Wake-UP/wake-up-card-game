# Translate WAKE UP / Перевести WAKE UP

**Current status, 2026-10-19:** the [English edition](../../game/en/README.md) has a complete draft aligned with current Russian effects and physical numbers. Independent language review remains pending. This folder is a blank template for further languages.

Events are numbered EV-001–EV-331, one physical card per row. EV-001–EV-030 are 30 Coffee copies; the other 299 ordinary events are followed by WAKE UP and the custom blank. There are 301 distinct nonblank event types. Statuses remain ST-001–ST-034.

Номера в старых обсуждениях относятся к прежней системе: используйте [таблицу соответствия](../../game/event-numbering.md). Русские эффекты — первоисточник. Содержание прежней инструкции и датированные заметки сохранены в [истории до перенумерации](https://github.com/NEO-Wake-UP/wake-up-card-game/blob/ae5afb42e89d9c16a2f776c86db843dbbcb55433/templates/translation/README.md).

Для оформления правил доступны [пустой фон](../rules/README.md) и [пустые рамки карт](../cards/README.md). Полный печатный набор ещё не подготовлен.

## Steps / Шаги

1. Copy this folder's `cards`, `rules.md` and `glossary.md` into a new `game/<language>/` folder. Use a language code: for example `hi` for Hindi, `bn` for Bengali, `ta` for Tamil. Use a regional suffix when needed, for example `pt-BR`. Add a short README with translator credit and status.
2. Open [Russian events](../../game/ru/cards/events.md) and [statuses](../../game/ru/cards/statuses.md). Fill Title and Effect by current number. Keep EV-001–EV-331 in order: the first 30 rows are identical Coffee copies, EV-330 is WAKE UP and EV-331 is blank. ST-034 is the blank status. Preserve all amounts, targets, timing, bold amounts with B and the 58 bold discard annotations. The blank cards have no predefined effect. Use the [number map](../../game/event-numbering.md) for historical references.
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
