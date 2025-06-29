import papermill as pm
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from itertools import product
from pathlib import Path
import os

# Define Parameter Grids
ls_param_grid = {
    'input_file_name': ['races.csv', 'results.csv']
}

# Define Notebooks
ls_param_notebooks = ['Notebooks/NB_2_Bronze.ipynb']
ls_other_notebooks = ['Notebooks/NB_3_Silver.ipynb', 'Notebooks/NB_4_Gold.ipynb']

# Generate all parameter combinations
v_keys = ls_param_grid.keys()
ls_param_combinations = [dict(zip(v_keys, v_values)) for v_values in product(*ls_param_grid.values())]

# Execute the parameterized notebook(s)
for notebook in ls_param_notebooks:
    for idx, params in enumerate(ls_param_combinations):
        output_path = f"executed_{notebook.split('.')[0]}_run{idx+1}.ipynb"
        pm.execute_notebook(
            notebook,
            output_path,
            parameters=params
        )
        print(f"Executed {notebook} with {params} -> {output_path}")

# Execute the other notebooks without parameters
for notebook in ls_other_notebooks:
    with open(notebook) as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=600)
    ep.preprocess(nb)

    output_path = f"executed_{notebook}"
    with open(output_path, "w") as f:
        nbformat.write(nb, f)

    print(f"Executed {notebook} -> {output_path}")
