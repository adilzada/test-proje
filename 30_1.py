import json
with open ('config1.json','r',encoding="utf-8") as file:
    data = json.load(file)
 
data["author"] ="ilkin_adil"
data["server"]["port1"] = 2024
data["server"]["port2"] = 2025
data["openInBrowser"] = True
data["dist"]["fonts"] = "Colibri"
 
with open("my_config.json", "w") as file:
    json.dump(data, file)
