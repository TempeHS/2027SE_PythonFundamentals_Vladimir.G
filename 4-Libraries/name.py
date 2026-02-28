import sys

if len(sys.argv) < 2:
    print("Error")

for arg in sys.argv[1:]:
    print("hello my name is", arg)
