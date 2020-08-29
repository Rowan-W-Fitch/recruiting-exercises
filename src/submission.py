import copy

def compute_shipment(shipment, warehouses):
    min_list = warehouses + warehouses
    for i in range(0, len(warehouses)):
        ship_copy = copy.deepcopy(shipment)
        list = []
        res = recursive_helper(ship_copy, i, list, warehouses)
        if len(res) < len(min_list):
            min_list = res
    if len(min_list) > len(warehouses):
        return []
    return min_list


""" this function recursively backtracks through all combinations of warehouses starting from a given index"""
def recursive_helper(shipment, idx, list, warehouses):
    #if you have reached the end of the list of warehouses and not fulfilled order, break recursion with a list that is impossible to reach
    if idx == len(warehouses) and len(shipment) > 0:
        return warehouses + warehouses #not possible to reach this answer, the correct answer is guaranteed to be shorter
    #if you have fulfilled the shipment, then return the list of warehouses
    elif len(shipment) == 0:
        return list
    #else subtract the inventory of the warehouse at current index, add that warehouse to list, and recursively repeat from idx+1 to len(warehouses)
    else:
        #subtract inventory of current warehouse from the shipment
        warehouse = warehouses[idx]
        dict = {} #key: item, val: amount taken from warehouse
        rmv_key_list = [] # list of keys to remove form shipment
        for itm in shipment.keys():
            amount = get_warehouse_amt(warehouse, itm)
            if amount >= shipment[itm]:
                dict[itm] = shipment[itm]
                rmv_key_list.append(itm)
            else:
                dict[itm] = amount
                old = shipment[itm]
                shipment[itm] = old - amount
        #remove any items from shipment that are totally fulfilled
        for k in rmv_key_list:
            del shipment[k]
        #add the current warehouse to list
        list_dict = {}
        list_dict[warehouse['name']] = dict
        list.append(list_dict)
        #now recursively get shortest list
        min_list = warehouses + warehouses
        for i in range(idx+1, len(warehouses)+1):
            shipment_copy = copy.deepcopy(shipment)
            list_copy = copy.deepcopy(list)
            res = recursive_helper(shipment_copy, i, list_copy, warehouses)
            if len(res) < len(min_list):
                min_list = res

        return min_list


#small helper function for indexing nested dicts
def get_warehouse_amt(warehouse, item):
    itm_dict = warehouse['inventory']
    if item in itm_dict.keys():
        return itm_dict[item]
    else:
        return 0
