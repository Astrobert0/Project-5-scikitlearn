from URL_generator_and_house_profile import URL_and_houseprof

from API import search_api

"""

print(search_api(token,"http://api.idealista.com/3.5/pt/search?operation=sale&propertyType=homes&center=38.737037,-9.133802&distance=4000"))
"""

url, house = URL_and_houseprof()

print(url,'\n',house,'\n\n')