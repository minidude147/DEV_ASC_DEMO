import xmltodict




with open("r1.xml") as file:
    xml_data = file.read()


#print(xml_data)

data = xmltodict.parse(xml_data)



print(data["router"]["interfaces"]["interface"][0]["ip"])    



print(data)