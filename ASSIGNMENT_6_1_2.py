# 2. Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.

# State_Name          <------>             Capital
 
# Andhra Pradesh	  ------>              Amaravati
# Arunachal Pradesh   ------>         	   Itanagar
# Assam               ------>              Dispur
# Bihar               ------>	           Patna
# Chhattisgarh	      ------>              Raipur
# Goa                 ------>	           Panaji
# Gujarat             ------>	           Gandhinagar
# Haryana             ------>	           Chandigarh
# Himachal Pradesh    ------>	           Shimla
# Jharkhand           ------>	           Ranchi
# Karnataka	          ------>              Bengaluru
# Kerala	          ------>              Thiruvananthapuram
# Madhya Pradesh      ------>	           Bhopal
# Maharashtra         ------>	           Mumbai
# Manipur	          ------>              Imphal
# Meghalaya      	  ------>              Shillong
# Mizoram	          ------>              Aizawl
# Nagaland	          ------>              Kohima
# Odisha         	  ------>              Bhubaneswar
# Punjab	          ------>              Chandigarh
# Rajasthan           ------>	           Jaipur
# Sikkim	          ------>              Gangtok
# Tamil Nadu          ------>	           Chennai
# Telangana	          ------>              Hyderabad
# Tripura	          ------>              Agartala
# Uttar Pradesh       ------>	           Lucknow
# Uttarakhand         ------>	           Dehradun (Winter) , Gairsain (Summer)
# West Bengal         ------>	           Kolkata


import json

size=int(input("enter the size for : "))   #7
india={}
for i in range(size):
    states=input("enter the states : ")
    capitals=input("enter the capitals : ")
    india[states]=capitals
print(india)
print(type(india))

jsonIndia = json.dumps(india)
print(jsonIndia)
print(type(jsonIndia))