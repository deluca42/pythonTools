import csv
import io

def generate_create_table_script(csv_line, table_name='your_table'):
    # Read a CSV line to infer column names and data types
    csv_reader = csv.reader(io.StringIO(csv_line))
    header = next(csv_reader)

    # Generate a CREATE TABLE script
    create_script = f"CREATE TABLE {table_name} (\n"

    for col_name, value in zip(header, csv_line.split(',')):
        data_type = 'TEXT'
        try:
            # Attempt to infer data type based on the value
            float(value)
            data_type = 'NUMERIC'
        except ValueError:
            pass

        create_script += f"    {col_name.strip()} {data_type},\n"

    create_script = create_script.rstrip(',\n') + "\n);"

    return create_script

# Example CSV line
csv_line = "636582,,ARMANZ,GA ARMANZ NEW EDT 50ML,1,,,,,,353.5,359.8928,359.9,0,359.9,,,0,,33030020,2000800,3614273636582,0.249,50,5.4,5.3,9.8,549,559"

# Generate CREATE TABLE script
script = generate_create_table_script(csv_line)

# Print the script
print(script)
