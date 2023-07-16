#getResults.py
#=============
#
#Iterates through a list of domains and collects JSON formatted
# report from OSINT discovery service API call with curl command
# Lost Rabbit Labs' WisQuas Digital Footprint Discovery and Inventory
#
# EXAMPLE: python getResults.py
#
import os                               # this program executes commands at the OS level

api_key = os.environ["WQ_API_KEY"] # put your API Key here
input_file = 'lildomains.txt'           # list of domains you have previously scanned one per line

input_file = open('lildomains.txt', 'r')   
for line in input_file:
    prog = "curl -o output/" + line + "_report.json -H 'X-api-Key: " + api_key + "' -d 'query=" + line + "' https://wisquas.lostrabbitlabs.com/api/report"
    prog = prog.replace('\n','')        # take out the extra newlines in there
    #print(prog)
    res = os.system(prog)
