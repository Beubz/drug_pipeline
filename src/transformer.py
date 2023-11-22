import pandas as pd


def clean_input_data(df):
	"""
	Clean the input DataFrame by handling missing values, encoding issues, and other anomalies.

	:param df: pandas DataFrame to be cleaned.
	:return: Cleaned pandas DataFrame.
	"""
	for col in df.columns:
		# Drop empty values - not the best option, depending on usecases
		df.dropna(subset=[col], inplace=True)

		# Convert or replace non-UTF-8 characters
		df[col] = df[col].apply(lambda x: x.encode('utf-8', errors='replace').decode('utf-8') if isinstance(x, str) else x)

		# Strip whitespace from the beginning and end of strings
		df[col] = df[col].str.strip()
			
		#Specific to this exercice 
		df[col] = df[col].str.replace(r'\\x[0-9a-fA-F]{2}', '', regex=True)
		
		# Attempt to normalize date columns to a standard format
		if col == 'date':
			df[col] = [pd.to_datetime(x, errors='coerce', dayfirst=True).strftime('%Y-%m-%d') 
				if pd.notnull(x) else x for x in df[col]]
	return df


def create_json_data(df_list):
	"""
	Creates a JSON structure from a list of DataFrames.

	:param df_list: List of DataFrames [drugs_data, pubmed_full_data, clinical_trials_data].
	:return: Dictionary representing the desired JSON structure.
	"""
	drugs_data = df_list[0]
	pubmed_full_data = df_list[1]
	clinical_trials_data = df_list[2]



	# Create the basic structure
	json_data = {
		'drugs': [],
		'drugs_in_pubmed': [],
		'drugs_in_journal': [],
		'drug_in_clinical_trials': []
	}

	# Add unique drugs
	json_data['drugs'] = drugs_data['drug'].unique().tolist()

	# Set to keep track of added drug-journal combinations
	added_drug_journal = set()

	for drug in json_data['drugs']:

		
		#drugs_in_pubmed
		for _, pubmed_row in pubmed_full_data.iterrows():
			if drug.lower() in pubmed_row['title'].lower():
				json_data['drugs_in_pubmed'].append({'drug': drug, 'pubmed_article': pubmed_row['title'], 'date': pubmed_row['date']})
				
				#drugs_in_journal from pubmed
				drug_journal_key = (drug, pubmed_row['journal'])
				if drug_journal_key not in added_drug_journal:
					json_data['drugs_in_journal'].append({'drug': drug, 'journal': pubmed_row['journal'], 'date': pubmed_row['date']})
					added_drug_journal.add(drug_journal_key)

		#drugs_in_trial
		for _, trial_row in clinical_trials_data.iterrows():
			if drug.lower() in trial_row['scientific_title'].lower():
				json_data['drug_in_clinical_trials'].append({'drug': drug, 'trial': trial_row['scientific_title'], 'date': trial_row['date']})
				
				#drugs_in_journal from trials
				drug_journal_key = (drug, trial_row['journal'])
				if drug_journal_key not in added_drug_journal:
					json_data['drugs_in_journal'].append({'drug': drug, 'journal': trial_row['journal'], 'date': trial_row['date']})
					added_drug_journal.add(drug_journal_key)

	return json_data


def create_graph(df_list):
	"""
	Creates a graph structure from a list of DataFrames after cleaning the dataframes.

	:param df_list: List of DataFrames to process.
	:return: JSON data representing the graph.
	"""
	# Clean DataFrame
	df_list = [clean_input_data(df) for df in df_list]

	# Create JSON data
	json_data = create_json_data(df_list)

	return json_data


