countries = {
    "Pakistan": 28387482934848,
    "India": 24732899,
    "Bangladesh": 392838,
    "Indoneshia": 299338282,
    "China": 2838472122828182838,
    "Russia": 495327859059,
    "Iran": 10_000_000
}

max = 0

for i in range(3):
    max = 0
    for i in countries.keys():
        if countries[i] > max:
            max = countries[i]
            name = i
    topper = {}
    topper[name] = max
    print(topper)
    countries.pop(name)