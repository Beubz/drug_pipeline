import pytest
import json
import os
from src.exporter import export_to_json

def test_export_to_json_valid(tmp_path):
    # Temporary JSON file path for testing
    test_output_path = tmp_path / "test_output.json"
    # Example data to be exported to JSON
    test_data = {
        "name": "Test",
        "type": "JSON Test",
        "isValid": True,
        "items": [1, 2, 3, 4, 5]
    }

    # Test exporting valid JSON data to a file
    export_to_json(test_data, test_output_path)
    assert test_output_path.is_file()

    # Verify the contents of the file
    with open(test_output_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        assert data == test_data

def test_export_to_json_exception(tmp_path):
    # Test handling of exceptions, such as invalid file paths
    test_data = {
        "name": "Test",
        "type": "JSON Test",
        "isValid": True,
        "items": [1, 2, 3, 4, 5]
    }
    invalid_path = tmp_path / "/invalide_path/test_output.json"
    
    with pytest.raises(Exception):
        export_to_json(test_data, invalid_path)