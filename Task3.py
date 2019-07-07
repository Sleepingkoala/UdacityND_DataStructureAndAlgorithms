"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.
"""
numbers_called = set()
area_codes = set()
mobile_preflixes = set()
telemarketers = set()

for call in calls:
    if call[0][0:5]== "(080)":
        if call[1][0:2]== "(0":
            area_codes.add(call[1][0:call[1].find(")")+1])
        elif call[1][0] == "7" or call[1][0] == "8" or call[1][0] == "9":
            mobile_preflixes.add(call[1][0:4])
      
    
numbers_called = list(area_codes) + list(mobile_preflixes)
numbers_called.sort()

print("The numbers called by people in Bangalore have codes:\n")
for number in numbers_called:
    print(number)

"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

fixed_lines_count = 0
calls_count = 0

for call in calls:
    if call[0][0:5] == "(080)":
        calls_count +=1
        if call[1][0:5] == "(080)":
            fixed_lines_count += 1
            
percentage = (fixed_lines_count/calls_count)*100
print(str("%.2f"% percentage),"percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")



