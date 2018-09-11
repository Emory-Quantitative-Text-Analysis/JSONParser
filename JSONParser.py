import json
import csv

"""
Usage: python JSONParser.py
Make sure to change the filename 
"""
filename = 'Murphy Miracles thicker than fog.json'
with open(filename) as file:
	json_dic = json.load(file)
file.close()
result_dic = {
	'id':None,
	'subject':None,
	'relation':None,
	'object':None
}
output = open("./Murphy Miracles thicker than fog SVO.csv",'w',newline='')
Fields = ['id','subject','relation','object']
writer = csv.DictWriter(output,fieldnames = Fields)
writer.writeheader()
id_=0
for each in json_dic['facts']:
	id_+=1
	result_dic['id']=id_
	result_dic['subject']=each['subject']['text']
	result_dic['relation']=each['relation']['text']
	result_dic['object']=each['object']['text']
	writer.writerow(result_dic)
output.close()
