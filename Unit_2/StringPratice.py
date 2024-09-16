#code is designed to extract a pice of information 

#using two string function today: split() and replace()

sunocoPrice = "Sunoco gas price: 4.24$"
mirabitoPrice = "Mirabito gas price: 3.45$"

#extract and isolate the prices
priceOfSunco = sunocoPrice.split(" ")
priceOfMirabito = mirabitoPrice.split(" ")
print(priceOfSunco[3])
print(priceOfMirabito[3])

#what kide of type of data are these?

print(type(priceOfSunco))
print(type(priceOfMirabito))
