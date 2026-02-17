
import fitz  # PyMuPDF
import os

pdf_path = "Bir_kulaklığın_anatomisi.pdf"
output_dir = "extracted_content"
image_dir = "assets/img/headset-reverse"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

if not os.path.exists(image_dir):
    os.makedirs(image_dir)

doc = fitz.open(pdf_path)

full_text = ""

for page_index, page in enumerate(doc):
    text = page.get_text()
    full_text += f"\n\n--- PAGE {page_index + 1} ---\n\n"
    full_text += text
    
    # Extract images
    image_list = page.get_images(full=True)
    for img_index, img in enumerate(image_list):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        
        image_filename = f"part{page_index + 1}-img{img_index + 1}.{image_ext}"
        image_path = os.path.join(image_dir, image_filename)
        
        with open(image_path, "wb") as f:
            f.write(image_bytes)
        print(f"Saved image: {image_path}")

with open(os.path.join(output_dir, "full_text.md"), "w", encoding="utf-8") as f:
    f.write(full_text)

print("Extraction complete.")
