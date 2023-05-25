import pandas as pd
import json

# Load JSON data from file
with open('nested_data_2.json') as file:
    data = json.load(file)

# Helper function to recursively flatten nested JSON
def flatten_json(data, prefix=''):
    flattened_data = {}
    for key, value in data.items():
        if isinstance(value, dict):
            flattened_data.update(flatten_json(value, prefix + key + '_'))
        elif isinstance(value, list):
            for i, item in enumerate(value):
                flattened_data.update(flatten_json(item, prefix + key + f'_{i}_'))
        else:
            flattened_data[prefix + key] = value
    return flattened_data

# Flatten nested JSON data
flattened_data = flatten_json(data)

# Create DataFrame
df = pd.DataFrame([flattened_data])

# Display the DataFrame
print(df)
