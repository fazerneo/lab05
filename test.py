def unique_element_counter(lst):
    unique_elements = []
    
    for item in lst:
        # Convert item to string representation to handle different types uniformly
        item_str = str(item)
        
        # Check if item_str is already in unique_elements
        if item_str not in (str(elem) for elem in unique_elements):
            # Convert item back to its original type before appending to unique_elements
            if isinstance(item, int):
                unique_elements.append(int(item_str))
            elif isinstance(item, float):
                unique_elements.append(float(item_str))
            elif isinstance(item, bool):
                unique_elements.append(bool(item_str))
            else:
                # If not int, float, or bool, append the item directly (e.g., string)
                unique_elements.append(item)
    
    return len(unique_elements), unique_elements

# Example usage:
list_1 = [1, True, 0, False, "string", True]
count, unique_elements = unique_element_counter(list_1)

print(f"The number of unique elements in list_1 is: {count}")
print(f"Unique elements in list_1: {unique_elements}")
