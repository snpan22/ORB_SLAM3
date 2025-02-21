import os

# Ask the user for the input and output file names (assuming the script is run in the correct directory)
input_file = input("Enter the name of the input file (e.g., f_dataset-MH01_mono.txt): ")
output_file = input("Enter the desired output file name (e.g., f_dataset-MH01_mono_comma_2.txt): ")

# Check if the input file exists in the current directory
if not os.path.isfile(input_file):
    print(f"Error: The input file '{input_file}' was not found in the current directory.")
else:
    try:
        # Read the space-delimited file
        with open(input_file, 'r') as infile:
            lines = infile.readlines()

        # Write to a new comma-delimited file
        with open(output_file, 'w') as outfile:
            for line in lines:
                # Remove extra spaces and replace them with commas
                line = line.strip().replace(' ', ',')
                # Write the converted line to the output file
                outfile.write(line + '\n')

        print(f"Converted file saved to: {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")
