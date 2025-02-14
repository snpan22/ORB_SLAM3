# File paths
input_file = 'f_dataset-MH01_mono.txt'  # Replace with your actual input file path
output_file = 'f_dataset-MH01_mono_comma_2.txt'  # Desired output file path (comma-delimited)

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
