from URL_generator_and_house_profile import URL_and_houseprof
from API import search_api
from API import get_oauth_token
import pandas as pd


url, house_profile = URL_and_houseprof()

token = get_oauth_token()

numpage = search_api(token['access_token'], url)

if house_profile['operation'] == 'rent':

    for number in range(1,40):
        numpage = f'&numPage={number}'
        urlpage = url+numpage
        data = search_api(token['access_token'], urlpage)
        print(data['actualPage'])
        df = pd.DataFrame(data['elementList'])
        df.to_csv(f'../Final_project/Data_rent/rent_page_{number}.csv')

elif house_profile['operation'] == 'sale':

    for number in range(1,5):
        numpage = f'&numPage={number}'
        urlpage = url+numpage
        data = search_api(token['access_token'], urlpage)
        print(data['actualPage'])
        df = pd.DataFrame(data['elementList'])
        df.to_csv(f'../Final_project/Data_sale/sale_page_{number}.csv')