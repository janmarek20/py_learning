shopping = {'piekarnia': ['chleb', 'pączek', 'bułki'],
            'warzywniak': ['marchew', 'seler', 'rukola']
}

print('Hey')
print('Hejko')

for shop, products in shopping.items():
    products_names = [product.capitalize() for product in products]
    all_products += products
    print(f'Idę do {shop.capitalize()} i kupuję tam {products_names}')
print(f'W sumie kupuję tam {len(all_products)} produktów.')
