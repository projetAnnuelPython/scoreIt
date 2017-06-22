import json


class JsonParser(object):
    def parsefile(self, filename):
        with open(filename) as data_file:
            return json.load(data_file)
