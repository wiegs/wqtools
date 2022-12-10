#processJSON.py
#==============
#
#Takes the saved output from Lost Rabbit Labs' WisQuas Digital Footprint Discovery and Inventory
# and puts it into a CSV file to create a spreadsheet to share with your webmaster or marketing
#
# INPUT: .json report file
# OUTPUT: saves a row to the CSV file and gives the OK sign
#
# ARGUMENTS: 1 - the input filename
#
# note CSV file uses semicolon ";" separator
#      if you want a header run headerRow.py
#
# EXAMPLE: python processJSON.py report.json
#
import sys                              
import os
import json                             
import pprint   

csv_output = "processJSON-RESULTS.csv"      # initialize variables
theIP = ""                              
theDNS = ""
theASN = ""
theRegistrar = ""
theCreated = ""
theExpires = ""
theFQDNs = ""
JSONfilename = sys.argv[1].strip()          # strip out stuff like whitespace probably
JSONfilename = JSONfilename.strip('"')      # strip out doublequotes for some reason
with open(JSONfilename) as f:               # load the file
    json_var = json.load(f)                 # into the variable
keys = json_var.keys()                      # keys is a list of the 4 top keys in the JSON data
# go get Domain variable theDomain
for x in keys:                              # loop through the keys array: query, results, scanDoc, others
    if x == "query":                        # the "query" key contains the domain name
        theDomain = json_var[x]             # we load the domain into a variable to use at the end for the output
# go get the rest from results 
for x in keys:
    if x == "results":
        json_result = json_var[x]
        try:
            theIP = json_result[0]["topScan"]["scan"]["ipaddr"]
        except:
            theIP = ""
        try:
            theDNS = json_result[0]["topScan"]["scan"]["whois"]["nameservers"]
        except:
            theDNS = ""    
        theDNS = str(theDNS)
        try:
            theASN = json_result[0]["topScan"]["scan"]["ip"]["asn"]    
        except:
            theASN = ""
        try:
            theASN = theASN + " " + json_result[0]["topScan"]["scan"]["ip"]["asn_description"]
        except:
            theASN = theASN + ""       
        try:
            theRegistrar = json_result[0]["topScan"]["scan"]["whois"]["registrar"]
        except:
            theRegistrar = ""
        try:
            theCreated = json_result[0]["topScan"]["scan"]["whois"]["created_date"]
        except:
            theCreated = ""
        try:    
            theExpires = json_result[0]["topScan"]["scan"]["whois"]["expired_date"]
        except:
            theExpires = ""
        try:
            theFQDNs = json_result[0]["topScan"]["scan"]["subdomains"]
        except:
            theFQDNs = ""
        theFQDNs = str(theFQDNs)

with open (csv_output, "a") as outputfile:  # write a new line to the output file
    outputfile.write(theDomain + ";" + theIP +";" + theDNS +";" + theASN +";" + theRegistrar +";" + theCreated +";" + theExpires +";" + theFQDNs +"\n")
outputfile.close()                          # close the output file

print(sys.argv[1] + " processed OK!")       # give the OK sign
