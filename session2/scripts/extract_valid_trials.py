import sys
import pandas as pd

'''
# Command-line inputs
input_csv_path = sys.argv[1]
output_csv_path = sys.argv[2]

# Load the csv file and extract active trials
df = pd.read_csv(input_csv_path)
df_valid = df[df.valid].copy()

# Save the new dataframe as a csv file
df_valid.to_csv(output_csv_path, index=False)

'''

import argparse

#create an argument parser

parser = argparse.ArgumentParser(description="load csv and extract trials")

#addd argument
parser.add_argument("inputcsv",type=str,help="input csv path")
parser.add_argument("outputcsv",type=str,help="output csv path")

args = parser.parse_args()

input_csv_path = args.inputcsv
output_csv_path = args.outputcsv

df = pd.read_csv(input_csv_path)
df_valid = df[df.valid].copy()

df_valid.to_csv(output_csv_path, index=False)
