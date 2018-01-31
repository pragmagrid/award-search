#!/usr/bin/python

import os.path
import sys
import csv

if len(sys.argv) < 2:
    sys.exit('Usage: %s csv-file-name' % sys.argv[0])

fin = sys.argv[1]
if not os.path.isfile(fin):
    sys.exit('ERROR: %s is not a file' % fin)

name,ext = os.path.splitext(fin)

if ext == '.csv':
    delimiter = ','
elif ext == '.txt':
    delimiter = '\t'
else:
    sys.exit('ERROR: %s must be .csv or .txt Excel format' % fin)

fout = name + '-edited' + ext

csvReader = csv.reader(open(fin,  'rU'), delimiter=delimiter, quotechar='"')
csvWriter = csv.writer(open(fout, 'wb'), delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

def writeAbstract(link, title, text):
    name = "abstracts/%s.html" % link
    f = open(name, 'w')
    f.write ("<html>\n<head>\n    <title>%s</title>\n</head>\n" % title)
    f.write ("<body>\n\n<h2>%s</h2>\n\n<p>" % title)
    f.write ("\n\n<h4>Award: %s</h4>\n\n<p>" % link)
    f.write (text)
    f.write ("</p>\n</body>\n</html>")
    f.close()

header=["AwardNumber","Title","NSFOrganization","Program(s)","StartDate","LastAmendmentDate","PrincipalInvestigator","State","Organization","AwardInstrument","ProgramManager","EndDate","AwardedAmountToDate","Co-PIName(s)","PIEmailAddress","OrganizationStreet","OrganizationCity","OrganizationState","OrganizationZip","OrganizationPhone","NSFDirectorate","ProgramElementCode(s)","ProgramReferenceCode(s)","ARRAAmount","Abstract"]

"""
0 AwardNumber
1 Title
2 NSFOrganization
3 Program(s)
4 StartDate
5 LastAmendmentDate
6 PrincipalInvestigator
7 State
8 Organization
9 AwardInstrument
10 ProgramManager
11 EndDate
12 AwardedAmountToDate
13 Co-PIName(s)
14 PIEmailAddress
15 OrganizationStreet
16 OrganizationCity
17 OrganizationState
18 OrganizationZip
19 OrganizationPhone
20 NSFDirectorate
21 ProgramElementCode(s)
22 ProgramReferenceCode(s)
23 ARRAAmount
24 Abstract
"""
rownum = 0
for row in csvReader:
    if "Fellowship" in row: 
        rownum += 1
        continue
    if rownum == 0:
        if row != header:
            print "Error in csv header, Check input file"
            sys.exit(0)
        newrow = ["Award<br>Number","Title","Program(s)","Start/<br>Amendment/<br>End date",
                  "PI (email)<br>Co-PI","State","Organization<br>Address","Award<br>Instrument","Awarded<br>$ to date",
                  "Program<br>Manager","NFS<br>Organization/<br>NSF Directorate"]
        csvWriter.writerow(newrow)
        rownum += 1
        continue

    newrow = row[0:2] # element 0:1, AwardNumber, Title
    newrow.append ( row[3] ) # element 2, Program(s)
    newrow.append ( "%s<br>%s<br>%s" % (row[4], row[5], row[11])) # element 3, dates
    newrow.append ( "%s (%s)<br>%s" % (row[6], row[14],row[13])) # element 4, PrincipalInvestigator, Co-PI, email
    newrow.append ( row[7] ) # element 5, state
    newrow.append ( "%s<br>%s<br>%s, %s %s<br>Ph: %s" % (row[8],row[15],row[16],row[17],row[18],row[19])) # element 6, organization and address
    newrow.append ( row[9] ) # element 7, AwardInstrument
    newrow.append ( row[12] ) # element 8, AwardedAmountToDate
    newrow.append ( row[10] ) # element 9, ProgramManager
    newrow.append ( "%s / %s" % ( row[2],row[20] )) # element 10, NSFOrganization

    writeAbstract(row[0], row[1], row[24])

    csvWriter.writerow(newrow)
    rownum += 1

sys.exit(0)

