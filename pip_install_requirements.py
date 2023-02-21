import os
import sys
import subprocess

file_dir = os.path.join(os.path.dirname(__file__))
sys.path.append(file_dir)

def pip_install(module):
    try:
        proc = subprocess.Popen(f"python -m pip install {module}")
        proc.communicate()
        print(f"{module} : SUCCESS")
    except:
        print(f"{module} : FAILED")


def readRequirements(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    lines = [line.rstrip('\n') for line in lines]

    targets = []
    for line in lines:
        if line.startswith("#") or line == "":
            targets.append(line)

    for target in targets:
        lines.remove(target)

    print(lines)
    return lines

if __name__ == "__main__":
    modules = readRequirements("requirements.txt")
    for module in modules:
        pip_install(module)