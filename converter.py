def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "invalid input"


def inches_from(centims):
    """Convert centimeters to inches"""
    try:
        inches = float(centims) / 2.54
        inches = round(inches, 3)  # Round to three decimal places
        return str(inches)
    except ValueError:
        return "invalid input"
