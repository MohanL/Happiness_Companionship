import json
with open('all_data.json') as f:
    # load json objects to dictionaries
    jsons = map(json.loads, f)

result = list()
items_set = set()

for js in jsons[0]:
    # only add unseen items (referring to 'title' as key)
    if not js['user_name'] in items_set:
        # mark as seen
        items_set.add(js['user_name'])
        # add to results
        result.append(js)

print len(result)

# write to new json file
with open('unduped.json' ,'w') as nf:
    json.dump(result, nf)

#print result
