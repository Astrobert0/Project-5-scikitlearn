import tkinter as tk
from PIL import Image, ImageTk
import pickle
import pandas as pd
import warnings
import xgboost as xgb 
import time

warnings.filterwarnings("ignore") #LATER RUN ALL IN HQ WITH ALL THE LIBRARIES UPDATED
        


def input_variable_confirmation():
    try:
        int(property_size.get())
        int(floor.get())
        float(latitude.get())
        float(longitude.get())
        input_list_construct()
    except ValueError:
        answer.config(text= 'A wrong value was inserted')
        
def input_list_construct():
    house_prf= {'size':int(property_size.get()), 'rooms':variablerooms.get(),'bathrooms':variablebathrooms.get(),'latitude':float(latitude.get()), 'longitude':float(longitude.get()), 
    'floorNumeric':int(floor.get()),'propertyType_duplex': 0, 'propertyType_flat': 0,'propertyType_penthouse':0,'propertyType_studio': 0}
    propert = variableproperty.get()
    
    if propert == 'duplex': 
        house_prf['propertyType_duplex'] += 1

    elif propert == 'flat': 
        house_prf['propertyType_flat'] += 1

    elif propert == 'penthouse': 
        house_prf['propertyType_penthouse'] += 1

    elif propert == 'studio': 
        house_prf['propertyType_studio'] += 1

    operationType = variableoperation.get()
    prediction(house_profile= house_prf, operation=operationType)

 

def prediction(house_profile, operation):
    if operation == 'rent':
        model = pickle.load(open(r'C:\Users\Sebas!\Documents\GitHub\Project-5-scikitlearn\rent_model.sav','rb'))
        df = pd.DataFrame(house_profile, index=[0])
        model_predict = model.predict(df)
        answer.config(text= f'The price of your house is {model_predict[0]}')

    elif operation== 'sale':
        model = xgb.XGBRegressor()
        model.load_model(r"C:\Users\Sebas!\Documents\GitHub\Project-5-scikitlearn\sale_model.json")
        df = pd.DataFrame(house_profile, index=[0])
        model_predict = model.predict(df)
        answer.config(text= f'The price of your house is {model_predict[0]}')


def image_show():
    img.show()

root = tk.Tk()

#Answer label-----------------------------------------------------------------------------------------------------------------------------------------------------
answer = tk.Label(root, text='')
answer.grid(row=9, column=1)

#Property size-----------------------------------------------------------------------------------------------------------------------------------------------------
L1 = tk.Label(root, text= 'Insert the property size').grid(row=0,column=0)

property_size = tk.Entry(root)
property_size.grid(row=0, column=1)

#coordinates-----------------------------------------------------------------------------------------------------------------------------------------------------
L2 = tk.Label(root, text='Insert the coordinates').grid(row=1, column=0)

#loading image
img = Image.open(r'C:\Users\Sebas!\Documents\GitHub\Project-5-scikitlearn\Images\coord_find.png')
#load = load.resize((370, 201), Image.ANTIALIAS)

# setting image with the help of label
image_button = tk.Button(root, text='How can i find it?', command= image_show)
image_button.grid(row = 2, column = 0, columnspan = 1, rowspan = 2, padx = 5, pady = 5)

#Latitude and longitude
L3 = tk.Label(root,text='Latitude').grid(row=2, column=1)

latitude = tk.Entry(root)
latitude.grid(row=2, column=2)

L4 = tk.Label(root, text= 'Longitude').grid(row=3, column=1)

longitude = tk.Entry(root)
longitude.grid(row=3, column=2)

#floor-----------------------------------------------------------------------------------------------------------------------------------------------------
L5 = tk.Label(root, text = 'Insert the floor (If it\'s ground floor, insert 0)').grid(row=4, column=0)

floor = tk.Entry(root, validate= 'key')
floor.grid(row=4,column= 1)

#property type-----------------------------------------------------------------------------------------------------------------------------------------------------
L6 = tk.Label(root, text = 'Select the property type').grid(row=5, column=0)

properties = ['flat', 'duplex','penthouse','studio']
variableproperty = tk.StringVar(root)
variableproperty.set(properties[0])

propertyType = tk.OptionMenu(root, variableproperty, *properties)
propertyType.grid(row=5, column=1)

#operation-----------------------------------------------------------------------------------------------------------------------------------------------------
L7 = tk.Label(root, text = 'Select the operation').grid(row=6, column=0)

operationList = ['rent', 'sale']
variableoperation = tk.StringVar(root)
variableoperation.set('rent')

operation = tk.OptionMenu(root, variableoperation, *operationList)
operation.grid(row=6, column=1)
#rooms-----------------------------------------------------------------------------------------------------------------------------------------------------
L8 = tk.Label(root, text = 'Select the ammount of rooms').grid(row=7, column=0)

roomList = [0,1,2,3,4]
variablerooms = tk.IntVar(root)
variablerooms.set(roomList[0])

rooms = tk.OptionMenu(root, variablerooms, *roomList)
rooms.grid(row=7, column=1)

#bathrooms-----------------------------------------------------------------------------------------------------------------------------------------------------
L9 = tk.Label(root, text = 'Select the ammount of bathrooms').grid(row=8, column=0)

bathList = [1,2,3,4]
variablebathrooms = tk.IntVar(root)
variablebathrooms.set(bathList[0])

bathrooms = tk.OptionMenu(root, variablebathrooms, *bathList)
bathrooms.grid(row=8, column=1)
#Predict script----------------

predict_button = tk.Button(root, text='Predict', bg="#20bebe", fg='white', command=  input_variable_confirmation)
predict_button.grid(row=9, column=0)


#Exit button-----------------------------------------------------------------------------------------------------------------------------------------------------
exit_button = tk.Button(root, text="Exit",  bg="red",fg="white", command=root.destroy)
exit_button.grid(row=9, column=2)

root.mainloop()