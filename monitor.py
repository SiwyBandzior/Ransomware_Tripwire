import os
import hashlib
import json

print(f"--- RANSOMEWARE TRIPWIRE: INTEGRITY MONITOR ---\n")

target_folder="./wazne_dane"
baseline_file = "baseline.json"

def calculate_file_hash(filepath):
    hasher = hashlib.sha512()

    try:
        with open(filepath, 'rb') as file:
            while chunk := file.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None
    
print("[*] Loading baseline from file...")

try:
    with open(baseline_file, 'r') as f:
        saved_baseline = json.load(f)
except FileNotFoundError:
    print("[!] ERROR: Baseline file not found. Run the baseline creator first!")
    exit()

print(f"[*] Scanning directory: {target_folder} for changes...\n")
print("--- SCAN RESULTS ---")

for filepath, saved_hash in saved_baseline.items():
    if not os.path.exists(filepath):
        print(f"[-] ALARM (DELETED): {filepath} is missing!")
    else:
        current_hash = calculate_file_hash(filepath)

        if current_hash == saved_hash:
            print(f"[ V ] OK: {filepath} is secure and unmodified.")
        else:
            print(f"[ ! ] ALARM (MODIFIED): {filepath} has been changed! Possible Ransomware activity!")

current_files = os.listdir(target_folder)

for filename in current_files:
    full_path = os.path.join(target_folder, filename)

    if os.path.isfile(full_path):
        if full_path not in saved_baseline:
            print(f"[ + ] WARNING (NEW FILE): {full_path} is untracked and potentially suspicious.")

print("\n--- SCAN COMPLETE ---")