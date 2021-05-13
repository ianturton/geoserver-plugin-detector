"""
A small python program to detect which GeoServer plugins are installed
"""
import glob
import sys
import os
import re


class detection:
    def __init__(self):
        self.community = {}
        self.extension = {}
        with open("plugins.txt", 'r') as file:
            for line in file:
                (type, name, jar) = line.split()
                if type == 'community':
                    self.community[jar] = name
                else:
                    self.extension[jar] = name

    def detect(self, directory):
        jars = glob.glob(directory+"/*.jar")
        print("Examining ", len(jars), " jars")
        for jar in jars:
            jar = os.path.basename(jar)
            jar = re.sub(r'-[\d.-]*\.jar$', '', jar)
            if jar in self.extension:
                print("found extension "+self.extension.get(jar))
            if jar in self.community:
                print("found community plugin "+self.community.get(jar))


def main():
    if len(sys.argv) < 2:
        print("Please provide the location of the ",
              "WEB-INF/lib directory of your GeoServer installation")
    else:
        detecter = detection()
        detecter.detect(sys.argv[1])


if __name__ == '__main__':
    main()
