import argparse

#create an argument parser

parser = argparse.ArgumentParser(description="Greeting user")

#create arguments and store as string and a help text explaining the arg
parser.add_argument('name',type=str,help="Name of the user")

#create optional arguments
parser.add_argument('--group',type=str, default="iBehave" ,help="which group someone belongs to")

#parse the argument
args = parser.parse_args()

#prints the args value and the arg parsed previously
print(f"Hello, {args.name}! {args.name} is part of {args.group}")

