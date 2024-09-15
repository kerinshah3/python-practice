#Dicts

d = { "key" : 9}

print(d["key"])

d["key2"] = 10
d["key5"] = 90


print(d)


del d["key2"]

print(d)

for key , value in d.items():
    print("key: "+ key + " value: " + str(value))
