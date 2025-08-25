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




with open("data.json" , "w") as file:
    json.dump(router_dict , file , indent = 2 )

