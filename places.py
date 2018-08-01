import urllib.request as ur
import json

def place(userInput,userLocation):
    userLocation=userLocation.replace(' ','+')
    url='https://maps.googleapis.com/maps/api/place/textsearch/json?query='+userInput+'+in+'+userLocation+'\&key=Your-API-Key'
    req=ur.Request(url)
    with ur.urlopen(req) as response:
        page=response.read()
        placeId=[]
        jsonFormat=json.loads(page)
        for data in jsonFormat['results']:
          placeId.append(data['place_id'])
        return placeId

def placeDetails(p_id):

    for data in p_id:
        url = 'https://maps.googleapis.com/maps/api/place/details/json?placeid='+data+'&key=Your-API-Key'
        req = ur.Request(url)

        with ur.urlopen(req) as response1:
            page1 = response1.read()
            result1 = str()
            jsonFormat = json.loads(page1)


            result1+=jsonFormat['result']['name']+'\n'+jsonFormat['result']['formatted_address']+'\n'+'\n'
        print(result1)

    print("Anything else ? \n")

print("enter your location : ")
user_location=input()
while True:
        print("What you wanna search at {} : \n".format(user_location))
        print("1.Hotels")
        print("2.Gym")
        print("3.Restaurent")
        print("4.clubs")
        print("5.spa")
        print("6.Exit")
        userInput=int(input())
        if userInput == 1:
            p_id=place('hotels',user_location)
        elif userInput == 2:
            p_id=place('gym',user_location)
        elif userInput == 3:
            p_id=place('restaurents',user_location)
        elif userInput == 4:
            p_id=place('club',user_location)
        elif userInput == 5:
            p_id=place('spa',user_location)
        elif userInput==6:
            quit()
        placeDetails(p_id)
