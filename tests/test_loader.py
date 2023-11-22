import pytest
import pandas as pd
from src.loader import load_csv, load_json

def test_load_csv_valid():
    # Test loading a valid CSV file
    result = load_csv('data/inputs/drugs.csv')
    assert isinstance(result, pd.DataFrame)

def test_load_csv_invalid():
    # Test loading an invalid or non-existent CSV file
    with pytest.raises(Exception):
        load_csv('invalide_path/file.csv')

def test_load_json_valid():
    # Test loading a valid JSON file
    result = load_json('data/inputs/pubmed.json')
    assert isinstance(result, pd.DataFrame)

def test_load_json_invalid():
    # Test loading an invalid or non-existent JSON file
    with pytest.raises(Exception):
        load_json('invalide_path/file.json')