import os
import csv
import sys

input_folder = 'sale'
output_folder = 'propre'

os.makedirs(output_folder, exist_ok=True)

csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]

if not csv_files:
    print("No files found in the folder 'sale...")
    sys.exit(1)
else:
    for filename in csv_files:
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        with open(input_path, mode='r', encoding='utf-8') as infile, \
            open(output_path, mode='w', encoding='utf-8', newline='') as outfile:
            reader = csv.reader(infile, delimiter='$')
            writer = csv.writer(outfile, delimiter=',')

            for row in reader:
                writer.writerow(row)

print("All files are converted and registered in the folder 'propre'")
sys.exit(0)
