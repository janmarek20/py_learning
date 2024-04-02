shopping = {'piekarnia': ['chleb', 'pączek', 'bułki'],
            'warzywniak': ['marchew', 'seler', 'rukola']
}

for shop, products in shopping.items():
    products_names = [product.capitalize() for product in products]
    all_products += products