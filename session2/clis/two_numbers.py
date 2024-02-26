import argparse

#create an argument parser

parser = argparse.ArgumentParser(description="Add numbers")

#addd argument
parser.add_argument("number1",type=float,help="first number")
parser.add_argument("number2",type=float,help="second number")

args = parser.parse_args()

result = args.number1 + args.number2

print(f"The addition of these numbers is:{result}")

