from typing import Dict, Callable
import subprocess
from dataclasses import dataclass


@dataclass
class SimSettings:
    job_name: str
    script_path: str
    input_path: str
    num_gpus: int
    mem_size_gb: int
    scratch_path: str

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
    """Replaces all dict keys with the corresponding dict values in the provided text."""
    for old_str, new_str in replace.items():
        if isinstance(new_str, Callable): 
            new_str = new_str()

        text = text.replace(old_str, new_str)
    return text

def run_sim(settings: SimSettings):
    # TODO(marco): Set correct input file path in script
    output = exec_command(f'abaqus cae noGUI={settings.script_path}')
    if output.returncode != 0:
        print("Could not execute journal file!")
        print(output.stderr)
        return

    sim_command = f'abaqus job={settings.job_name} gpus={settings.num_gpus} memory={settings.mem_size_gb} scratch={settings.scratch_path} input={settings.input_path}'
    output = exec_command(sim_command)

def main() -> None:
    settings = SimSettings(
        job_name='test',
        script_path='journal/test.py',
        input_path='test.inp',
        num_gpus=4,
        mem_size_gb=4,
        scratch_path='scratch',
    )
    run_sim(settings)


if __name__ == '__main__':
    main()
