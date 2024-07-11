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
