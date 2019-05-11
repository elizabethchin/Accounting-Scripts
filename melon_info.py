"""Print out all the melons in our inventory."""

from melons import melon_names


def print_melon(melon_names):
    """Print each melon with corresponding attribute information."""
    for melon, attributes in melon_names.items():
        print(melon)
        for attribute, value in attributes.items():
                print(f"{attribute}: {value}")
print_melon(melon_names)

