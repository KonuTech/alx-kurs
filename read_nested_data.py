import pandas as pd
import json

# Load JSON data from file
with open('nested_data.json') as file:
    data = json.load(file)

# Flatten nested JSON data
flattened_data = pd.json_normalize(
    data,
    record_path=['department', 'employees'],
    meta=['id', 'name', ['department', 'name'], ['department', 'location']],
    meta_prefix='employee_'
)

# Create DataFrame
df = pd.DataFrame(flattened_data)

# Display the DataFrame
print(df)
