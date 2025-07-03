# WinRARE
A WinRAR license key generator made in Python

## Info
- The chances of getting a working license is pretty low (in the name WinRARE)
- The tool can generate up to 100,000 license at once (might make your PC lag/bug when asking for lots of licenses)
- The tool saves the licenses in the C:\ drive in the Downloads folder under the generated "RarRegKeys" folder
- To add a license, put one inside WinRAR's program files (usually located in C:\Program Files\WinRAR)

## Creating a Windows Executable
To make a standalone `.exe`:
1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. download the script `rar.py` and compile (inside the script's location):
   ```bash
   pyinstaller --onefile rar.py
   ```
3. Find `dist/generate_rarreg_keys.exe` and double-click to run, creating files in `~/Downloads/RarRegKeys`.

&copy; 2025 SSMG4 All Rights Reserved.
