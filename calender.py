l={"January":6,"February":2,"March":2,"April":5,"May":0,"June":3,"July":5,"August":1,"September":4,"October":6,"November":2,"December":4}
dict1={0:"Sunday",1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday",8:"Monday",9:"Tuesday",10:"Wednesday",11:"Thursday",12:"Friday",13:"Saturday",
          -1:"Saturday",-2:"Friday",-3:"Thursday",-4:"Wednesday",-5:"Tuesday",-6:"Monday",-7:"Sunday"}
dict2={15:9,16:7,17:5,18:3,19:1,20:0,21:-2,22:-4,23:-6,24:-8,25:-10}
Month=input("Enter Month:")
m=l[Month]
Year=int(input("Enter Year:"))
y=str(Year)[2:]
z=int(str(Year)[:2])
Date=int(input("Enter Date:"))
Nleap=int(int(y)/4)
add=int(m)+int(y)+Date+Nleap+dict2[z]
a=add%7
b=a-1
if  y=="00":
   if Year%400 ==0 and Month=="January" or Month=="February":
        print(dict1[b])
   elif Year%400!=0 and Month=="January" or Month=="February":
       print(dict1[a])
elif Year%4==0 and Month=="January" or Month=="February":
        print(dict1[b])
else:
   print(dict1[a])
