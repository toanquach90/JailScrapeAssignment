import urllib2, csv 
#import Python’s built-in csv module at the top of the file
from bs4 import BeautifulSoup 
#import the BeautifulSoul parsing HTML

outfile = open('jaildata.csv', 'w')
writer = csv.writer(outfile) 
#writes a CSV ﬁle including its header and data.

url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500' 
#link to the database on the website that we would like to scrap. Adjust the URL variables to get all the data by passing a new max_rows value at 500
html = urllib2.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser") 
#To parse a document by passing it into the BeautifulSoup constructor. BeautifulSoup will use an HTML parser.

tbody = soup.find('tbody', {'class': 'stripe'})
#direct command to instruct BeautifulSoup to extract only the table we need.

rows = tbody.find_all('tr')
 #convert the rows in the table into a list

for row in rows:
 #a table with many rows. Each row is about an inmate

    cells = row.find_all('td')
#loop through each cell in each row. Cells are created in HTML by <td> tag. Add each cell in a row to a Python list.

    data = []
    for cell in cells:
        #loop inside a loop
        data.append(cell.text.encode('utf-8'))
        #Python lists are combined into one big list.

    writer.writerow(data)
#Write the headers at the first row of the final list into the cvs file.