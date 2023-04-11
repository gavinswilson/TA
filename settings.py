import yaml, io

class yaml_data():
    filename = None
    data_loaded = None

    def __init__(self):
        print ("did stuff")

    def readFile(self):
        with open(self.filename, 'r') as stream:
            self.data_loaded = yaml.safe_load(stream)
    
    def setFilename(self, filename):
        self.filename = filename

    def printData(self):
        print(self.filename)
        print(self.data_loaded)
        print(self.data_loaded['a list'])

    def changeData(self, section, data):
        self.data_loaded[section] = data
    
    def saveSettings(self):
        with io.open(self.filename, 'w', encoding='utf8') as outfile:
            yaml.dump(self.data_loaded, outfile, default_flow_style=False, allow_unicode=True)