#author: Palash Dusane (palashdusane@gmail.com)

from bs4 import BeautifulSoup #parsing HTML and XML documents.
from requests import get  #allows you to send HTTP requests using Python
import database as db #import functions from database.py file


def getdata_India():
    '''this function performs web scraping from gov website'''
    url = 'https://www.mohfw.gov.in/' #data source
    page = get(url)
    html_soup = BeautifulSoup(page.content,'html.parser')

    table = html_soup.find(class_= 'table table-striped')
    table_body= table.find('tbody')
    table_rows= table_body('tr')

    db.createtable_covid19India()
    count=0
    for row in table_rows:
        count +=1
        if(count>34):
            break
        data = row('td')
        db.insert_covid19India(data[1].get_text(),data[2].get_text(),data[3].get_text(),data[4].get_text())
        
    db.database_commit()
    db.close_database()

