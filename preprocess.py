import json
#from nltk.tokenize import word_tokenize

with open("data") as json_file:
    json_data = json.load(json_file)

# PREPROCESS
#for profile in json_data:
    # now profile is a dictionary
#    for attribute, value in profile.iteritems():
#        print attribute + ": ", value # iterate through each item

print json.dumps(json_data, indent=4)

print"*********"
print json_data[0]['profile']
