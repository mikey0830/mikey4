def currency_converter(amount, from_currency, to_currency):
    
    conversion_rate = {
        'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
        'INR': {'CNY': 0.09, 'PHP': 8.69, 'GBP': 0.01},
        'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
        'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45}
    }

   
    if amount < 0:
        return 0.0

    
    if from_currency in conversion_rate and to_currency in conversion_rate[from_currency]:
        converted_amount = amount * conversion_rate[from_currency][to_currency]
        return round(converted_amount, 2)
    else:
        
        return None

