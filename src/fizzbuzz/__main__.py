from argparse import ArgumentParser
import sys, fizzbuzz

parser = ArgumentParser(prog="fizzbuzz.py", description="FizzBuzz: A childhood game turned computer sciense interview question")
parser.add_argument("-s", "--start", dest="start", type=int, default=1, help="The value of i at the start of the loop.")
parser.add_argument("-f", "--stop", dest="stop", type=int, default=101, help="The loop gets stopped when i reaches this number.")
parser.add_argument("-S", "--step", dest="step", type=int, default=1, help="i gets incremented by step every iteration of the loop.")
parser.add_argument("-F", "--fizz", dest="fizz", type=int, default=3, help="Multiples of this number are replaced by the phrase \"Fizz\".")
parser.add_argument("-B", "--buzz", dest="buzz", type=int, default=5, help="Multiples of this number are replaced by the phrase \"Buzz\".")

def run():
	"""Runs the program with all command-line arguments.
	"""
	args = parser.parse_args()
	start, stop, step, fizz, buzz = args.start, args.stop, args.step, args.fizz, args.buzz
	sys.exit(fizzbuzz.main(start, stop, step, fizz, buzz))

if __name__ == "__main__":
	run()