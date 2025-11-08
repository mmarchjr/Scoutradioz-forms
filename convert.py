# Program to convert JSONC files to JSON by removing comments and fixing formatting issues.

import json
import re
import os
import sys
from typing import Any
def remove_comments(jsonc_str: str) -> str:
    """Remove comments from a JSONC string."""
    pattern = r'//.*?$|/\*.*?\*/'
    regex = re.compile(pattern, re.DOTALL | re.MULTILINE)
    return re.sub(regex, '', jsonc_str)
def convert_jsonc_to_json(input_path: str, output_path: str) -> None:
    """Convert a JSONC file to a JSON file."""
    with open(input_path, 'r', encoding='utf-8') as infile:
        jsonc_content = infile.read()
    
    json_content = remove_comments(jsonc_content)
    
    try:
        parsed_json = json.loads(json_content)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return
    
    with open(output_path, 'w', encoding='utf-8') as outfile:
        json.dump(parsed_json, outfile, indent=4)
    
    print(f"Converted {input_path} to {output_path}")

# Outputs the converted file as "original name - converted.json" in a "converted" directory. Scans current directory for .jsonc files.
if __name__ == "__main__":
    input_directory = os.getcwd()
    output_directory = os.path.join(input_directory, "converted")
    os.makedirs(output_directory, exist_ok=True)

    for filename in os.listdir(input_directory):
        if filename.endswith(".jsonc"):
            input_path = os.path.join(input_directory, filename)
            output_filename = f"{os.path.splitext(filename)[0]} - converted.json"
            output_path = os.path.join(output_directory, output_filename)
            convert_jsonc_to_json(input_path, output_path)