def calculate_percentage_return(start_price, end_price):
    """Calculates the percentage return given a start and end price."""
    if start_price == 0:
        return 0.0
    absolute_return = end_price - start_price
    return (absolute_return / start_price) * 100

def calculate_future_value(principal, rate, years, compounding_periods=1):
    """Calculates the future value of an investment."""
    fv = principal * (1 + rate / compounding_periods) ** (compounding_periods * years)
    return fv

def rule_of_72(interest_rate):
    """Estimates years to double an investment using the Rule of 72."""
    return 72 / (interest_rate * 100)