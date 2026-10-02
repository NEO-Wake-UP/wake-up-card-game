#!/usr/bin/env python3
"""Build the one-page Russian A5 proof directly from game/ru/rules.md.

Requires reportlab and Liberation Sans Regular/Bold TTF fonts.
Pass --font-dir when the fonts are not installed in a standard location.
The small original vector icons need no emoji font or external image files.
"""
from pathlib import Path
from html import escape
import argparse
import hashlib
import json
import os
import re

from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

ROOT = Path(__file__).resolve().parents[1]
PAGE_W, PAGE_H = 148 * mm, 210 * mm
MARGIN = 6.5 * mm
WIDTH = PAGE_W - 2 * MARGIN
INK = HexColor('#17191D')
PURPLE = HexColor('#39265B')
RED = HexColor('#CA233C')


def register_fonts(explicit=None):
    runtime = Path(os.environ.get('CODEX_PRIMARY_RUNTIME_ROOT', '/opt/codex/runtimes/codex-primary-runtime'))
    candidates = [Path(explicit)] if explicit else []
    candidates += [
        Path('/usr/share/fonts/truetype/liberation2'),
        Path('/usr/share/fonts/truetype/liberation'),
        runtime / 'dependencies/node/node_modules/pdfjs-dist/standard_fonts',
    ]
    for folder in candidates:
        if all((folder / f'LiberationSans-{style}.ttf').is_file() for style in ('Regular', 'Bold')):
            for name, style in [('Body', 'Regular'), ('BodyBold', 'Bold')]:
                pdfmetrics.registerFont(TTFont(name, str(folder / f'LiberationSans-{style}.ttf')))
            pdfmetrics.registerFontFamily('Body', normal='Body', bold='BodyBold')
            return
    raise SystemExit('Install Liberation Sans or pass --font-dir DIR.')


def markup(text):
    return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', escape(text))


def read_source():
    source = ROOT / 'game/ru/rules.md'
    lines = [line.strip() for line in source.read_text().splitlines() if line.strip()]
    assert lines[0] == '# WAKE UP'
    metadata = lines[1].replace('**', '').split(' / ')
    assert len(metadata) == 3 and lines[2] == '## КОМПЛЕКТ'
    blocks = []
    for line in lines[4:]:
        if line.startswith('## '):
            blocks.append(('head', line[3:]))
        elif line.startswith('- '):
            blocks.append(('item', line[2:]))
        else:
            blocks.append(('body', line))
    return source, metadata, lines[3], blocks


def person_icon(c, x, y):
    c.setFillColor(HexColor('#417B9D'))
    for dx, dy, radius in [(2.1, 1.2, 1.7), (7.8, 1.2, 1.7), (5, 2.1, 2.0)]:
        c.circle(x + dx, y + dy, radius, fill=1, stroke=0)
    c.roundRect(x, y - 5.3, 10, 4.4, 1.8, fill=1, stroke=0)


def hourglass_icon(c, x, y):
    c.setStrokeColor(HexColor('#62666C'))
    c.setLineWidth(0.8)
    p = c.beginPath()
    p.moveTo(x + 1, y + 4.4)
    p.lineTo(x + 9, y + 4.4)
    p.lineTo(x + 9, y + 2)
    p.lineTo(x + 5.7, y - 0.3)
    p.lineTo(x + 9, y - 2.5)
    p.lineTo(x + 9, y - 5)
    p.lineTo(x + 1, y - 5)
    p.lineTo(x + 1, y - 2.5)
    p.lineTo(x + 4.3, y - 0.3)
    p.lineTo(x + 1, y + 2)
    p.close()
    c.drawPath(p, fill=0, stroke=1)
    c.setFillColor(HexColor('#D3A24D'))
    for points in [[(2.1, 2.5), (7.9, 2.5), (5, 0.5)], [(2.1, -4.1), (7.9, -4.1), (5, -1.7)]]:
        p = c.beginPath()
        p.moveTo(x + points[0][0], y + points[0][1])
        for dx, dy in points[1:]:
            p.lineTo(x + dx, y + dy)
        p.close()
        c.drawPath(p, fill=1, stroke=0)


