import nltk
nltk.download('punkt')

import sys
import json
from nltk.tokenize import word_tokenize
from optparse import OptionParser

def preprocess():
    return 0

def main():
#    parser = OptionParser()
#    parser.add_option("-f", "--file", dest="filename",
#                      help="write report to FILE", metavar="FILE")
#    parser.add_option("-q", "--quiet",
#                      action="store_false", dest="verbose", default=True,
#                      help="don't print status messages to stdout")
#    (options, args) = parser.parse_args()


    with open("data.txt") as json_file:
        json_data = json.load(json_file)
        print json.dumps(json_data, indent=4)
        print "******"
        for profile in json_data:
            bio = profile['bio']
            tokens = word_tokenize(bio.encode('utf-8'))
            print tokens
    return 0

if __name__ == "__main__":
        main()

