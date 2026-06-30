"""
Data validation functions.
"""


# Example function to implement:
def validate_isbn(isbn):
    """Validate ISBN-13 format."""

    isbn = str(isbn).strip().replace('-','')

    if not isbn.isdigit():
        return False

    if len(isbn) != 13:
        return False

    # Add check digit code here

    return True
