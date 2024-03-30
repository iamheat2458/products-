product = []
while True:
    name = input('what are you buy?') 
    if name == 'q':
    	break
    price = input('what is price?')
    product.append([name, price])
print(product)

for p in product:
	print(p[0], 'is', p[1])