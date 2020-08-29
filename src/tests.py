from submission import compute_shipment

#test algo
def main():
    #shouldnt take the 1st warehouse here
    test_ship1 = {'a': 5, 'b':10, 'c':11, 'd':3}
    test_warehouses1 = [
    {'name': 'w1', 'inventory': {'a': 1, 'b': 1, 'd': 2}},
    {'name': 'w2', 'inventory': {'a': 2, 'b': 4, 'c': 6, 'd': 2}},
    {'name': 'w3', 'inventory': {'a': 2, 'b': 3, 'c': 4, 'd': 1}},
    {'name': 'w4', 'inventory': {'a': 3, 'b': 5, 'c': 1}}
    ]
    print(compute_shipment(test_ship1, test_warehouses1)) #ans should be [{w2: {a:2, b:4, c:6, d:2}}, {w3: {a: 2, b: 3, c: 4, d: 1}}, {w4: {a: 1, b: 3, c: 1}}]

    #should take the 1st and last warehouse here
    test_ship2 = {'a': 7, 'b': 11, 'c': 19, 'd': 5, 'e': 18}
    test_warehouses2 = [
    {'name': 'w1', 'inventory': {'a': 3, 'b': 5, 'd': 2}},
    {'name': 'w2', 'inventory': {'a': 1, 'b': 4, 'c': 6, 'd': 2, 'e': 11}},
    {'name': 'w3', 'inventory': {'a': 2, 'b': 4, 'c': 6, 'd': 2, 'e': 11}},
    {'name': 'w4', 'inventory': {'a': 3, 'b': 4, 'c': 6, 'd': 2, 'e': 11}},
    {'name': 'w5', 'inventory': {'a': 2, 'b': 4, 'c': 6, 'd': 2, 'e': 11}},
    {'name': 'w6', 'inventory': {'a': 2, 'b': 4, 'c': 6, 'd': 2, 'e': 11}},
    {'name': 'w7', 'inventory': {'a': 4, 'b': 6, 'c': 19, 'd': 3, 'e': 18}},
    ]
    print(compute_shipment(test_ship2, test_warehouses2)) #ans should be [{w1: {'a': 3, 'b': 5, 'd': 2}}, {w7: {'a': 4, 'b': 6, 'c': 19, 'd': 3, 'e': 18}}]

    #should take the 1st and 2nd here, 6th and 7th are also valid combo but would be more expensive
    test_ship3 = {'a': 7, 'b': 11, 'c': 19, 'd': 5, 'e': 18}
    test_warehouses3 = [
    {'name': 'w1', 'inventory': {'a': 3, 'b': 5, 'd': 2}},
    {'name': 'w2', 'inventory': {'a': 4, 'b': 6, 'c': 19, 'd': 3, 'e': 18}},
    {'name': 'w3', 'inventory': {'a': 2, 'b': 4, 'c': 6, 'd': 2, 'e': 11}},
    {'name': 'w4', 'inventory': {'a': 3, 'b': 4, 'c': 6, 'd': 2, 'e': 11}},
    {'name': 'w5', 'inventory': {'a': 2, 'b': 4, 'c': 6, 'd': 2, 'e': 11}},
    {'name': 'w6', 'inventory': {'a': 3, 'b': 5, 'd': 2}},
    {'name': 'w7', 'inventory': {'a': 4, 'b': 6, 'c': 19, 'd': 3, 'e': 18}},
    ]
    print(compute_shipment(test_ship3, test_warehouses3)) #ans should be [{w1: {'a': 3, 'b': 5, 'd': 2}}, {w2: {'a': 4, 'b': 6, 'c': 19, 'd': 3, 'e': 18}}]

    #should take the last here, there are other valid combos but they use more than 1 warehouse
    test_ship3 = {'a': 7, 'b': 11, 'c': 19, 'd': 5, 'e': 18}
    test_warehouses3 = [
    {'name': 'w1', 'inventory': {'a': 3, 'b': 5, 'd': 2}},
    {'name': 'w2', 'inventory': {'a': 4, 'b': 6, 'c': 19, 'd': 3, 'e': 18}},
    {'name': 'w3', 'inventory': {'a': 2, 'b': 4, 'c': 6, 'd': 2, 'e': 11}},
    {'name': 'w4', 'inventory': {'a': 3, 'b': 4, 'c': 6, 'd': 2, 'e': 11}},
    {'name': 'w5', 'inventory': {'a': 2, 'b': 4, 'c': 6, 'd': 2, 'e': 11}},
    {'name': 'w6', 'inventory': {'a': 3, 'b': 5, 'd': 2}},
    {'name': 'w7', 'inventory': {'a': 7, 'b': 11, 'c': 19, 'd': 5, 'e': 18}},
    ]
    print(compute_shipment(test_ship3, test_warehouses3)) #ans should be [{w7: {'a': 7, 'b': 11, 'c': 19, 'd': 5, 'e': 18}}]

    #should return empty list, not enough inventory for d
    test_ship4 = {'a': 17, 'b': 11, 'c': 19, 'd': 15, 'e': 18}
    test_warehouses4 = [
    {'name': 'w1', 'inventory': {'a': 3, 'b': 5, 'd': 2}},
    {'name': 'w2', 'inventory': {'a': 4, 'b': 6, 'c': 19, 'd': 3, 'e': 18}},
    {'name': 'w3', 'inventory': {'a': 2, 'b': 4, 'c': 6, 'd': 2, 'e': 11}},
    {'name': 'w4', 'inventory': {'a': 3, 'b': 4, 'c': 6, 'd': 2, 'e': 11}},
    {'name': 'w5', 'inventory': {'a': 2, 'b': 4, 'c': 6, 'd': 2, 'e': 11}},
    {'name': 'w6', 'inventory': {'a': 3, 'b': 5, 'd': 2}},
    {'name': 'w7', 'inventory': {'a': 7, 'b': 11, 'c': 19, 'd': 1, 'e': 18}},
    ]
    print(compute_shipment(test_ship4, test_warehouses4)) #ans should be []

    #should return entire list of warehouses, just enough inventory for d
    test_ship5 = {'a': 17, 'b': 11, 'c': 19, 'd': 14, 'e': 18}
    test_warehouses5 = [
    {'name': 'w1', 'inventory': {'a': 3, 'b': 5, 'd': 2}},
    {'name': 'w2', 'inventory': {'a': 4, 'b': 6, 'c': 19, 'd': 3, 'e': 18}},
    {'name': 'w3', 'inventory': {'a': 2, 'b': 4, 'c': 6, 'd': 2, 'e': 11}},
    {'name': 'w4', 'inventory': {'a': 3, 'b': 4, 'c': 6, 'd': 2, 'e': 11}},
    {'name': 'w5', 'inventory': {'a': 2, 'b': 4, 'c': 6, 'd': 2, 'e': 11}},
    {'name': 'w6', 'inventory': {'a': 3, 'b': 5, 'd': 2}},
    {'name': 'w7', 'inventory': {'a': 7, 'b': 11, 'c': 19, 'd': 1, 'e': 18}},
    ]
    print(compute_shipment(test_ship5, test_warehouses5)) #ans should be whole list of warehouses


#execute actual tests by just running this file
main()
