import yaml 


with open("R1.yml") as file:
    data  = yaml.safe_load(file)


print(type(data))
