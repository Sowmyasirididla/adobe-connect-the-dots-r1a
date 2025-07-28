# Connecting the Dots Challenge - Round 1A Solution

## Teammates
- Didla Sowmya Siri
- Hanshika Misra
  
## Project Overview

This repository contains my solution for Round 1A of the "Connecting the Dots" Challenge. The goal is to extract a structured outline from PDF documents, including the document title and hierarchical headings (H1, H2, H3) along with their page numbers.

The output is a JSON file per PDF, following the specified format, enabling smarter document experiences such as semantic search and insight generation.

## Approach

- Utilized **PyMuPDF (fitz)** to parse PDFs offline.
- Extracted text spans with font size and style information per page.
- Determined the document title as the largest text block on the first page.
- Applied heuristics based on font size to classify headings into H1, H2, H3 levels.
- Collected heading text and associated page numbers into a hierarchical JSON outline.
- The entire solution runs offline, uses only CPU, and meets the performance and size constraints (<200MB for any model/code).

## Folder Structure

- `/input`: Place your input PDF files here.
- `/output`: JSON output files will be generated here, named after the input PDFs (e.g., `sample.pdf` → `sample.json`).
- `outline_extractor.py`: Main Python script that performs extraction.
- `Dockerfile`: Defines the container environment for offline execution.
- `requirements.txt`: Python dependencies (`pymupdf`).
- `README.md`: This file.

## How to Build the Docker Image

Run the following command from the root directory of this repository:


Replace `yourimagename` with your preferred image name.

## How to Run the Solution

To process all PDF files placed in `/input` and generate JSON outputs in `/output`, execute:


- The container automatically processes all PDFs inside `/app/input`.
- Outputs are saved as JSON files inside `/app/output`.
- No internet connection is used during runtime to comply with challenge rules.

## Constraints and Compliance

- Runs on CPU only (amd64 architecture).
- No GPU or internet dependency.
- Execution time ≤ 10 seconds for a 50-page PDF.
- Model/code size ≤ 200MB.
- Output files adhere strictly to the required JSON format.

## Known Limitations / Assumptions

- Heading detection is heuristic-based relying on font size and style; may vary with document formatting.
- Tested on provided sample PDFs and additional test files.
- Multilingual handling not implemented in Round 1A.

## Contact / Questions

For any questions or clarifications, please contact us via the GitHub repository.

---

Thank you!

