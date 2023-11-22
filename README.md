# Drug Pipeline


## Description

This Python-based data pipeline project aims to create a comprehensive linkage graph connecting various drugs to their mentions in PubMed articles, scientific publications, and journals. The resulting graph is represented in a JSON file, detailing each drug's occurrences with associated publication titles and dates.

## Getting Started

### Installing

How to install :
- Clone the repository: `git clone https://github.com/beubz/drug_pipeline.git`
- Navigate to the project directory: `cd drug_pipeline`
- Install dependencies: `pip install -r requirements.txt`

### Executing program

How to run the program:
- Run the main script: `python src/main.py --drugs_path data/inputs/drugs.csv --pubmed_path data/inputs/pubmed.csv --clinical_trials_path data/inputs/clinical_trials.csv --pubmed_json_path data/inputs/pubmed.json --output_path data/output/graph.json`
- To run the tests: `python -m pytest -s tests`
- See output here : drug_pipeline/data/output/graph.json

