import inquirer

def URL_and_houseprof():
   """This python function returns 2 variables, which is url and house_profile; url it is a string that will be used to make the query in the function search_api() 
   and house_profile it is a dictionary that as the name implies, has the characteristic of the property that the user inputs """

   distance = 4000
   center = '38.737037,-9.133802' #This is the coordinates of the cities where we will apply the query Lisbon

   questions = [ 

            inquirer.List('operation', message= 'Which operation you want to perform?', choices = ['rent', 'sale']),
                         ]

   main_answers = inquirer.prompt(questions)

   if main_answers['operation'] == 'rent':

      propertyType = inquirer.prompt([inquirer.List('propertyType',message='What is the type of property?', choices=['flat', 'duplex', 'studio', 'penthouse'])])
      sizehome = input('What is the size of the property? (minimum 60, maximum 1000)\n ')
      bedrooms = input('How many bedrooms? (insert numbers only up to 4)\n ')
      bathrooms = input('How many bathrooms? (insert numbers only up to 3)\n ')
      flat = inquirer.prompt([inquirer.Confirm('apartment', message= 'It is an apartment?', default=False)])

      url = f'http://api.idealista.com/3.5/pt/search?operation={main_answers["operation"]}&propertyType=homes&center={center}&distance={distance}&minSize={sizehome}&maxSize={sizehome}&flat={flat["apartment"]}&bedrooms={bedrooms}&bathrooms={bathrooms}'      

      house_profile = main_answers
      house_profile['size'] = sizehome
      house_profile['bedrooms'] = bedrooms
      house_profile['bathrooms'] = bathrooms
      house_profile['flat'] = flat['apartment']    
      house_profile['latitude'] = 38.737037
      house_profile['longitude'] = -9.133802  
      house_profile['distance'] = distance
         

   return url, house_profile