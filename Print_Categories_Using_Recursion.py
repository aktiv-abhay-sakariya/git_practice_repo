def print_all_categories(categories, depth=0, final=None):
    """
    This function recursively traverses list of dict if "children" keys in
    every dictionary is not empty and add in final.

    Args:
        categories (list) : list of dict where each contain id, name, children
        default : depth (int) : initially 0 when recursion call then increase by 1
                  final (None) : initially None and add all categories name

    Returns:
        final (str) : string which are laddered string
    """
    if final is None:
        final = """"""
    for category in categories:
        final += '\t'*depth + '-' + category['name'] + '\n'
        if category['children']:
            final += print_all_categories(category['children'], depth + 1)
    return final


categories = [
            {"id": 1,
            "name": "Electronics",
            "children": [{
                        "id": 2,
                        "name": "Mobile",
                        "children": [{"id": 3,
                                    "name": "Samsung",
                                    "children": []},
                                    {"id": 4,
                                    "name": "Apple",
                                    "children": []}]},
                        {"id": 5,
                        "name": "Laptop",
                        "children": []}]},
            {"id": 6,
            "name": "Clothing",
            "children": [{"id": 7,
                        "name": "Men",
                        "children": [{"id": 12,
                                    "name": "Shirt",
                                    "children": []},
                                    {"id": 13,
                                    "name": "T-Shirt",
                                    "children": []}]},
                        {"id": 8,
                        "name": "Women",
                        "children": []}]},
            {"id": 9,
            "name": "Food",
            "children":[{"id": 10,
                        "name": "Veg",
                        "children": []},
                        {"id": 11,
                        "name": "Non-Veg",
                        "children": []}]}
            ]
print(print_all_categories(categories))
print(print_all_categories(categories))


