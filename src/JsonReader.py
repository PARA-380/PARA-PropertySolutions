import json

class jsonwriter:

    def __init__(self,obj):
        self._data : dict = obj


    def write(self):
        jsonObj = json.dumps(self._data, indent=4)

        #writing to sample .json
        with open("data/sample.json", "w") as outfile:
            outfile.write(jsonObj)


    def read(self):
        pass


#example : dict = {"Properties":{"property1":{"Tenant":{"name" : "Ridham Patel"}},"property2":{"Tenant":{}},"property3":{"Tenant":{}}}}
jsonwriter(example).write()