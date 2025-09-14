import os

## This command will list files in your working directory
files = os.listdir()


## This line will enable you to tell the interpreter
### the actual logic starts here
## It exists essentially to avoid infinite loop when defining
### and importing functions across several files
if __name__ == "__main__":
    print("Hello, World!")
    print(files)