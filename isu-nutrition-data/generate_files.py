'''generates seperate json files for each station/date combo'''

import json
import os
import shutil


with open('data.json') as f:
    rawData = json.load(f)


data = {}

## convert dictionary from station:date to date:station
for centerName, centerData in rawData.items():
    if not 'stations' in centerData:
        continue
    
    formatedData = {}
   
    for station, stationData in centerData['stations'].items():
        for date, dateData in stationData['dates'].items():
            if date not in formatedData:
                formatedData[date] = {}
            for meal, mealData in dateData['meals'].items():
                if meal not in formatedData[date] :
                    formatedData[date][meal]  = {}
                
                formatedData[date][meal][station] = mealData 
    data[centerName] = formatedData


## remove excess food data

for center, centerData in data.items():
    for date, dateData in centerData.items():
         for meal, mealData in dateData.items():
            for station, stationData in mealData.items():
                foods = []
                for food in stationData['foods']:
                    if food == {}:
                        continue
                    
                    try:
                        food_ = {
                            'name':food['name'],
                            'servingSize':food['servingSize'],
                            'fat': food['Total Fat'],
                            'carbs': food['Total Carbohydrate'],
                            'protein': food['Protein'],
                            'calories':food['Calories']
                        }
                    except:
                        continue

                    foods.append(food_)
                
                data[center][date][meal][station] = sorted(foods, key=lambda elem: int(elem['calories']) , reverse=True)


# reformat date keys

data_ = {}

for center, centerData in data.items():
    data_[center] = {}
    for date, dateData in centerData.items():
        arr = date.split(", ")
        newDate = ' '.join(arr[1:])
        newDate = '_'.join(newDate.split(' '))
        
        data_[center][newDate] = dateData

with open('data_cleaned.json', 'w') as f:
    json.dump(data_, f, sort_keys=True,indent=4, ensure_ascii=False, )


data = data_

# generate files

if os.path.exists('data'):
    shutil.rmtree('data')
os.mkdir('data')


for center, centerData in data.items():

    centerName = '_'.join(center.split(' '))

    if os.path.exists('data/' + centerName):
        shutil.rmtree('data/' + centerName)
    os.mkdir('data/' + centerName)

   
    
    for date, dateData in centerData.items():
        with open('data/' + centerName + '/' + date + '.json', 'w') as f:
            json.dump(data[center][date], f, sort_keys=True,indent=4, ensure_ascii=False, )

#generate list of dining cetners

centers = []

for center, centerData in data.items():
    centers.append(center)

with open('data/dining-centers.json', 'w') as f:
        json.dump(centers, f, sort_keys=True,indent=4, ensure_ascii=False, )