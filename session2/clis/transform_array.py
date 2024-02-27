from argparse import ArgumentParser
import numpy as np

parser = ArgumentParser(description="transform an array file")

parser.add_argument("infile", type=str,help="an .npy file to be analysed")
parser.add_argument("outfile", type=str,help="an .npy file to be analysed")

parser.add_argument("--operation",type=str,default="standardised",choices=["normalised","standardised"])

args = parser.parse_args()

if args.operation == "normalised":
    input_array_path = args.infile # grab the first input
    output_array_path = args.outfile # grab the second input

    # Load the input and standardize it
    input_array = np.load(input_array_path)
    output_array = (input_array - np.min(input_array)) / np.max(input_array)
    print("normalised")
elif args.operation == "standardised":
    # Command-line inputs
    input_array_path = args.infile # grab the first input
    output_array_path = args.outfile # grab the second input

    # Load the input and standardize it
    input_array = np.load(input_array_path)
    output_array = (input_array - np.mean(input_array)) / np.std(input_array)

    # Save the standardized array
    np.save(output_array_path, output_array)    
    print("standardised")
else: 
    raise ValueError("Hey, I don't know what to do, silly!")

# Command-line inputs


# Save the standardized array
np.save(output_array_path, output_array)