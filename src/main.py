from typing import Dict, Callable
import subprocess

def exec_command(command: str) -> subprocess.CompletedProcess[bytes]:
    """Executes the provided terminal command."""
    output = subprocess.run(command.split(" "), capture_output=True, shell=True)
    return output

def read_file(path: str) -> str:
    """Reads a file and returns its content."""
    file = open(path, "r")
    content = file.read()
    file.close()
    return content

def write_file(path: str, content: str) -> None:
    """Creates/overwrites a file with the provided content."""
    file = open(path, "w")
    file.write(content)
    file.close()

def replace_all(text: str, replace: Dict[str, str|Callable[[], str]]) -> str:
    """Replaces all the dict keys with the dict values in the provided text."""
    for old_str, new_str in replace.items():
        if isinstance(new_str, Callable): 
            new_str = new_str()

        text = text.replace(old_str, new_str)
    return text

def main():
    output = exec_command('abaqus cae noGUI=journal/test.py')
    print(output)

if __name__ == '__main__':
    main()
