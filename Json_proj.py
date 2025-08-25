import json
import xmltodict

# with open("car_data.json") as file:
    # data = json.load(file)



# print(data)    

with open("Car_data.xml") as file1:
    data2 = file1.read()




data3 = xmltodict.parse(data2)


print(data3["automobile"]["drivers"])



