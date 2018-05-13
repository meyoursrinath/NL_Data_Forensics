'''
A python script to parse through an input html file and extract selected data from it
'''

# Importing required libraries
from bs4 import BeautifulSoup
import os


class HTMLParser:
    def __init__(self, file_name):
        self.soup = None
        self.file_name = file_name
        with open(file_name, "rb") as inp:
            self.soup = BeautifulSoup(inp, "lxml")

    # Extraction function
    def extract_elements(self):
        os.system("clear")
        print "\nElements of", self.file_name, "are\n"
        print "Title :",
        print self.soup.title.string
        print "Header :",
        print self.soup.h1.string
        print "Paragraph :",
        print self.soup.p.string
        print


def main():
    parser = HTMLParser("index.html")
    parser.extract_elements()


if __name__ == '__main__':
    main()
