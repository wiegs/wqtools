#processLRL.py
#=============
#
#process the output from Lost Rabbit Labs' WisQuas JSON data into CSV
#
#Args: one(1): the input filename
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
theFortiguard = ""                          # variable home for Fortiguard site rating
theSiteadvisor = ""                         # variable home for Siteadvisor site rating
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
    if x == "scanDoc":
        json_result = json_var[x]
        try:
            theIP = json_result["ipaddr"]
        except:
            theIP = ""
        try:
            theDNS = json_result["whois"]["nameservers"]
        except:
            theDNS = ""    
        theDNS = str(theDNS)
        try:
            theASN = json_result["ipwhois"]["asn"]    
        except:
            theASN = ""
        try:
            theASN = "ASN " + theASN + " " + json_result["ipwhois"]["asn_description"]
        except:
            theASN = theASN + ""       
        try:
            theRegistrar = json_result["whois"]["registrar"]
        except:
            theRegistrar = ""
        try:
            theCreated = json_result["whois"]["created_date"]
        except:
            theCreated = ""
        try:    
            theExpires = json_result["whois"]["expired_date"]
        except:
            theExpires = ""
        try:
            theSiteadvisor = json_result["blacklist"]["siteadvisor"]
        except:
            theSiteadvisor = ""
        try:
            theFQDNs = json_result["subdomains"]
        except:
            theFQDNs = ""
        theFQDNs = str(theFQDNs)

with open (csv_output, "a") as outputfile:  # write a new line to the output file
    outputfile.write(theDomain + ";" + theIP +";" + theDNS +";" + theASN +";" + theRegistrar +";" + theCreated +";" + theExpires +";" + theSiteadvisor +";" + theFQDNs +"\n")
outputfile.close()                          # close the output file

print(sys.argv[1] + " processed OK!")       # give the OK sign

