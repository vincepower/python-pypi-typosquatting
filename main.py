import requests
import json
import jellyfish

# List of top packages
top_url = requests.get("https://hugovk.github.io/top-pypi-packages/top-pypi-packages-30-days.min.json")
top_data = json.loads(top_url.text)

# How many packages in the list
print("# Records in top packages: ", len(top_data['rows']))

# List of all packages
complete_list_url = requests.get("https://raw.githubusercontent.com/vincepower/python-pypi-package-list/main/pypi-packages.json")
complete_list_data = json.loads(complete_list_url.text)

# How many packages in the list
print("# Records in all packages: ", len(complete_list_data['packages']))

# How many times to loop (JSON starts counting at zero)
counter = 0
max_counter = 9

# What Levenshtein distance are we looking for
levenshtein_number = 3

# Preparing the output
print("# The following potential names have been found")
print("# which could be typosquatting the top", max_counter+1, "packages")
print("---")

# Entering the loop for the top packages
while counter <= max_counter:
    matching_list = []

    # Getting the name of the next package from
      # the entire list to match against
    for comparing_to in complete_list_data['packages']:

        # if the name is within the set number of changes
        # from the original then this will record it
        if jellyfish.levenshtein_distance(top_data['rows'][counter]['project'], comparing_to) < levenshtein_number:
            matching_list.append(comparing_to)

    # Displaying the results of the matching
    print(top_data['rows'][counter]['project'], matching_list, sep=": ")

    # On to the next record in the top data
    counter += 1
