#!/usr/bin/env python

"""
Convert CSV file to libsvm format. Works only with numeric variables.
Put -1 as label index (argv[3]) if there are no labels in your file.
Expecting no headers. If present, headers can be skipped with argv[4] == 1.

"""


import csv


def construct_line( label, line ):
    #cnt = 0:
    new_line = []
    #print(line)
    #print(label)
    if float( label ) == 0.0:
        label = "0"
    new_line.append( label )

    for i, item in enumerate( line ):
        if item == '' or float( item ) == 0.0:
            continue
        new_item = "%s:%s" % ( i + 1, item )
        new_line.append( new_item )
    new_line = " ".join( new_line )
    new_line += "\n"
    return new_line

# ---


input_file = "./features/final.csv"
output_file="./features/final.train"


label_index = 0 # set 0 for labeling features / set -1 for testing


skip_headers = 0

i = open( input_file, 'r' )
o = open( output_file, 'w' )

reader = csv.reader( i )

if skip_headers:
	headers = reader.next()

for line in reader:

    if label_index == -1:
        
        
        label = '1'
    else:
        label = line.pop( label_index )

    new_line = construct_line( label, line )
    #print(new_line)
    o.write( new_line )

i.close()
o.close()

