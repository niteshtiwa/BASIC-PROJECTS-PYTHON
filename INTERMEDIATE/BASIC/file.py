# csv comma seprated value
import csv
# csv.reader 
# csv.writer
data = [
  [" name", "Age", "city"], 
  ["nitesh", '19', 'delhi']
]
with open('data.csv', mode ='w') as file:
  writer = csv.writer(file)
  writer.writerows(data)

with open('data.csv', mode = 'r') as file :
  reader = csv.reader(file)
  for row in reader : 
    print (row)
