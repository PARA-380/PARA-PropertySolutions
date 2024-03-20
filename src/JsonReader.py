import json

class jsonwriter:

    def write(self):
        jsonObj = json.dumps(self, indent=4)
        print(jsonObj)

        #writing to sample .json
        with open("data/sample.json", "w") as outfile:
            outfile.write(jsonObj)
        outfile.close()


    def read(self):
        pass

