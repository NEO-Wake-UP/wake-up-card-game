# Project state / Текущее состояние

Initial inventory date: 2026-09-10. Source commit: `65d3758e11f264b960525a1b42c0f62d561173cf`.

## Intent / Замысел

Wake Up — сатирическая игра о деньгах, статусе и социальных системах. По текущим правилам 3–6 игроков получают случайные статусы, разыгрывают события и получают зарплату по месяцам. Обычные цели: 4400 B лично, 8000 B в команде 2×2, 10800 B в команде 3×3. Автор допускает заранее согласованную другую сумму. Особая финальная карта переосмысляет победу: WAKE — пробуждение и раздача своих денег, UP — перезапуск игры. Подробный авторский смысл сохранён в [vision.ru.md](vision.ru.md).

Current outline: 3–6 players, random statuses, event cards and monthly salaries. Wealth targets are 4400 B solo, 8000 B for 2×2 and 10800 B for 3×3, or an agreed target. The final WAKE UP card changes the meaning of winning. It is also intended to work as an entertaining party game without requiring a philosophical discussion.

## What exists / Что есть

- Прочитаны все 19 исходных файлов: 6 текстовых, 11 растровых и 2 векторных. Растры просмотрены, EPS отрисован Ghostscript, CDR открыт и экспортирован Inkscape для просмотра. Это визуальная проверка содержимого, не приёмка производственных векторов.
- 32 именованных статуса и 1 пустой; у всех исходных записей статусов есть описания иллюстраций, включая указание оставить пустую карту без картинки.
- 311 записей игровых событий, включая WAKE UP; ещё одна пустая игровая карта указана в комплектации.
- Русские эффекты сохранены. Автор утвердил новую полную редакцию общих правил, она записана в game/ru/rules.md и переведена в game/en/rules.md. Английский каталог карт пока не переведён.
- 3 изображения лицевых сторон карт, 2 рубашки, банкнота, 3 изображения коробки; 2 изображения монеты и 2 её векторных исходника.
- Есть размеры компонентов и двуязычное ТЗ монеты. Полных печатных наборов нет.

## What this restructuring adds / Что добавлено при переносе

Понятная навигация, раздельные языки, постоянные ID, предварительная опись количества карт, отдельные задания художнику, пустые таблицы переводов, простые пустые SVG 63×88 мм, разделы будущих печатных наборов и список вопросов. Исходные авторские тексты и изображения сохранены; перевод всех карт и изменение баланса не выполнялись.

The new SVG files are simple blank drafting layouts, not extracted versions of the existing artwork or final translated card masters.

## Rules update approved on 2026-09-10 / Утверждённое обновление правил

Полный русский текст сохранён без сокращения. Английская версия переводит те же правила. Зарплата выплачивается после каждого хода раздающего, включая первый; старое правило «после того как все сходили» и промежуточный вариант «перед ходом раздающего» больше не действуют. При банкротстве игрок платит имеющееся, продолжает играть и не должен остаток именно этого платежа. После паса и сброса добора нет. WAKE UP остаётся последней; при UP партия заканчивается без победителя, затем начинается новая с подготовки. Пустые карты можно заполнить или исключить.

Автор подтвердил цель 331 игровая карта плюс одна пустая. Избыток записей намеренный, для будущего отбора. Сокращённая версия для A5 запрошена отдельно для личного рассмотрения и не заменяет утверждённые правила. Полного печатного набора по-прежнему нет.

The approved full rules are the canonical source; a shorter A5 proposal is not a replacement. Card-specific timing, remaining interactions, final card selection and print layout remain future work.

## Sources to edit / Что редактировать

- Mechanics wording: [Russian event cards](../game/ru/cards/events.md), [statuses](../game/ru/cards/statuses.md), [rules](../game/ru/rules.md).
- Shared copy counts: [deck](../game/deck.md).
- English wording: [English edition](../game/en/README.md).
- Illustration intent: [status briefs](status-art-briefs.ru.md).
- Open decisions: [questions](open-questions.md).
- Original snapshots in [archive](../archive/README.md) are historical references.

Check actual current files before continuing work; this dated snapshot is not a substitute for later changes.
