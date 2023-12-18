from typing import Dict, Callable
import subprocess
from dataclasses import dataclass
import re

@dataclass
class SimSettings:
    job_name: str
    script_path: str
    input_path: str
    num_cpus: int
    num_gpus: int
    mem_size_mb: int
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

def create_job_control(settings: SimSettings) -> str:
    return f"""
job = mdb.Job(
    name='{settings.job_name}', 
    model='Model-1', 
    description='', 
    type=ANALYSIS, 
    atTime=None, 
    waitMinutes=0, 
    waitHours=0, 
    queue=None, 
    memory={settings.mem_size_mb}, 
    memoryUnits=MEGA_BYTES, 
    getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, 
    nodalOutputPrecision=SINGLE, 
    echoPrint=OFF, 
    modelPrint=OFF, 
    contactPrint=OFF, 
    historyPrint=OFF, 
    userSubroutine='', 
    scratch='{settings.scratch_path}', 
    resultsFormat=ODB, 
    numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, 
    numCpus={settings.num_cpus}, 
    numDomains=1, 
    numGPUs={settings.num_gpus}
)

job.submit(consistencyChecking=OFF)
job.waitForCompletion()
    """
    # TODO(marco): Add result conversion

def run_sim(settings: SimSettings):
    # TODO(marco): Set correct file paths in script

    template_path = f'templates/{settings.job_name}.py'
    script_path = f'scripts/{settings.job_name}.py'
     
    script = read_file(template_path)
    # Remove existing job control
    script = re.sub(r"mdb\.jobs\[.*submit\(.*\)", '# DELETED', script)
    script = re.sub(r"mdb\.jobs\[.*waitForCompletion\(.*\)", '# DELETED', script)
    script = re.sub(r"mdb\.jobs\[.*writeInput\(.*\)", '# DELETED', script)
    script = re.sub(r"session\.viewports\[.*(\n\s.*)*", '# DELETED', script)
    script = re.sub(r".*session\.openOdb.*", '# DELETED', script)
    script = re.sub(r"session\.odbs.*", '# DELETED', script)
    script = re.sub(r"(?s)mdb\.Job\(.*?\)", '# DELETED', script)
    
    material_file = '1_Combined_WBS355MC_211340.csv'
    script.replace('materal_path', 'materials/'+material_file)
    # Append custom job control
    script += create_job_control(settings)
    write_file(script_path, script)

    # Run script
    output = exec_command(f'abaqus cae noGUI={script_path}')
    if output.returncode != 0:
        print("Abaqus script execution failed!")
        print(output.stderr)

    print("Simulation done")

def main() -> None:
    settings = SimSettings(
        job_name='test',
        script_path='script/test.py',
        input_path='test.inp',
        num_cpus=1,
        num_gpus=0,
        mem_size_mb=4000,
        scratch_path='',
    )
    run_sim(settings)

if __name__ == '__main__':
    main()
