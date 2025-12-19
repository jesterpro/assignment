#7-8

sandwich_orders= ['Tuna sandwich','Wasabi sandwich','cheese sandwich']
finished_sandwiches= []
for items in sandwich_orders:
    print(f"Making ",items)
while sandwich_orders:
        finished_orders= sandwich_orders.pop()
        print(f"I finished making your {finished_orders.title()}")
        finished_sandwiches.append(finished_orders)
"""
#7-9
sandwich_orders= ['pastrami','tuna sandwich','pastrami','wasabi sandwich','cheese sandwich','pastrami']
finished_sandwiches= []
print("choose from the list below")
print(sandwich_orders)
print("Oops sorry we ran out of pastrami, please check the list again")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)
for items in sandwich_orders:
    print(f"Making ",(items))
while sandwich_orders:
        finished_orders= sandwich_orders.pop()
        print(f"i finished making your {finished_orders.title()}")
        finished_sandwiches.append(finished_orders)

"""
