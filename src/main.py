import argparse
import pandas as pd

import loader
import transformer
import exporter
import adhoc


def parse_args():
    parser = argparse.ArgumentParser(description="Data pipeline script")
    parser.add_argument('--drugs_path', help='Path to the drugs data file', required=True)
    parser.add_argument('--pubmed_path', help='Path to the pubmed data file', required=True)
    parser.add_argument('--clinical_trials_path', help='Path to the clinical trials data file', required=True)
    parser.add_argument('--pubmed_json_path', help='Path to the pubmed JSON data file', required=True)
    parser.add_argument('--output_path', help='Path to the output file', required=True)
    return parser.parse_args()


def main():
    args = parse_args()

    # step 1 : data loader
    drugs_data = loader.load_csv(args.drugs_path)
    pubmed_data = loader.load_csv(args.pubmed_path)
    clinical_trials_data = loader.load_csv(args.clinical_trials_path)
    pubmed_json_data = loader.load_json(args.pubmed_json_path)
    pubmed_full_data = pd.concat([pubmed_data, pubmed_json_data], ignore_index=True)

    # step 2 : data transformer
    json_data = transformer.create_graph([drugs_data, pubmed_full_data, clinical_trials_data])

    # step 3 : data exporter
    exporter.export_to_json(json_data, args.output_path)


    # step 4 Annexe : Traintement adhoc
    adhoc.find_journal(args.output_path)


if __name__ == "__main__":
    main()