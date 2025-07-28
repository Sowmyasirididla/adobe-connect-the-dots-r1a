import fitz
import re
import os
import json

def extract_headings(filepath):
    doc = fitz.open(filepath)
    title = ""
    headings = []
    font_sizes = set()
    blocks_info = []

    # Step 1: Gather all text blocks and font sizes
    for page_no in range(len(doc)):
        page = doc[page_no]
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if "lines" in b:
                for l in b["lines"]:
                    for s in l["spans"]:
                        text = s["text"].strip()
                        if not text:
                            continue
                        font_size = round(s["size"])
                        font_sizes.add(font_size)
                        blocks_info.append({
                            "text": text,
                            "size": font_size,
                            "flags": s["flags"],
                            "page": page_no + 1
                        })

    if not blocks_info:
        return None, []

    # Step 2: Find likely title (largest text on p1)
    page1_blocks = [b for b in blocks_info if b["page"] == 1]
    if page1_blocks:
        title_block = max(page1_blocks, key=lambda x: x["size"])
        title = title_block["text"]

    # Step 3: Sort unique font sizes, largest = H1
    font_sizes = sorted(font_sizes, reverse=True)
    if len(font_sizes) > 3:
        font_sizes = font_sizes[:3]  # use top 3 sizes as H1, H2, H3

    level_map = {}
    for idx, sz in enumerate(font_sizes):
        level_map[sz] = f"H{idx+1}"

    # Step 4: Detect headings with simple heuristics
    for b in blocks_info:
        sz = b["size"]
        if sz in level_map:
            # Additional heuristics: short line, not a number, not too long
            if 3 <= len(b["text"]) <= 80 and not re.match(r"^[\d. ]+$", b["text"]):
                headings.append({
                    "level": level_map[sz],
                    "text": b["text"],
                    "page": b["page"]
                })
    return title, headings

def main():
    input_dir = "./input"
    output_dir = "./output"
    os.makedirs(output_dir, exist_ok=True)

    # Process all PDFs in input folder
    for fname in os.listdir(input_dir):
        if fname.endswith(".pdf"):
            fpath = os.path.join(input_dir, fname)
            title, headings = extract_headings(fpath)
            output_json = {
                "title": title or "",
                "outline": headings
            }
            oname = os.path.splitext(fname)[0] + ".json"
            o_path = os.path.join(output_dir, oname)
            with open(o_path, "w", encoding="utf-8") as f:
                json.dump(output_json, f, ensure_ascii=False, indent=2)
            print(f"Processed {fname} -> {oname}")

if __name__ == "__main__":
    main()
