
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: csv_to_bugs.py
Author: remonechev
Description: This script outputs the data in a csv file as text file in the format readable by BUGS software.
"""

# Imports
import os
import sys
import pandas as pd

def convert_to_openbugs_format(df):
    openbugs_data = "list(\n"
    for col in df.columns:
        openbugs_data += f"  {col} = c({', '.join(map(str, df[col]))}),\n"
    openbugs_data = openbugs_data.rstrip(',\n') + "\n)"  # Remove the last comma and close the list
    return openbugs_data

# Main function
def main(args):
    """
    Main function of the script.

    :param args: Command line arguments
    """
    print(args)


    # check correct number of arguments
    if len(args) < 2:
        print("Usage: python3 csv_to_bugs.py <csv_file> [<output_file>] [<separator>] ")
        sys.exit(1)

    csv_file = args[1]
    
    # Check if the file exists
    if not os.path.isfile(csv_file):
        print(f"File {csv_file} does not exist.")
        sys.exit(1)
        
    separator = ',' if len(args) < 3 else args[2]

    # Read the csv file
    df = pd.read_csv(args[1], sep=separator)
    print(f"CSV Data: \n{df.head()}")

    # Convert the sample data to OpenBUGS format
    openbugs_formatted_data = convert_to_openbugs_format(df)

    bugs_data_summary = (openbugs_formatted_data[:1000] if len(openbugs_formatted_data) > 1000 else openbugs_formatted_data)
    print(f"BUGS Data: \n{bugs_data_summary}")

    output_file = csv_file.replace(".csv", ".txt") if len(args) < 3 else args[2]

    # Write the data to a file
    with open(output_file, 'w') as f:
        f.write(openbugs_formatted_data)

# Entry point of the script
if __name__ == "__main__":
    main(sys.argv)