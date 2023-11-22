import json


def export_to_json(json_data, output_path):
	"""
	Exports the given data to a JSON file.

	:param json_data: The data to be exported in JSON format.
	:param output_path: The file path where the JSON data will be saved.
	"""
	try:
		# Convert the data to a JSON-formatted string with indentation for readability
		json_output = json.dumps(json_data, indent=4, ensure_ascii=False)

		# Write the JSON string to the specified file path
		with open(output_path, 'w') as file:
			file.write(json_output)
		print(f"The JSON is created here : {output_path}")

	except Exception as e:
		# Print an error message if something goes wrong
		print(f"An error occurred while writing to the file: {e}")
		raise