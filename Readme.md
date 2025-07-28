# Connecting the Dots Challenge - Round 1A Solution

## Teammates

- Didla Sowmya Siri
- Hanshika Misra

## Project Overview

This repository contains our solution for Round 1A of the "Connecting the Dots" Challenge.

**Goal:** Extract a structured outline from PDF documents, including the document title and hierarchical headings (H1, H2, H3) with page numbers.

Each input PDF in `/input` is processed to generate a matching JSON in `/output`.

## Approach

- Utilized **PyMuPDF (fitz)** to parse PDFs offline.
- Extracted text spans with font sizes and style per page.
- Chose the largest text on page 1 as document title.
- Detected headings heuristically via font size for H1, H2, H3.
- Collected headings and page numbers into the output JSON as required.
- Solution runs offline, CPU only, and fits well within performance and size constraints (<200MB).

## Folder Structure

- `/input` — Place your input PDF files here.
- `/output` — JSONs will be generated here, matching each PDF filename.
- `outline_extractor.py` — Main Python extraction script.
- `Dockerfile` — Container for offline, platform-compliant runs.
- `requirements.txt` — Python dependencies.
- `README.md` — This file.

## How to Build the Docker Image

Run this from your repo root (**replace `yourimagename` if you wish**):

docker build --platform linux/amd64 -t yourimagename:round1a

## How to Run the Solution

docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none yourimagename:round1a

- The container processes all PDFs in `/app/input`.
- Outputs JSONs in `/app/output`, named as `<pdfname>.json`.
- No internet is used at runtime for full compliance.

## Constraints and Compliance

- **CPU only** (amd64/x86_64 architecture)
- No GPU or internet at runtime.
- **≤10 seconds** execution for 50-page PDF.
- Model/code size ≤200MB.
- JSON output matches challenge schema exactly.

## Known Limitations

- Heading detection is heuristic (font-size based); rare unconventional PDF layouts may be misclassified.
- Multilingual detection is not implemented in this round.

## Contact / Questions

Message via this GitHub repo for any questions.

---

**Thank you!**

---

