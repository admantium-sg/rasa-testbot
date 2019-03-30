from rasa_nlu.model import Metadata, Interpreter
import json
import sys

def pprint(o):
 # small helper to make dict dumps a bit prettier
    print(json.dumps(o, indent=2))

def show_args():
   print("This is the name of the script: ", sys.argv[0])
   print("Number of arguments: ", len(sys.argv))
   print("The arguments are: " , str(sys.argv))

interpreter = Interpreter.load('./model/current/nlu')
show_args()
pprint(interpreter.parse(sys.argv[1]))
