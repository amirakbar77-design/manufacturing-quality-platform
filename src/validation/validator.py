import numpy as np

rules = {
    "temperature": {
        "min": 250,
        "max": 400
    },
    "rotational_speed": {
        "min": 500,
        "max": 3000
    }
}


def validate_record(record):
    errors = []

    for field, rule in rules.items():

        # Check 1: Does the field exist?
        if field not in record:
            errors.append(f"{field} field is missing")
            continue

        # Get the value
        value = record[field]

        # Check 2: Is it a number?
        if not isinstance(value, (int, float, np.integer, np.floating)):
            errors.append(f"{field} must be a number")
            continue

        # Check 3: Is it within the valid range?
        if value < rule["min"] or value > rule["max"]:
            errors.append(f"{field} is outside the valid range")

    return errors
