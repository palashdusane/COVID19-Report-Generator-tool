#author: Palash Dusane (palashdusane@gmail.com)

import datetime as dt
import dataprocessing as dp
import matplotlib.pyplot as plt

current_date= int(dt.date.today().strftime("%d%m%y"))
previous_date= int((dt.date.today() - dt.timedelta(days = 1)).strftime("%d%m%y"))

def table_covid19India():
    '''get records in dataframe for current date'''
    df = dp.get_dataframe(current_date)
    print(df)
    
    
def piechart_covid19India():
    '''get current date's piechart consisting of Active Cases,Cured/Discharged Cases,Deaths'''
    df = dp.get_dataframe(current_date)
    data_lst =dp.sum_covid19india(df)
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.axis('equal') # ensures a circle
    labels = ['Active Cases','Cured/Discharged Cases','Deaths']
    ax.pie(data_lst,labels=labels,colors = ['orange', 'green', 'red'],autopct='%1.2f%%')
    #plt.savefig('piechart.png',bbox_inches='tight')
    plt.show()
    

def bargraph_covid19India():  
    '''get current date's bargraph consisting of Active Cases,Cured/Discharged Cases,Deaths'''
    df = dp.get_dataframe(current_date)
    data_lst =dp.sum_covid19india(df)
    fig = plt.figure()
    ax = fig.add_axes([0,0,0.7,1])
    labels = ['Active','Cured/Discharged','Deaths']
    ax.bar(labels,data_lst)
    #plt.savefig('bargraph.png',bbox_inches='tight')
    plt.show()
    
def bargraph_compare():
    '''get comparision bargraph of yesterday and today'''
    yesterday = str(dt.date.today().strftime('%d-%m-%y'))
    today = str((dt.date.today()-dt.timedelta(1)).strftime('%d-%m-%y'))
    df1 = dp.get_dataframe(current_date)
    df2 = dp.get_dataframe(previous_date)
    data_lst1 =dp.sum_covid19india(df1)
    data_lst2 =dp.sum_covid19india(df2)
    merge_lst = [data_lst2[0],data_lst1[0],data_lst2[1],data_lst1[1],data_lst2[2],data_lst1[2]]
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    labels = [today+'\n(active)',yesterday+'\n(active)',today+'\n(cured)',yesterday+'\n(cured)',today+'\n(deaths)',yesterday+'\n(deaths)']
    ax.bar(labels,merge_lst)
    plt.show()

def bargraph_topfive():
    '''get top five affected states/ut'''
    df = dp.top5_covid19india('most',current_date)
    print(df)
    #labels = [df.iloc[0]['State/UT'],df.iloc[1]['State/UT'],df.iloc[2]['State/UT'],df.iloc[3]['State/UT'],df.iloc[4]['State/UT']]
    df.plot.bar() 
    plt.show() 
    
def bargraph_lastfive():
    '''get five least affected states/ut'''
    df = dp.top5_covid19india('least',current_date)
    print(df)
    #labels = [df.iloc[0]['State/UT'],df.iloc[1]['State/UT'],df.iloc[2]['State/UT'],df.iloc[3]['State/UT'],df.iloc[4]['State/UT']]
    df.plot.bar() 
    plt.show() 

