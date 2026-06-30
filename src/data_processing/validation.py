"""
Data validation functions.
"""


# Example function to implement:
def validate_isbn(isbn):
    """Validate ISBN-13 format."""

    isbn = str(isbn).strip().replace("-", "")

    if not isbn.isdigit():
        return False

    if len(isbn) != 13:
        return False

    # Add check digit code here
    total = 0
    for i in range(12):
        digit = int(isbn[i])
        # get the remainder after division
        if i % 2 == 0:
            total += digit
        else:
            total += digit * 3
    check_digit = (10 - (total % 10)) % 10

    if check_digit != int(isbn[12]):
        return False

    return True
