#author: Palash Dusane (palashdusane@gmail.com)

import database as db
import pandas as pd

def get_dataframe(current_date):
    '''get records of current_date from database'''
    data = db.getdata_covid19India(current_date)
    df = pd.DataFrame(data, columns = ['State/UT','Confirmed Cases','Cured Cases','Deaths'])
    df.index +=1
    return df
'''    
def population_affected():
    population_india = 1378455853 #current indian population [source: https://www.worldometers.info/world-population/india-population/]
    
    df = get_dataframe(dt.date.today())
    total_confirmed = df['Confirmed Cases'].sum()
    return [population_india,total_confirmed]
    '''

def sum_covid19india(df):
    '''calculates sum of cured cases,deaths and confirmed cases'''
    cured_cases = df['Cured Cases'].sum()
    death_cases = df['Deaths'].sum()
    active_cases = df['Confirmed Cases'].sum()-df['Cured Cases'].sum()-df['Deaths'].sum()
    return [active_cases,cured_cases,death_cases]

def top5_covid19india(order,current_date):
    ''' get top 5 or last 5 affected states/ut'''
    if(order == 'most'):
        data = db.gettop5_covid19India(current_date)
    elif(order == 'least'):
        data = db.getlast5_covid19India(current_date)
    df = pd.DataFrame(data, columns = ['State/UT','Confirmed Cases','Cured Cases','Deaths'])
    df.index += 1
    return df
    
    
    
    


