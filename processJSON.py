#processJSON.py
#=============
#
#process the output from Lost Rabbit Labs' WisQuas JSON data into CSV
#
#Args: one(1): the input filename
#
import sys
import json

CSV_OUTPUT = "processJSON-RESULTS.csv"      # initialize variables
THE_IP = ""
THE_DNS = ""
THE_ASN = ""
THE_REGISTRAR = ""
THE_CREATED = ""
THE_EXPIRES = ""
THE_FQDNS = ""
THE_DATALASTUPDATED = ""                     # data was last updated
THS_SITEADVISOR = ""                         # variable home for Siteadvisor site rating
JSON_FILENAME = sys.argv[1].strip()          # strip out stuff like whitespace probably
JSON_FILENAME = JSON_FILENAME.strip('"')      # strip out doublequotes for some reason
with open(JSON_FILENAME, encoding="utf8") as f:  # load the file
    json_var = json.load(f)                     # into the variable
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
            THE_IP = json_result["ipaddr"]
        except:
            THE_IP = ""
        try:
            THE_DNS = json_result["whois"]["nameservers"]
        except:
            THE_DNS = ""
        THE_DNS = str(THE_DNS)
        try:
            THE_ASN = json_result["ipwhois"]["asn"]
        except:
            THE_ASN = ""
        try:
            THE_ASN = "ASN " + THE_ASN + " " + json_result["ipwhois"]["asn_description"]
        except:
            THE_ASN = THE_ASN + ""
        try:
            THE_REGISTRAR = json_result["whois"]["registrar"]
        except:
            THE_REGISTRAR = ""
        try:
            THE_CREATED = json_result["whois"]["created_date"]
        except:
            THE_CREATED = ""
        try:
            THE_EXPIRES = json_result["whois"]["expired_date"]
        except:
            THE_EXPIRES = ""
        try:
            THS_SITEADVISOR = json_result["blacklist"]["siteadvisor"]
        except:
            THS_SITEADVISOR = ""
        try:
            THE_FQDNS = json_result["subdomains"]
        except:
            THE_FQDNS = ""
        try:
            THE_DATALASTUPDATED = json_result["updatedAt"]
        except:
            THE_DATALASTUPDATED = ""
        THE_FQDNS = str(THE_FQDNS)

with open (CSV_OUTPUT, "a") as outputfile:  # write a new line to the output file
    outputfile.write(theDomain + ";" + \
                    THE_IP +";" + \
                    THE_DNS +";" + \
                    THE_ASN +";" + \
                    THE_REGISTRAR +";" + \
                    THE_CREATED +";" + \
                    THE_EXPIRES +";" + \
                    THS_SITEADVISOR +";" + \
                    THE_FQDNS + ";" + \
                    THE_DATALASTUPDATED + "\n")
outputfile.close()                          # close the output file

print(sys.argv[1] + " processed OK!")       # give the OK sign
