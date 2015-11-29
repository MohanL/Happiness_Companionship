import requests, json, sys

github_url = "https://api.about.me/api/v2/json/users/view/random"
key = "?client_id=cb12c2533a888bc5cc3f7dd5d0cb473a2c221f5d"
num_calls = "&profile_number=" + str(sys.argv[1])
data_file = open('data.txt', 'w')

try :
    r = requests.post(github_url+key+num_calls+"&extended=true")
except requests.exceptions.RequestException as e:
    print e
    sys.exit(1)

json_output = r.json()

#print r.json()['result']
if(json_output['status'] == 200):
    data_file.write(json.dumps(json_output['result'], indent=4))
else:
    print json_output['status']
data_file.close()
