#author: Palash Dusane (palashdusane@gmail.com)

import database as db
import webscraper as ws
import datetime as dt
import visualization as v
current_date= int(dt.date.today().strftime("%d%m%y"))

db.createtable_covid19India()
if(db.checkdate_covid19India()==False): #check if data is already inserted or not
    ws.getdata_India()

print("********************************************************************")
print("*                                                                  *")
print("*                 COVID-19 Information Tool- India                 *")
print("*                 [version 1.0 | Author:Palash Dusane]             *")
print("*                                                                  *")
print("********************************************************************\n")
print("Note: This tool scraps public data from https://www.mohfw.gov.in/")
print("Use command '?' or 'help' (shortkey:h) to get more information")
while(True):
    user_input = input(">>>")
    if(user_input=='?' or user_input=='help' or user_input=='h'):
        help_msg = '''
COVID-19 Information Tool - Help
info  (shortkey: i):   get state-wise COVID-19 spread tabular information.
graph (shortkey: g):   get current date's bar graph consisting of ative,cured/discharged,death cases
pie   (shortkey: p):   get current date's pie chart consisting of active,cured/discharged,death cases
bar5+ (shortkey: b5+): get top five most affected states/ut bar graph
bar5- (shortkey: b5-): get top five least affected states/ut bar graph
comp  (shortkey: c):   get comparision bargraph of yesterday and today*
quit  (shortkey: q):   exit from tool
*these commands will work only if database is properly updated
'''
        print(help_msg)
    elif(user_input=='info' or user_input=='i'):
        v.table_covid19India()
    elif(user_input=='graph' or user_input=='g'):
        v.bargraph_covid19India()
    elif(user_input=='pie' or user_input=='p'):
        v.piechart_covid19India()
    elif(user_input=='bar5+' or user_input=='b5+'):
        v.bargraph_topfive()
    elif(user_input=='bar5-' or user_input=='b5-'):
        v.bargraph_lastfive()
    elif(user_input=='comp' or user_input=='c'):
        v.bargraph_compare()
    elif(user_input=='quit' or user_input=='q'):
        break
    else:
        print("Invalid command (try '?' or 'help' (shortkey:h))")
        

    
