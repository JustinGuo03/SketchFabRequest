import json
import requests

class modelRequest:
    token_url = "https://sketchfab.com/oauth2/token/"
    search_url = "https://api.sketchfab.com/v3/search?type=models&q={noun}&downloadable=true&archives_flavours=false"
    model_url = "https://api.sketchfab.com/v3/models/{UID}/download"


    EMAIL_ADDRESS = "research@sethangell.com"
    PASSWORD = "Er_PdS?gKL7qBjM$xgh=x5Edm"

    client_id = "0TCY3fDzG4IdLZEwvwtuZgQA6vkxakraPFcDnljp"
    client_secret = "bBSwzvaFewbuWAgR3hflbs5JT9vTsTBlYXZmY47A4WxyByVHfivlF8uIu17Ax3MfiHjpba8Ub0qQQmYj39tEPOcNhlgSwcl99DiLkgML0bmw2lpvTsy6Uqlw85FKc98R"
  
    data = {'grant_type': 'password', 'username': EMAIL_ADDRESS, 'password': PASSWORD}

    noun = ""

    def __init__(self, noun = ""):
        self.noun = noun
    
    def requestModel(self, noun):
        self.noun = noun
        access_token_response = requests.post(self.token_url, data=self.data, verify=False, allow_redirects=False, auth=(self.client_id, self.client_secret))

        access_token = json.loads(access_token_response.text)['access_token']
        
        api_call_headers = {'Authorization': 'Bearer ' + access_token}
        search_response = requests.get(self.search_url.format(noun = self.noun), headers=api_call_headers, verify=False)
        uid = json.loads(search_response.text)['results'][0]['uid']

        model_request = requests.get(self.model_url.format(UID = uid), headers=api_call_headers, verify=False)
        gltf_url = json.loads(model_request.text)['gltf']['url']

        download_request = requests.get(gltf_url, verify=False)
        return download_request

    def requestModelURL(self, noun):
        self.noun = noun

        access_token_response = requests.post(self.token_url, data=self.data, verify=False, allow_redirects=False, auth=(self.client_id, self.client_secret))

        access_token = json.loads(access_token_response.text)['access_token']
        
        api_call_headers = {'Authorization': 'Bearer ' + access_token}
        search_response = requests.get(self.search_url.format(noun = self.noun), headers=api_call_headers, verify=False)
        uid = json.loads(search_response.text)['results'][0]['uid']

        model_request = requests.get(self.model_url.format(UID = uid), headers=api_call_headers, verify=False)
        gltf_url = json.loads(model_request.text)['gltf']['url']

        return gltf_url