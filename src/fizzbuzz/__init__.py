from rich import print

__version__ = '0.1.0'

def main(start=1, stop=100, step=1, fizz=3, buzz=5):
	"""FizzBuzz: A childhood game turned interview question

	Args:
		start (int, optional): The value of i at the start of the loop. Defaults to 1.
		stop (int, optional): The loop gets stopped when i reaches this number. Defaults to 100.
		step (int, optional): i gets incremented by step every iteration of the loop. Defaults to 1.
		fizz (int, optional): Multiples of this number are replaced by the phrase \"Fizz\". Defaults to 3.
		buzz (int, optional): Multiples of this number are replaced by the phrase \"Buzz\". Defaults to 5.
	"""
	for i in range(start, stop, step):
		output = ""
		if i % fizz == 0:
			output = output + "[bold green]Fizz[/bold green]"
		if i % buzz == 0:
			output = output + "[bold blue]Buzz[/bold blue]"
		if output == "":
			output = str(i)
		print(output)
	return(0)
