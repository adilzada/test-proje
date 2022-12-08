import json
 
with open ('config2.json','r',encoding="utf-8") as file:
    data = json.load(file)

data['vm']['ip'] = '192.168.42.5'
data['vm']['memory'] = '2048'
 
data['vm']["forwarded_ports"].append({
    "guest_port": 35729,
    "host_port": 35729
})
 
data['vdd']["sites"]["drupal7"]["vhost"]["alias"].append(
    "www.elizabeth@second.uk")
    
data['vdd']['sites']['drupal7']['account_name'] = 'predator'
data['vdd']['sites']['drupal7']['account_mail'] = 'predator@mail.ru'
data['vdd']['sites']['drupal7']['account_pass'] = '2020'
 
 
with open("my_config.json", "w") as file:
    json.dump(data, file)
