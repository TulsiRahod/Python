dictionary={"capitals":{"france":"paris","Germany":"Berlin"},"city":["Dehli","Mumbai","cheenai","GUjarat"]}

def add(a,b,c):
    travel={}
    travel["country"]=a
    travel["city"]=b
    travel["Total_visit"]=c
    travel_log.append(travel)
# travel={
#     "France":{"city":["Paris","Lille","Dijon"],"Total_visit":12},
#     "Germany":{"city":["Berlin","Hamurg","Stuttgart"],"Total_visit":5}
# }

# print(travel["France"])

travel_log=[
    {
        "country":"France",
      "city":["Paris","Lille","Dijon"],
      "Total_visit":12
      },
    {
    "country":"Germany",
     "city":["Berlin","Hamurg","Stuttgart"],
     "Total_visit":5
     }
]
add(a="Russia",b=["Moscow","Saint petersbug"],c=2)
print(travel_log)