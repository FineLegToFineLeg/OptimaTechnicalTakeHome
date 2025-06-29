# Solution README

This project is a Python-based data pipeline designed to perform the transformation of Formula 1 race data into structured JSON files. The pipeline processes race and results data, generating one JSON file per year containing key statistics for each race. The output is intended to support rapid analysis for a motorsport analytics YouTube channel, providing easily accessible, structured data shortly after each race.

## Table of Contents

- [Overview](#Overview)
- [Installation](#installation)
- [Usage](#usage)
- [Future](#future)

## Overview

The solution is made up of 5 notebooks and a main executable script to run the pipeline itself:

- NB_1_Common_Functions
- NB_1_Settings
- NB_2_Bronze
- NB_3_Silver
- NB_4_Gold
- main.py

The executable script runs the notebooks, in order, for the results.csv and races.csv files to generate jsons in the required outputs. Note that the pipeline has been structured using the medallion archietecutre and has been implemented with scalability in mind in order to allow other files to be added into the mini data platform if required.

**The following requirements have been met:**
- Develop a data pipeline that produces JSON files which have the same structure as below.
- Each element in the list should be for one race from the races.csv file.
- You should produce one file per year available in the source data.
- Your JSON files should be called stats_{year}.json, one for each year and be placed in the results folder.
- If the time is not available in races.csv, use 00:00:00.
- If the JSON value for a key is always a number, represent it as such rather than a string.
- Unit tests and some logging is included for functions found in NB_1_Common Functions.
- Notes in the [Future](#future) of this file outline the tools you might use to deploy this pipeline to a cloud provider and what kind of considerations you'd need to make in doing so.
- Further considerations and improvements to this solution are also discussed.

## Installation

1. Run the following command to install all of the requirements for this script

```bash
pip install -r requirements.txt
```

2. Use the following command to ensure the pipeline is being run in the correct location:

```bash
cd data-engineering\datapipeline\solution
```

## Usage

1. Excecute the pipeline by running the following command:

```bash
python main.py
```

After running, the output files will be found in the results/gold folder for further usage. Any errors and notes will be produced in Logs.csv file.

## Future

While this solution does not require deploying the solution to a cloud provider, it is designed with future scalability in mind. In a production environment, data pipelines like this would typically be deployed into a cloud storage-backed, managed solution. It would also be suggested to move towards a metadata based ingestion framework for maximum scalability to allow more files of both structured and unstructured formats to be ingested into storage.

An example stack for this workflow would be as follows:

| Tool/Service                       | Purpose                                                                                                                             |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Azure Data Lake Storage (ADLS)** | Centralised storage for raw, processed, and results data (e.g., `.csv`, `.json`)                                                    |
| **Azure Databricks**               | Managed platform for executing notebooks and large-scale data processing with Apache Spark                                          |
| **Databricks Workflows**           | Fully managed orchestration and scheduling of notebook execution, replacing the need for local orchestration scripts like `main.py` |
| **Azure DevOps**                   | CI/CD pipelines for automated deployment, version control, and testing                                                              |

### Considerations when deploying to Databricks

**Notebook Migration:**
Existing Jupyter notebooks (NB_2_Bronze.ipynb, NB_3_Silver.ipynb, NB_4_Gold.ipynb) would be migrated to the Databricks workspace via the UI or Databricks CLI.

**Code Refactoring to PySpark:**
To utilise Databricks' distributed processing capabilities, parts of the notebook logic would be converted to PySpark.

**Orchestration Replacement:**
The current main.py file used for local orchestration would become redundant. Instead, Databricks Workflows would manage notebook execution, dependencies, and scheduling.

**Environment Management:**
Python dependencies would be managed within Databricks using cluster libraries or Databricks environment configurations.

### Additional Considerations

**Data Security:**
Apply strict access controls using Azure RBAC, secret scopes, and service principals.

**Monitoring & Logging:**
Utilize Databricks' job monitoring and integrate with Azure Monitor, Log Analytics, or similar tools for pipeline health tracking.

**Scalability:**
Leverage Databricks' autoscaling clusters to efficiently handle varying data volumes.

**Cost Management:**
Implement cost controls and regularly monitor resource usage to avoid unnecessary expenses.
