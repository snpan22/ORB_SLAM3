import csv
import os

# Ask the user for the input CSV file name and the output TXT file location
input_file = input("Enter the name of the input CSV file (e.g., data.csv): ")
output_file_path = input("Enter the full path for the output TXT file (e.g., /path/to/destination/data.txt): ")

# Check if the input file exists
if not os.path.isfile(input_file):
    print(f"Error: The file '{input_file}' was not found.")
else:
    try:
        # Open the CSV input file
        with open(input_file, 'r') as infile:
            csv_reader = csv.reader(infile)
            
            # Create the output directory if it doesn't exist
            output_dir = os.path.dirname(output_file_path)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            # Open the specified output file
            with open(output_file_path, 'w') as outfile:
                for row in csv_reader:
                    # Join the row items with a space and write to the output file
                    outfile.write(','.join(row) + '\n')  # Or use '\t'.join(row) for tab separation

        print(f"Conversion complete. The data is saved to: {output_file_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
