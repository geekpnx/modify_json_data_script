import json
import random
import string

# Function to generate a shorter id_tag based on store and name
def generate_id_tag(store, name):
    # Take the first 3 characters from the store and name, remove spaces, and add random suffix
    store_part = ''.join(store.split())[:3].lower()  # First 3 chars from store
    name_part = ''.join(name.split())[:3].lower()  # First 3 chars from name
    random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))  # Random 4 characters
    return f"{store_part}_{name_part}_{random_suffix}"

# Function to add "store" key and "id_tag" key
def add_fields_to_data(data):
    for item in data:
        # Add store before name
        new_item = {"store": "Aldi Süd"}
        new_item.update(item)
        item.clear()
        item.update(new_item)

        # Generate id_tag from store and name, then add it after link
        id_tag = generate_id_tag(item['store'], item['name'])
        item['id_tag'] = id_tag  # Add id_tag after link field

# Load JSON data from a file
with open('aldi_sued_products.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Modify the data by adding "store" and "id_tag"
add_fields_to_data(data)

# Save the modified data back to a file
with open('aldi_sued_products_modified.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("Data updated and saved to aldi_sued_products_modified.json.")
