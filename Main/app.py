import requests

request = requests.get("http://localhost:5000/app/getPlaybook")

if(request.status_code == 200):
    from localPlaybook import *

    playbook_req = playbook()

    print(playbook_req)

else:
    print("error")