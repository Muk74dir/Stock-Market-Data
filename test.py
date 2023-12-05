import json
from Data.models import JSONModel

with open('Data/load_json_data.py') as f:
    data = json.load(f)
    
print(data)