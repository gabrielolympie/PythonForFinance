def format_currency(amount, currency="$"):
    """Formats a number as a currency string."""
    result = f'{currency}{amount:.2f}'
    return result


def calculate_profit_margin(revenue, cost):
    if revenue == 0:
        print('Warning, profit margin cannot be computed with a zero revenue, falling back to zero')
        return 0
    
    result = ((revenue - cost) / revenue) ** 100
    return result