"""Build the Bridgetek PDF from the AsciiDoc template and PDF theme.

Requires Asciidoctor PDF on PATH and the Python package PyMuPDF.
"""

from __future__ import annotations

import argparse
import io
import re
import subprocess
import tempfile
from pathlib import Path

import pymupdf as fitz
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent


def image_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    names = (["C:/Windows/Fonts/arialbd.ttf", "DejaVuSans-Bold.ttf"]
             if bold else ["C:/Windows/Fonts/arial.ttf", "DejaVuSans.ttf"])
    for name in names:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            pass
    raise FileNotFoundError("An Arial or DejaVu Sans TrueType font is required")


def paint_page_furniture(image: Image.Image, page_number: int,
                         title: str, attributes: dict[str, str],
                         logo: Path) -> None:
    draw = ImageDraw.Draw(image)
    scale = 2
    width, height = image.size
    blue = (0, 119, 200)
    red = (153, 0, 0)
    black = (27, 27, 27)
    if page_number == 1:
        inset = 27 * scale
        draw.rectangle((inset, inset, width - inset, height - inset),
                       outline=blue, width=3 * scale)
        return

    left = 61 * scale
    right = width - left
    logo_width = 89 * scale
    logo_height = round(logo_width * 133 / 345)
    with Image.open(logo) as logo_image:
        logo_image = logo_image.convert("RGBA")
        logo_image = logo_image.resize((logo_width, logo_height),
                                      Image.Resampling.LANCZOS)
        image.paste(logo_image, (left, 8 * scale), logo_image)
    draw.line((left, 46 * scale, right, 46 * scale), fill=red, width=2)

    heading = f"{title} | {attributes.get('document-category', 'Application Note')}"
    heading_size = 16
    heading_font = image_font(heading_size, bold=True)
    while draw.textlength(heading, font=heading_font) > right - left - logo_width - 15 * scale:
        heading_size -= 1
        heading_font = image_font(heading_size, bold=True)
    draw.text((right, 16 * scale), heading, font=heading_font,
              fill=black, anchor="ra")

    draw.line((left, height - 37 * scale, right, height - 37 * scale),
              fill=black, width=2)
    link_text = "Product Page  |  Document Feedback"
    footer_font = image_font(14)
    footer_top = height - 30 * scale
    draw.text((left, footer_top), link_text, font=footer_font, fill=blue)
    copyright_text = (
        f"Copyright (C) {attributes.get('copyright-year', 'YYYY')} "
        f"{attributes.get('company-name', 'Bridgetek Pte Ltd')}"
    )
    copyright_font = image_font(13)
    draw.text((width // 2 + 12 * scale, footer_top), copyright_text,
              font=copyright_font, fill=black, anchor="ma")
    draw.text((right, footer_top), str(page_number), font=footer_font,
              fill=black, anchor="ra")


def read_attributes(source: Path) -> tuple[str, dict[str, str]]:
    text = source.read_text(encoding="utf-8")
    title_match = re.search(r"(?m)^= (.+)$", text)
    if not title_match:
        raise ValueError("AsciiDoc document title is missing")
    attributes = dict(re.findall(r"(?m)^:([a-z0-9-]+):\s*(.*)$", text))
    return title_match.group(1).strip(), attributes


def build(source: Path, theme: Path, output: Path, input_pdf: Path | None) -> None:
    title, attributes = read_attributes(source)
    logo = source.parent / "images" / "bridgetek-logo.png"
    if not logo.is_file():
        raise FileNotFoundError(f"Logo asset not found: {logo}")

    with tempfile.TemporaryDirectory() as temp_dir:
        raw_pdf = input_pdf or Path(temp_dir) / "raw.pdf"
        if input_pdf is None:
            subprocess.run(
                ["asciidoctor-pdf", "-a", f"pdf-theme={theme}",
                 "-o", str(raw_pdf), str(source)],
                cwd=source.parent,
                check=True,
            )
        source_document = fitz.open(str(raw_pdf))
        # A consistent high-resolution preview across PDF viewers. The
        # editable/searchable source remains the accompanying .adoc file.
        document = fitz.open()
        for index, source_page in enumerate(source_document, 1):
            page = document.new_page(width=source_page.rect.width,
                                     height=source_page.rect.height)
            pixmap = source_page.get_pixmap(matrix=fitz.Matrix(2, 2),
                                            alpha=False)
            bitmap = Image.open(io.BytesIO(pixmap.tobytes("png"))).convert("RGB")
            paint_page_furniture(bitmap, index, title, attributes, logo)
            bitmap_stream = io.BytesIO()
            bitmap.save(bitmap_stream, format="PNG")
            page.insert_image(page.rect, stream=bitmap_stream.getvalue(),
                              keep_proportion=False)
            if index > 1:
                left = 61
                link_y = source_page.rect.height - 23
                page.insert_link({"kind": fitz.LINK_URI,
                                  "from": fitz.Rect(left, link_y - 8, left + 58, link_y + 3),
                                  "uri": attributes.get("product-page-url", "https://brtchip.com/")})
                email = attributes.get("feedback-email", "docufeedback@brtchip.com")
                page.insert_link({"kind": fitz.LINK_URI,
                                  "from": fitz.Rect(left + 66, link_y - 8,
                                                    left + 146, link_y + 3),
                                  "uri": f"mailto:{email}"})
            for link in source_page.get_links():
                if link["kind"] == fitz.LINK_URI:
                    page.insert_link({"kind": fitz.LINK_URI,
                                      "from": link["from"], "uri": link["uri"]})
                elif link["kind"] == fitz.LINK_GOTO:
                    page.insert_link({"kind": fitz.LINK_GOTO,
                                      "from": link["from"],
                                      "page": link["page"],
                                      "to": link["to"]})
        output.parent.mkdir(parents=True, exist_ok=True)
        document.save(str(output), garbage=4, deflate=True)
        document.close()
        source_document.close()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", nargs="?", type=Path,
                        default=ROOT / "BRT_AN_Template_Ver.2.0.adoc")
    parser.add_argument("--theme", type=Path,
                        default=ROOT / "bridgetek-pdf-theme.yml")
    parser.add_argument("--output", type=Path,
                        default=ROOT / "BRT_AN_Template_Ver.2.0.pdf")
    parser.add_argument("--input-pdf", type=Path,
                        help="Already-rendered PDF; skips Asciidoctor PDF")
    args = parser.parse_args()
    build(args.source.resolve(), args.theme.resolve(), args.output.resolve(),
          args.input_pdf.resolve() if args.input_pdf else None)


if __name__ == "__main__":
    main()
