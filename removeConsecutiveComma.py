import csv

def remove_consecutive_commas(input_csv, output_csv):
    with open(input_csv, 'r', newline='', encoding='utf-8') as infile, open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            # Remove consecutive commas in each cell
            cleaned_row = [','.join(cell if cell else 'MISSING' for cell in row)]
            
            # Write the cleaned row to the output CSV
            writer.writerow(cleaned_row)


# Example usage
input_file = '/home/deluca-ubuntu/products/coty/loreal_no_header.csv'
output_file = '/home/deluca-ubuntu/products/coty/loreal_without_commas.csv'

remove_consecutive_commas(input_file, output_file)
