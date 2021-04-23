from URL_generator_and_house_profile import URL_and_houseprof
from API import search_api
from API import get_oauth_token
import pandas as pd
import time

"""using the variables from the function URL_and_houseprof we proceed to do the query 
"""
def API_query_input(house_profile, url):
    dfpage = {}

    if house_profile['operation'] == 'rent':

        for number in range(1,10):
            numpage = f'&numPage={number}'
            urlpage = url+numpage
            data = search_api(token['access_token'], urlpage)
            print(data['actualPage'])
            dfpage[number] = pd.DataFrame(data['elementList'])
            time.sleep(3)
        
        df = pd.concat(dfpage).droplevel(0)
        
    elif house_profile['operation'] == 'sale':

        for number in range(1,10):
            numpage = f'&numPage={number}'
            urlpage = url+numpage
            data = search_api(token['access_token'], urlpage)
            print(data['actualPage'])
            dfpage = pd.DataFrame(data['elementList'])
        
        df = pd.concat(dfpage).droplevel(0)

    return df    
        
