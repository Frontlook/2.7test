# encoding=utf8
import csv
import sys
from urllib import urlopen
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')

html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html,'lxml')
table = bsObj.findAll("table",{"class":"wikitable"})[0]
rows = table.findAll("tr")
csvFile = open("editors.csv", 'wt', buffering=1)
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()