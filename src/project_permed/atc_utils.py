def get_atc_level_n(atc_codes_tuple, n):
    """
    Get ATC codes at level n from a tuple of ATC codes
    Args:
        atc_codes_tuple: tuple of strings, e.g. ("C07AB04",)
        n: int, ATC level (1-5)
    Returns:
        set of ATC codes at level n
    """
    if not atc_codes_tuple:
        return set()

    slice_lengths = [None, 1, 3, 4, 5, 7]
    slice_length = slice_lengths[n]
    return {code[:slice_length] for code in atc_codes_tuple}


def share_atc_level(drug_a_id, drug_b_id, n, drug_dict):
    """
    Check if two drugs share any ATC codes at level n
    Args:
        drug_a_id: int, first drug concept ID
        drug_b_id: int, second drug concept ID
        n: int, ATC level (1-5)
        drug_dict: dictionary mapping drug IDs to (atc_codes_tuple, drug_name)
    Returns:
        bool, True if drugs share any ATC codes at level n
    """
    atc_a = get_atc_level_n(drug_dict.get(drug_a_id, ((), ""))[0], n)
    atc_b = get_atc_level_n(drug_dict.get(drug_b_id, ((), ""))[0], n)
    return bool(atc_a & atc_b)
