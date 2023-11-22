import pandas as pd
import json


def load_csv(file_path):
	"""
	Load a CSV file into a Pandas DataFrame.

	:param file_path: Path to the CSV file to be loaded.
	:return: Pandas DataFrame containing data from the CSV file.
	"""
	try:
		data = pd.read_csv(file_path, encoding='utf-8')
		return data
	except Exception as e:
		print(f"Error loading CSV file: {file_path}")
		print(e)
		raise  


def load_json(file_path):
	"""
	Load a JSON file into a a Pandas DataFrame.

	:param file_path: Path to the JSON file to be loaded.
	:return: Pandas DataFrame containing data from the JSON file.
	"""
	try:
		with open (file_path, encoding='utf-8') as file:
			data_json =  json.load(file)
		return pd.DataFrame(data_json)
	except Exception as e:
		print(f"Error loading JSON file: {file_path}")
		print(e)
		raise
