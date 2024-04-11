shopping = {'piekarnia': ['chleb', 'pączek', 'bułki'],
            'warzywniak': ['marchew', 'seler', 'rukola']
}

all_products = 0
for shop, products in shopping.items():
    products_names = [product.capitalize() for product in products]
    all_products += len(products)
    print(f'Idę do {shop.capitalize()} i kupuję tam {products_names}')
print(f'W sumie kupuję tam {all_products} produktów.')