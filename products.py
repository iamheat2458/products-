product = []
while True:
    name = input('what are you buy?') 
    if name == 'q':
    	break
    price = input('what is price?')
    proce = int(price)
    product.append([name, price])
print(product)

for p in product:
	print(p[0], 'cost', p[1])

with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in product:
		f.write(p[0] + ',' + str(p[1]) + '\n')
