import argparse

#create an argument parser

parser = argparse.ArgumentParser(description="Add numbers")

#addd argument
parser.add_argument("number1",type=float,help="first number")
parser.add_argument("number2",type=float,help="second number")
parser.add_argument("--scale",type=int,default=1,help="scaling factor")

args = parser.parse_args()

result = args.number1 + args.number2 * args.scale

print(f"The result is:{result}")

