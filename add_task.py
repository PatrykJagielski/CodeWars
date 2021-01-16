import os
import sys


if __name__ == "__main__":
    path = f'{os.getcwd()}/{sys.argv[1]}'

    try:
        os.mkdir(path)
    except OSError:
        print(f"Creation of the directory {path} failed")
    else:
        print(f"Successfully created the directory {path}")

    os.mknod(f'{path}/instructions.md')
    os.mknod(f'{path}/solution.py')
    os.mknod(f'{path}/best_solution.py')
