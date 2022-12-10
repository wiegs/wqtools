# write the output file header row, close it after
with open (csv_output, "a") as outputfile:   
    outputfile.write("Domain;IP;DNS;ASN;Registrar;Created;Expires;FQDNs\n")
outputfile.close()
