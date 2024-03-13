import csv

def remove_quotes_from_csv(input_csv, output_csv):
    with open(input_csv, 'r', newline='', encoding='utf-8') as infile, open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            # Remove double quotes from each element in the row
            cleaned_row = [cell.replace('"', '') for cell in row]
            writer.writerow(cleaned_row)

input_file = '/home/deluca-ubuntu/products/coty/loreal_without_commas.csv'
output_file = '/home/deluca-ubuntu/products/coty/loreal_without_quotes.csv'

remove_quotes_from_csv(input_file, output_file)
