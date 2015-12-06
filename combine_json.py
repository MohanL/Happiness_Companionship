import json
file_list = ["data1.json","data2.json","data3.json","data4.json","data5.json","data6.json","data7.json","data8.json","data9.json","data10.json"]
head = []
with open("all_data.json", "w") as outfile:
    for f in file_list:
        with open("data/"+f, 'rb') as infile:
            file_data = json.load(infile)
            head += file_data
    json.dump(head, outfile)

with open('all_data.json') as f:
    # load json objects to dictionaries
    jsons = map(json.loads, f)

result = list()
items_set = set()

for js in jsons:
    # only add unseen items (referring to 'title' as key)
    if not js['user_name'] in items_set:
        # mark as seen
        items_set.add(js['user_name'])
        # add to results
        result.append(js)

# write to new json file
with open('new_file.json' ,'w') as nf:
    json.dump(result, nf)

print result
