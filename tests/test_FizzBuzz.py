from subprocess import run
from pathlib import Path
from types import NoneType
from rich.pretty import pprint
from fizzbuzz import __version__

src = Path(__file__ + "/../../src")

def test_version():
	assert __version__ == '0.1.0'

def test_3_5():
	proc = run("py fizzbuzz", capture_output=True, cwd=src)
	out = proc.stdout.split(b"\r\n")
	err = proc.stderr
	assert out and not err
	assert out[2] == b"Fizz"

def test_3_4():
	proc = run("py fizzbuzz -B=4", capture_output=True, cwd=src)
	out = proc.stdout.split(b"\r\n")
	err = proc.stderr
	assert out and not err
	assert out[2] == b"Fizz" and out[3] == b"Buzz"

def test_3_3():
	proc = run("py fizzbuzz -B=3", capture_output=True, cwd=src)
	out = proc.stdout.split(b"\r\n")
	err = proc.stderr
	assert out and not err
	for line_num in range(2, len(out) - 1, 3):
		assert out[line_num] == b"FizzBuzz"

def test_1_1():
	proc = run("py fizzbuzz -F=1 -B=1", capture_output=True, cwd=src)
	out = proc.stdout.split(b"\r\n")
	err = proc.stderr
	assert out and not err
	for line_num in range(0, len(out) - 1):
		assert out[line_num] == b"FizzBuzz"

if __name__ == "__main__":
	test_3_5()
	test_3_4()
	test_3_3()
	test_1_1()