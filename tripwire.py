import os
import hashlib
import json

print("--- RANSOMWARE TRIPWIRE: BASELINE CREATOR ---\n")

target_folder = "./wazne_dane"
baseline_file = "baseline.json"

def calculate_file_hash(filepath):
    """Calculates the SHA-512 hash of file (Digital Fingerprint)"""
    hasher = hashlib.sha512()

    try:
        with open(filepath, 'rb') as file:
            while chunk := file.read(8192):
                hasher.update(chunk)

        return hasher.hexdigest()
    except FileNotFoundError:
        return None
    

print(f"[*] Scanning directory: {target_folder}")

if not os.path.exists(target_folder):
    print(f"[!] Error: The folder '{target_folder}' does not exist. Create it first!")
    exit()

file_hashes = {}

for filename in os.listdir(target_folder):
    full_path = os.path.join(target_folder, filename)

    if os.path.isfile(full_path):
        print(f" -> Calculating hash for: {filename}...")
        file_hash = calculate_file_hash(full_path)

        if file_hash:
            file_hashes[full_path] = file_hash

print("\n [*] Saving baselines to file...")

with open(baseline_file, 'w') as f:
    json.dump(file_hashes, f, indent=4)

print(f"[V] SUCCESS: Baseline created for {len(file_hashes)} files.")
print(f"[V] Baseline saved as '{baseline_file}.")