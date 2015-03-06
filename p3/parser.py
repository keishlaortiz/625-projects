from city import City
"""
Class to read a file that contains a list of cities with its coordinates (in degree) and store them
into a list of class City
"""
class Parser(object):

    def __init__(self,inputFile):
        self.file = inputFile

    def parseFile(self):

        cities = [City(line.split()[0], float(line.split()[1]), float(line.split()[2])) for line in open(self.file,'r')]

        return cities