import requests
import os
import subprocess as sp

treshold = 1

used_memory = sp.getoutput("free -m | awk '/^Mem/ {print $3}'")
print(used_memory)

available_memory = sp.getoutput("free -m | awk '/^Mem/ {print $2}'")
print(available_memory)

memory_consumption = (float(used_memory) * 100/float(available_memory))

if memory_consumption > treshold:
   print("Memory Usage Alert. Sending data to Storage")
   output = sp. getoutput('ps aux')
   data={}
   data['date'] = ""
   data['host'] = ""
   data['message'] = output
   params = {'code': ''}
   response = requests.post('', params=params, json=data)
   print(response.content)
