import os

product = []
if os.path.isfile('products.csv'):
	print('file found!')
	with open('products.csv', 'r', encoding='utf-8') as f:
	    for line in f: 
		    if 'Stuff,Price' in line:
			    continue
		    name, price = line.strip().split(',')
		    product.append([name, price])
	print(product)

else:
	print('file not found...')



# input for user 
while True:
    name = input('what are you buy?') 
    if name == 'q':
    	break
    price = input('what is price?')
    proce = int(price)
    product.append([name, price])
print(product)

# print out the purchasing record 
for p in product:
	print(p[0], 'cost', p[1])

# file writing 
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('Stuff,Price\n')
	for p in product:
		f.write(p[0] + ',' + str(p[1]) + '\n')
