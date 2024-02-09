import csv

def remove_header(input_csv, output_csv):
    with open(input_csv, 'r', newline='', encoding='utf-8') as infile, open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Skip the header lines
        for _ in range(15):  # Assuming the header is in the first 15 lines
            next(reader, None)

        # Write the remaining rows (excluding the header) to the output CSV
        for row in reader:
            writer.writerow(row)

# Example usage
input_file = '/home/deluca-ubuntu/products/coty/loreal_output_utf8.csv'
output_file = '/home/deluca-ubuntu/products/coty/loreal_no_header.csv'

remove_header(input_file, output_file)
