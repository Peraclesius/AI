import subprocess

def is_alias(path):
    print(subprocess.check_output(["python3", "-aa", path]) == "1\n")