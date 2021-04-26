from API import search_api
from API import get_oauth_token
import pandas as pd
import time

"""using the variables from the function URL_and_houseprof we proceed to do the query 
"""
def API_query_input(house_profile, url, pages, token):
    dfpage = {}

    if house_profile['operation'] == 'rent':

        for number in pages:
            numpage = f'&numPage={number}'
            urlpage = url+numpage
            data = search_api(token['access_token'], urlpage)
            print(data['actualPage'])
            dfpage[number] = pd.DataFrame(data['elementList'])
            time.sleep(3)
        
        df = pd.concat(dfpage).droplevel(0)
        df.to_csv(f'../Project-5-scikitlearn/Data_rent/rent_test.csv')

        
    elif house_profile['operation'] == 'sale':

        for number in pages:
            numpage = f'&numPage={number}'
            urlpage = url+numpage
            data = search_api(token['access_token'], urlpage)
            print(data['actualPage'])
            dfpage[number] = pd.DataFrame(data['elementList'])
        
        df = pd.concat(dfpage).droplevel(0)
        df.to_csv(f'../Project-5-scikitlearn/Data_sale/sale_test.csv')
    return df    
        
