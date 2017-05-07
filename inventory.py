#coding=utf-8
'''
遍历字典，格式输出所有健和值  游戏的物品清单
'''
stuff = {'rope':1,'torch':6, 'gold coin':42,'dagger':1,'arrow':12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k,v in inventory.items():
        print(str(v) +' '+k)
        item_total += v
    print ("Total number of items:"+ str(item_total))

displayInventory(stuff)


'''
遍历字典，添加物品，如果有则加1，无则添加
返回一个字典
'''
def addToInventory(inventory,addedItems):
    for indexOfItem in range(len(addedItems)):
        itemsToadded = addedItems[indexOfItem]
        if itemsToadded in inventory:
            inventory[itemsToadded] += 1
        else:
            inventory[itemsToadded] = 1
    return inventory


inv = { 'gold coin': 42, 'rope':1 }
drangonLoot = ['gold coin','dagger','gold coin','gold coin','ruby']
inv = addToInventory(inv,drangonLoot)
displayInventory(inv)