def cake_icon(c, x, y):
    c.setFillColor(HexColor('#D77C90'))
    c.roundRect(x, y - 5, 10, 6, 0.8, fill=1, stroke=0)
    c.setStrokeColor(white)
    c.setLineWidth(0.8)
    c.line(x + 0.7, y - 1.2, x + 9.3, y - 1.2)
    c.setStrokeColor(HexColor('#417B9D'))
    for dx in (2, 5, 8):
        c.line(x + dx, y + 1, x + dx, y + 3.5)
        c.setFillColor(HexColor('#D3A24D'))
        c.circle(x + dx, y + 4.5, 0.7, fill=1, stroke=0)


def layout(size, contents, blocks):
    body = ParagraphStyle('body', fontName='Body', fontSize=size, leading=size * 1.10,
                          textColor=INK, spaceAfter=1.0)
    styles = {
        'body': body,
        'head': ParagraphStyle('head', parent=body, fontName='BodyBold', fontSize=10.6,
                               leading=12, textColor=PURPLE, spaceBefore=2.5, spaceAfter=1.5),
        'item': ParagraphStyle('item', parent=body, leftIndent=7, firstLineIndent=0,
                               bulletIndent=0, bulletFontName='Body', bulletFontSize=8,
                               spaceAfter=0.75),
    }
    badge = 82
    left_width = WIDTH - badge - 10
    component = Paragraph(markup(contents), body)
    _, component_h = component.wrap(left_width, PAGE_H)
    # The contents block shares the badge's vertical space below the large title.
    header_h = max(badge, 34 + 6 + 12 + 2 + component_h)
    result = []
    total = header_h + 4
    for kind, text in blocks:
        style = styles[kind]
        p = Paragraph(markup(text), style, bulletText='•' if kind == 'item' else None)
        _, h = p.wrap(WIDTH, PAGE_H)
        result.append((p, h, style.spaceBefore, style.spaceAfter))
        total += h + style.spaceBefore + style.spaceAfter
    return total, header_h, component, component_h, result


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--font-dir')
    ap.add_argument('--size', type=float, default=10.0)
    ap.add_argument('--output', type=Path, default=ROOT / 'print-and-play/ru/WAKE_UP_rules_RU_A5.pdf')
    args = ap.parse_args()
    register_fonts(args.font_dir)
    source, metadata, contents, blocks = read_source()
    total, header_h, component, component_h, flow = layout(args.size, contents, blocks)
    available = PAGE_H - 2 * MARGIN
    if total > available:
        raise SystemExit(f'Layout needs {total:.2f} pt; only {available:.2f} pt available at {args.size} pt.')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(args.output), pagesize=(PAGE_W, PAGE_H), invariant=1, pageCompression=1)
    c.setTitle('WAKE UP — правила игры · A5 · 2026-10-01')
    c.setAuthor('Лучинкин Дмитрий Олегович / Luchinkin Dmitrii Olegovich')
    c.setSubject('Русские правила: точный текст game/ru/rules.md, одна страница A5')
    top = PAGE_H - MARGIN
    c.setFillColor(PURPLE)
    c.setFont('BodyBold', 31)
    c.drawString(MARGIN, top - 29, 'WAKE UP')
    c.setFont('BodyBold', 10.6)
    c.drawString(MARGIN, top - 34 - 6 - 10, 'КОМПЛЕКТ')
    component.drawOn(c, MARGIN, top - 34 - 6 - 12 - 2 - component_h)
    badge = 82
    bx, by = PAGE_W - MARGIN - badge, top - badge
    c.setLineWidth(1.2)
    c.setStrokeColor(RED)
    c.rect(bx, by, badge, badge, fill=0, stroke=1)
    for i, (text, icon) in enumerate(zip(metadata, [person_icon, hourglass_icon, cake_icon])):
        baseline = top - 23 - i * 19
        c.saveState()
        icon(c, bx + 7, baseline + 3)
        c.restoreState()
        c.setFillColor(INK)
        c.setFont('Body', 9.1)
        c.drawString(bx + 22, baseline, text)
        assert pdfmetrics.stringWidth(text, 'Body', 9.1) < badge - 28
    y = top - header_h - 4
    for p, h, before, after in flow:
        y -= before
        p.drawOn(c, MARGIN, y - h)
        y -= h + after
    c.showPage()
    c.save()
    print(json.dumps({'output':str(args.output), 'pages':1, 'page_mm':[148,210],
                      'body_pt':args.size, 'bottom_mm':round(y/mm,2),
                      'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest()}, ensure_ascii=False))


if __name__ == '__main__':
    main()
