import pdfplumber

with pdfplumber.open("deep learning.pdf") as pdf:
    all_text = ""
    for page in pdf.pages:
        all_text += page.extract_text() + "\n"

with open("deep_learning.txt", "w", encoding="utf-8") as f:
    f.write(all_text)