Bridgetek Application Note AsciiDoc and PDF kit

Files
  BRT_AN_Template_Ver.2.0.adoc  Reusable content template
  bridgetek-pdf-theme.yml        PDF colors, typography, tables, and notes
  render_bridgetek_pdf.py        One-command PDF build and repeating page furniture
  images/bridgetek-logo.png      Logo extracted from the Word template
  images/note.png                Note icon extracted from the Word template
  BRT_AN_Template_Ver.2.0.pdf   Styled preview with editable placeholders

To reuse
1. Copy the entire folder so the .adoc file and images/ directory stay together.
2. Edit the attributes near the top of the .adoc file: title, code, reference,
   version, date, clearance number, product and contact links, and copyright year.
3. Replace bracketed instructional text, sample rows, and sample headings.
4. To add a product photo, place it in images/ and uncomment :product-image:.
5. To include the internal revision history, uncomment its attribute line.

To build a PDF
Install Asciidoctor PDF, Python, and the PyMuPDF and Pillow Python packages.
From this folder, run:

    python render_bridgetek_pdf.py

The script first runs Asciidoctor PDF with bridgetek-pdf-theme.yml, then adds
the cover border and the repeating logo, links, copyright, and page numbers.
The result is BRT_AN_Template_Ver.2.0.pdf unless --output is supplied.
The PDF preview uses high-resolution rendered pages for consistent display
across viewers; edit the .adoc source rather than the preview PDF.

The theme uses Asciidoctor PDF's bundled Noto Sans font as a portable
approximation of the Word template's Verdana-family typography. The original
Word document remains the source for the legal and contact wording.
