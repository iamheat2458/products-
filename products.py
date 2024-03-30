product = []
while True:
    name = input('what are you buy?') 
    if name == 'q':
    	break
    price = input('what is price?')
    product.append([name, price])
print(product)
