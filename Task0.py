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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
FirstRecordOfTexts = texts[0]
print("First record of texts,",FirstRecordOfTexts[0],"texts",FirstRecordOfTexts[1],"at time",FirstRecordOfTexts[2])
#print("First record of texts, "+FirstRecordOfTexts[0]+" texts "+FirstRecordOfTexts[1]+" at time "+ FirstRecordOfTexts[2])

LastRecordOfCalls = calls[-1]
print("Last record of calls,",LastRecordOfCalls[0],"calls",LastRecordOfCalls[1],"at time",LastRecordOfCalls[2],", lasting",LastRecordOfCalls[3],"seconds")
#print("Last record of calls, "+LastRecordOfCalls[0]+" calls "+LastRecordOfCalls[1]+" at time "+LastRecordOfCalls[2]+", lasting "+LastRecordOfCalls[3]+" seconds")


