def sales(cars, customers):
    # sort the lists
    cars.sort()
    customers.sort()
    
    # make pointers to iterate with
    carP = 0
    customerP = 0
    sales = 0
    
    while carP < len(cars) and customerP < len(customers):

        if customers[customerP] >= cars[carP]:
            sales += 1
            carP += 1  # move to the next car & customer
        customerP += 1
    
    return sales


if __name__ == "__main__":
    print(sales([20, 10, 15], [11, 25, 15]))
    print(sales([13, 7, 2, 3, 12, 4, 19], [3, 25, 16, 14]))
    print(sales([24, 6, 20, 21, 12, 5], [25, 1, 24, 15]))
    print(sales([14, 9, 10, 15, 18, 20], [24, 17, 9, 22, 12, 4]))
