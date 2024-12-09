def sort_dicts_by_key(dict_list, key):
    try:
        return sorted(dict_list, key=lambda x: x[key])
    except KeyError:
        raise ValueError(f"Key '{key}' not found in one or more dictionaries.")

# Example usage
data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 22}, {"name": "Charlie", "age": 30}]
key = "age"
sorted_data = sort_dicts_by_key(data, key)
print("Sorted Data:", sorted_data)
