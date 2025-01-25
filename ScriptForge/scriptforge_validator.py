import os
import esprima
import json
from jsonschema import validate, ValidationError
from scriptforge_schema import scriptforge_schema

# Validate JavaScript/TypeScript syntax
def validate_script_syntax(file_path):
    try:
        with open(file_path, 'r') as file:
            code = file.read()
        esprima.parseScript(code)
        print(f"✅ Syntax is valid: {file_path}")
    except Exception as e:
        print(f"❌ Syntax error in {file_path}: {e}")

# Validate JSON files against the schema
def validate_json(file_path, schema):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        validate(instance=data, schema=schema)
        print(f"✅ JSON is valid: {file_path}")
    except ValidationError as e:
        print(f"❌ Validation error in {file_path}: {e}")
    except Exception as e:
        print(f"❌ Error loading {file_path}: {e}")

# Validate all files in the given directory
def validate_files(directory, schema):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith(".js") or file.endswith(".ts"):
                validate_script_syntax(file_path)
            elif file.endswith(".json"):
                validate_json(file_path, schema)

# Main execution
if __name__ == "__main__":
    # Path to your scripts folder
    project_directory = "scripts"  # Replace with your scripts folder name
    validate_files(project_directory, scriptforge_schema)