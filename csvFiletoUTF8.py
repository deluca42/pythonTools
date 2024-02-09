import csv
import chardet

def detect_file_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

def convert_to_utf8(input_csv, output_csv):
    # Detect the current encoding of the input CSV file
    current_encoding = detect_file_encoding(input_csv)

    # Convert the CSV file to UTF-8
    with open(input_csv, 'r', newline='', encoding=current_encoding) as infile, \
         open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            # Write the row to the output CSV file
            writer.writerow(row)

# Example usage
input_file = '/home/deluca-ubuntu/products/Coty/Loreal.csv'
output_file = '/home/deluca-ubuntu/products/Coty/loreal_output_utf8.csv'

convert_to_utf8(input_file, output_file)
