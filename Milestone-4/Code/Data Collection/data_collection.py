import requests
import json

num=0
airports=['ATL','DFW','DEN','ORD','LAX','JFK','LAS','MCO','MIA','CLT','SEA','PHX','EWR','SFO','IAH','BOS','FLL','MSP','LGA','DTW','PHL','SLC','DCA','SAN','BWI','TPA','AUS','IAD','BNA','MDW','HNL']
for i in airports:
        url='https://airlabs.co/api/v9/schedules?dep_iata='+i+'&limit=20&api_key=30c7a1b7-2105-4f3f-bc59-657501af30df'


        resp = requests.get(url=url)
        myjson = resp.json()
        json_string=json.dumps(myjson)
        print(json_string)
        print(i)
        num+=1
        
        with open(str(num)+'output.json','w') as json_file:
                json_file.write(json_string)



