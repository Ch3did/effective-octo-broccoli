import argparse

def decorator(func):
    parser = argparse.ArgumentParser(description='Update env Credentials')
    parser.add_argument('-t', help='Type', required=True)
    args = vars(parser.parse_args())
    def wrapper(args):
        func(args)
    return wrapper(args['t'])



@decorator
def update(var: dict)-> None:
    gambiarra = "number of" if "months" in var else ""
    new_var = input(f"Enter the new {gambiarra} {var.lower()}: ")
    with open('env', 'r') as file:
        lines = file.readlines()
    with open('env', 'w') as file:
        for line in lines:
            if line.startswith(f'{var.upper()}='):
                line = f'{var.upper()}="{new_var}"\n'
            file.write(line)
    print(f"{var.title()} successfully updated in the env file.")




