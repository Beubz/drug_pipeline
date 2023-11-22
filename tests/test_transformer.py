import pytest
import pandas as pd
from src.transformer import clean_input_data, create_json_data  

# Mock data 
mock_clinical_trials = pd.DataFrame({
    'id': ['NCT00001', 'NCT00002', 'NCT00003', 'NCT00004'],
    'scientific_title': ['Study of Drug A', 'Research on Drug B', None, 'Analysis of Drug C\\xa0'],
    'date': ['01/01/2020', '01/02/2020', '01/03/2020', '01/04/2020'],
    'journal': ['Journal A', 'Journal B', 'Journal C', None]
})

mock_drugs = pd.DataFrame({
    'atccode': ['A01', 'A02', 'A03', 'A04'],
    'drug': ['Drug A', 'Drug B', 'Drug C', 'Drug D\\x9c']
})

mock_pubmed = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'title': ['Study on Drug A', 'Effects of Drug B', 'Drug C Research', ' '],
    'date': ['01/01/2020', '01/02/2020', '01/03/2020', '01/04/2020'],
    'journal': ['Journal A', 'Journal B', 'Journal C', 'Journal D']
})

def test_clean_input_data():
    cleaned_data = clean_input_data(mock_clinical_trials)
    # Check that there are no None values
    assert cleaned_data.isnull().sum().sum() == 0
    # Check for the removal of hex characters and whitespace
    for col in cleaned_data.columns:
        assert not any('\\x' in str(x) for x in cleaned_data[col])
        assert all(str(x).strip() == str(x) for x in cleaned_data[col])

def test_create_json_data():
    json_data = create_json_data([mock_drugs, mock_pubmed, mock_clinical_trials])
    # Check for the presence of key components in the JSON data
    assert 'drugs' in json_data
    assert 'drugs_in_pubmed' in json_data
    assert 'drugs_in_journal' in json_data
    assert 'drug_in_clinical_trials' in json_data

# Run tests with pytest
if __name__ == "__main__":
    pytest.main()