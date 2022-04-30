from modelRequest import *
import requests

sketchFab = modelRequest()
carModel = sketchFab.requestModel('car')

with open('/Users/JJ/Downloads/carModel.zip', 'wb') as f:
    f.write(carModel.content)
