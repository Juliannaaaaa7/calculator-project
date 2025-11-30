# greetings.py
from datetime import datetime
import os

names_path = os.path.join("data", "names.txt")

# Якщо папки/файла нема — створюємо з прикладами
if not os.path.exists(names_path):
    os.makedirs(os.path.dirname(names_path), exist_ok=True)
    with open(names_path, "w", encoding="utf-8") as f:
        f.write("Anna\nPetro\nMaria\n")
    print(f"Created sample {names_path!r} — edit it if needed.\n")

with open(names_path, "r", encoding="utf-8") as f:
    names = [line.strip() for line in f if line.strip()]

time = datetime.now().strftime("%H:%M:%S")

for name in names:
    print(f"Hello, {name}! Current time: {time}")