def hello() -> str:
    return "Hello from project-permed!"


def parse_quantity(quantity):
    """
    Parses quantity into structured components.
    Usefull to parse gp_scripts.
    """
    if not isinstance(quantity, str):
        return {"quantity": None, "unit": None, "details": None}

    # Extract numeric quantity
    quantity_match = re.search(r"(\d+(\.\d+)?)", quantity)
    numeric_quantity = float(quantity_match.group(1)) if quantity_match else None
    # If the numeric quantity is an integer (i.e., no decimal part), return it as an integer

    # Extract unit (e.g., tablet(s), millilitres, etc.)
    unit_match = re.search(
        r"(tablet|cap|ampoule|millilitre|ml|pack|vial|sachet|dose vial|suppository|prefilled syringe)",
        quantity,
        re.IGNORECASE,
    )
    unit = unit_match.group(0).lower() if unit_match else None

    # Extract details, which includes everything after the unit
    details_start_index = quantity.lower().find(unit) + len(unit) if unit else None
    details = quantity[details_start_index:].strip() if details_start_index else None

    return {"quantity": numeric_quantity, "unit": unit, "details": details}

def parse_to_number(value):
    """
    Parses a concentration string and returns a numeric representation.
    Handles cases like "30mg/5ml", "20mg/ml", and single numbers like "10 mg". 
    Usefull for parsing gp_scripts.
    """
    if value is None:  # Handle None values
        return None

    # Find all numeric parts
    numbers = re.findall(r"\d+(?:\.\d+)?", value)

    # Handle concentrations in the form "20mg/ml" or "30mg/5ml"
    if "/" in value:
        if len(numbers) >= 1:  # Ensure at least one number exists
            num = float(numbers[0])  # Numerator is the first number
            den = 1.0  # Default denominator is 1.0 (for cases like /ml)
            if len(numbers) > 1:
                den = float(numbers[1])  # Use the second number if present
            return num / den

    # Handle single numbers like "10 mg" or "20mg"
    elif numbers:
        return float(numbers[0])  # Use the first number
    return None  # Return None for non-parsable cases

def remove_duplicates(row):
    """ 
    Usefull removing duplicates in OMOP data.
    """
    # Identify unique indices in start_dates
    seen = set()
    unique_indices = [i for i, x in enumerate(row["start_dates"]) if not (x in seen or seen.add(x))]
    
    # Filter each list column based on unique indices
    filtered_row = {
        "start_dates": [row["start_dates"][i] for i in unique_indices],
        "end_dates": [row["end_dates"][i] for i in unique_indices],
        "exposure_counts": [row["exposure_counts"][i] for i in unique_indices],
        "gap_days": [row["gap_days"][i] for i in unique_indices],
    }
    return filtered_row

