def update_dictionary(a_dictionary, key, value):
    newdict = {key:value}
    a_dictionary.update(newdict)
    return a_dictionary

a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
print(update_dictionary(a_dictionary,'city',"Addis Ababa"))