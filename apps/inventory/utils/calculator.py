from django.conf import settings


def calculate_weight_and_bars(chemical=None, chemical_weight=None, soap_bars=None):
    """
    Calculate the weight of a chemical and the number of soap bars that can be made from it.
    Args:
        chemical (str): The chemical to calculate.
        chemical_weight (float): The weight of the chemical in grams.
        soap_bars (int): The number of soap bars to calculate.
    Returns:
        dict: A dictionary containing the weights of the chemicals and the number of soap bars.
    """

    # weight of a single soap bar in grams
    required_weights = settings.CHEMICAL_WEIGHTS

    # Calculate weights if number of soap bars is given
    if soap_bars is not None:
        weights = {
            chem: required_weights[chem] * soap_bars for chem in required_weights
        }
        return {"weights": weights, "soap_bars": int(soap_bars)}

    # Calculate number of soap bars if chemical and weight is given
    if chemical and chemical_weight:
        soap_bars = chemical_weight / required_weights[chemical]
        weights = {
            chem: required_weights[chem] * soap_bars for chem in required_weights
        }
        return {"weights": weights, "soap_bars": int(soap_bars)}


if __name__ == "__main__":
    print(calculate_weight_and_bars(chemical="palm_starling", chemical_weight=44200))
