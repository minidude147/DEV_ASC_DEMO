import json



# with open("R1.json") as file:
#     data = json.load(file)

router_dict = {
"router": { 
        "hostname":"R1" , 
        "interfaces": [

            {
                "id": "0" , 
                "enabled": "True" ,
                "name": "GigabitEthernet0/0",
                "ip": "192.168.1.254",
                "mask":"255.255.255.0"
            },
            {   "id": "1" ,
                "enabled": "True",
                "name": "GigabitEthernet0/1" , 
                "ip": "192.168.1.253" , 
                "mask":"255.255.255.0"
            }  
                    ] , 
        "routing": {
                "routes" : [
                    {
                        "destination": "192.168.2.0", 
                        "mask" : "255.255.255.0" , 
                        "gateway":"192.168.2.253"
                    } , 
                    {
                        "destination":"192.168.3.1" , 
                        "mask":"255.255.255.0" , 
                        "gateway":"255.255.255.0" 
                    }



                         ]







        }         



 }


}








router_json = json.dumps(router_dict)


print(router_json)
print(type(router_json))
print(type(router_dict))



#print(router_json)




#with open("data.json" , "w") as file:
 #   json.dump(router_dict , file , indent = 2 )

#json.load = loads from json file into ram
#json.loads = takes json data which is in string format and turns it into a dict
#json.dump = takes python dict and writes it to a json file from within python
#json.dumps  = takes a python dict and converts it to a string object in ram