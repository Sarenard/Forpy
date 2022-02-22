import src.Exceptions as Exceptions
from src.Interpreter import Interpreter
from src.Parser import Parser
import sys


if len(sys.argv) < 2:
    print("You don't specified a file !")
    raise Exceptions.NoFileSpecified("Not enough arguments for the program, usage : main.py [file.forpy]")

parser = Parser(sys.argv[1])
interpreter = Interpreter(parser.generate_instructions())
interpreter.run()