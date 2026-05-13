import base64
import os

CONFIG_DIR = "configs"
OUTPUT = "themoon18.txt"

links = []

for file in os.listdir(CONFIG_DIR):
    path = os.path.join(CONFIG_DIR, file)
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line=line.strip()
            if line:
                links.append(line)

merged = "\n".join(links)
encoded = base64.b64encode(merged.encode()).decode()

with open(OUTPUT, "w") as f:
    f.write(encoded)

print("Subscription generated:", OUTPUT)
