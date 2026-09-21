# Contributing / Как работать над игрой

## Где менять материалы / Where to edit

| Change / Изменение | File / Файл |
| --- | --- |
| Русское название или эффект события | [game/ru/cards/events.md](game/ru/cards/events.md) |
| Русский статус | [game/ru/cards/statuses.md](game/ru/cards/statuses.md) |
| Rules / Правила | [RU](game/ru/rules.md) / [EN](game/en/rules.md) |
| English translation | [English edition](game/en/README.md) |
| Copy counts / Количества экземпляров | [game/deck.md](game/deck.md) |
| Illustration brief / Задание художнику | [design](design/README.md) |
| New language / Новый язык | [Translation template](templates/translation/README.md) |

## Работа через браузер / Browser workflow

1. Откройте нужный файл и нажмите карандаш (Edit). / Open a file and choose Edit.
2. В таблице найдите карту по ID, например ST-019. Измените название или эффект, сохраняя ID и разделители `|`. / Find a card by ID; preserve its ID and table separators.
3. Проверьте Preview, чтобы таблица осталась читаемой. / Check the rendered preview.
4. Сохраните правку в отдельной ветке и откройте Pull request: это страница сравнения изменений перед их включением в main. Опишите, что и зачем изменилось. / Save in a branch and open a pull request explaining the change.
5. После просмотра включите изменения в main. При смене эффекта отметьте, какие переводы и печатные файлы требуют обновления. / After review, merge; record translations and print exports affected by gameplay edits.

## Conventions / Соглашения

- Lowercase ASCII folder/file names, words separated by hyphens; conventional root filenames such as README.md retain their standard form. / Простые имена латиницей, слова через дефис.
- One permanent ID per card record, shared by translations and artwork. Do not renumber when sorting or silently combine duplicate titles. / Один постоянный ID для всех переводов и иллюстраций карты.
- Keep art without gameplay lettering; maintain title and effect as editable text. / Картинка и текст — отдельно.
- The Russian catalogue is the current wording source. Mark translations draft/reviewed with a source commit; updating an image does not update the rules. / У переводов указываем статус и редакцию исходника.
- Keep historical source snapshots in archive; edit the current game folders. / Архивные снимки не являются рабочими копиями.
- Preserve attribution and follow the [current licence](LICENSE.md), its [English translation](legal/license.en.md) and the [transition notes](legal/README.md). Earlier permissions remain available within their scope. / Сохраняйте авторство и учитывайте новую лицензию и прежние разрешения.
- When intentionally submitting your own copyrightable contribution for inclusion under the current project licence, state that you have the necessary rights and offer the contribution under that licence. Do not assume an unmarked third-party submission transfers rights. / При передаче собственного охраняемого вклада для включения на текущих условиях явно укажите наличие нужных прав и разрешение по этой лицензии. Молчание стороннего автора не означает передачу прав.

## Optional local check / Проверка на компьютере

Run `python scripts/validate.py` from the repository. It checks card ID alignment, positive copy counts and local Markdown links, and reports translation completeness. It does not certify game balance, final deck size or print readiness. No programming is needed for ordinary browser edits.
