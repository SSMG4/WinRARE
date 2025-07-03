import os
import random
import string
import time
from pathlib import Path
from typing import List

# Configuration
MAX_FILES = 100000  # Maximum number of files allowed
OUTPUT_DIR = Path.home() / "Downloads" / "RarRegKeys"
FILE_PREFIX = "rarreg"
KEY_LENGTH = 512  # Approximate size of a real rarreg.key file (~512 bytes)
LICENSEES = ["WinRAR GmbH", "Test User", "Demo License", "Single PC User"]
LICENSE_TYPES = ["Single PC usage license", "Unlimited Company License", "Evaluation License"]

def generate_potential_key_content() -> str:
    """Generate a WinRAR license key with a chance of matching the validation format."""
    licensee = random.choice(LICENSEES)
    license_type = random.choice(LICENSE_TYPES)
    uid = ''.join(random.choices(string.hexdigits.lower(), k=16))  # 16-char hex UID
    # Signature starts with '641221225' followed by 120 hex digits
    signature = "641221225" + ''.join(random.choices(string.hexdigits.lower(), k=120))
    # Pad to ~512 bytes with random ASCII
    padding = ''.join(random.choices(string.ascii_letters + string.digits, k=KEY_LENGTH - len(signature) - 100))
    
    content = (
        f"RAR registration data\n"
        f"{licensee}\n"
        f"{license_type}\n"
        f"UID={uid}\n"
        f"{signature}\n"
        f"{padding}\n"
    )
    return content

def create_key_files(num_files: int, output_dir: Path) -> List[str]:
    """Generate multiple rarreg.key files with randomized content."""
    output_dir.mkdir(parents=True, exist_ok=True)
    created_files = []
    
    for i in range(num_files):
        file_name = f"{FILE_PREFIX}.key" if i == 0 else f"{FILE_PREFIX}{i}.key"
        file_path = output_dir / file_name
        content = generate_potential_key_content()
        
        with open(file_path, "w", encoding="ascii") as f:
            f.write(content)
        
        created_files.append(str(file_path))
    
    return created_files

def get_valid_input() -> int:
    """Prompt user for the number of files to generate (1 to 100,000)."""
    while True:
        try:
            num_files = int(input(f"Enter the number of rarreg.key files to generate (1-{MAX_FILES:,}): "))
            if 1 <= num_files <= MAX_FILES:
                return num_files
            else:
                print(f"Please enter a number between 1 and {MAX_FILES:,}.")
        except ValueError:
            print("Please enter a valid integer.")

def main():
    print("WinRAR License Key File Generator by SSMG4")
    num_files = get_valid_input()
    print(f"Generating {num_files:,} potential rarreg.key files...")
    start_time = time.time()
    
    created_files = create_key_files(num_files, OUTPUT_DIR)
    
    # Calculate total size
    total_size_mb = (num_files * KEY_LENGTH) / (1024 * 1024)  # Convert bytes to MB
    print(f"\nGenerated {len(created_files):,} files in {OUTPUT_DIR}")
    print(f"Total size: {total_size_mb:.2f} MB")
    print(f"Time taken: {time.time() - start_time:.2f} seconds")
    print(f"Sample files: {created_files[:3] if created_files else []}...")
    print("Note: These are randomly generated and have a very low chance of working. Test in WinRAR to verify.")
    print("\nPress Enter to exit...")
    input()  # Wait for Enter key to exit

if __name__ == "__main__":
    main()