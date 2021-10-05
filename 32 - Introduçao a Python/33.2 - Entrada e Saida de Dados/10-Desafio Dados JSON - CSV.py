# Dado o seguinte arquivo no formato JSON ,(json.json)
# leia seu conteúdo e calcule a porcentagem de livros em cada categoria,
# em relação ao número total de livros. O resultado deve ser escrito em um
# arquivo no formato CSV 

import json
import csv

jsonName="json.json"

def arrAppendjson(jsonName):
  arr = []
  with open(jsonName) as file:
   for line in file:
    arr.append(json.loads(line))
  return arr

def arrOfCategoriesPropertieInObjectsInArr(arr):
  categories = []
  output = []    
  for i in arr:
   if i not in categories:
      categories.append(i['categories'])
  for j in categories:
    for k in j:
      if k not in output:
        output.append(k)
  return output

arrOfObjects = arrAppendjson(jsonName)
arrOfCategories = arrOfCategoriesPropertieInObjectsInArr(arrOfObjects)

def arryOfRepetions(arrOfObjects, arrOfCategories):
  arr = []
  for i in arrOfCategories:
    for j in arrOfObjects:
      for k in j["categories"]:
         if k == i :
          arr.append(k)
  return arr 


arr  = (arryOfRepetions(arrOfObjects, arrOfCategories))

def objOfCountsRepetions(arr):
    obj = {}
    for i in arr:
        if i in obj:
            obj[i] += 1
        else:
            obj[i] = 1
    return obj

objRepetion = (objOfCountsRepetions(arr))

def percentualOfEachCategory(objRepetion, arrOfObjects):
  output = []
  all = len(arrOfObjects)
  for i in objRepetion:
    output.append([i, objRepetion[i]/all * 100])
  return output

eachCategoryArr =percentualOfEachCategory(objRepetion, arrOfObjects)  

def writeCSV(eachCategoryArr):
  with open('results.csv','w') as csvfile:
    for i in eachCategoryArr:
      csv.writer(csvfile).writerow(i)


writeCSV(eachCategoryArr)
