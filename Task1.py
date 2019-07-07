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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
#the different telephone numbers should include sending(incoming) and recieving(answering) numbers in both texts.txt and calls.txt

texts_sending = set()
texts_recieving = set()
for text in texts:
    texts_sending.add(text[0])
    texts_recieving.add(text[1])

calls_sending = set()
calls_recieving = set()
for call in calls:
    calls_sending.add(call[0])
    calls_recieving.add(call[1])
    
different_telephones = set()
different_telephones = texts_sending|texts_recieving|calls_sending|calls_recieving
print("There are",len(different_telephones),"different telephone numbers in the records.")





    

