# Abaqus Automation

The goal of this project is to automate the creation and execution of Abaqus simulations.

# Usage

## Templates

The automation script allows modifying Abaqus job scripts before execution in an programmatic manner.

The job scripts are placed in the `template` directory of this project.
The template is read by the automation script before the simulation is started and all placeholder are replaced by predefined values.
The placeholders and replacement values are defined in the file `src/main.py`, where they can be easily changed.
For examples, it is possible to automaticlly insert custom material parameters or add random variance to the model.

```python
# Using material parameters defined in a seperate file
def run_sim(settings: SimSettings):
    ...
    script = read_file(template_path)
    ...
    material_file = 'my_material.csv'
    script = script.replace('material_path', 'materials/'+material_file)
    ...
    write_file(script_path, script)
```

Additionally, the automation script removes all previous job submission commands from the template and inserts a new commit command at the end.
The parameters for the job sumbission are also defined in the file `src/main.py`, where they can be changed.

```python
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
```

After all replacements are done, the final job script is saved to the directory `scripts` and the simulation is started.

## Data Extraction

Abaqus stores the simulation in `.odb` files.
Since they require a Abaqus license to open, we provide a script to extract data to a `.json` file.

To execute to data extraction, run `python src/data_extraction.py` in the terminal.

## Data Conversion

When storing large amount of data from multiple simulations, the JSON format is a bad choice, not only with respect to storage size, but also reading times.

TODO(marco) Continue

