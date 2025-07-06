import json

with open("deep_learning.txt", "r", encoding="utf-8") as f:
    text = f.read()

chunk_size = 500  # اندازه هر chunk به کاراکتر
chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

print(f"parts number (chunk): {len(chunks)}")

with open("chunks.jsonl", "w", encoding="utf-8") as f:
    for chunk in chunks:
        json.dump({"text": chunk}, f, ensure_ascii=False)
        f.write("\n")