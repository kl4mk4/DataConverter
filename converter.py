import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Data Converter')
    parser.add_argument('input_file', type=str, help='Path to the input file')
    parser.add_argument('output_file', type=str, help='Path to the output file')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    print(f"Input file: {args.input_file}")
    print(f"Output file: {args.output_file}")

import json

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError as e:
        print(f"Invalid JSON format: {e}")
        return None
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        return None

if __name__ == "__main__":
    args = parse_args()
    data = load_json(args.input_file)
    if data:
        print("JSON file loaded successfully.")
        print(data)
