
guest_list=['Paul', 'John', 'Rokan', 'Levi']
print( guest_list[0], 'you are here by invited to the ceremony')
print( guest_list[1], 'you are here by invited to the ceremony')
print( guest_list[2], 'you are here by invited to the ceremony')
print( guest_list[3], 'you are here by invited to the ceremony')
print( guest_list, 'Due to availability of space, more guest will be invited to the ceremony')
guest_list.insert(0, 'Bryan')
guest_list.insert(2, 'Boris')
guest_list.append('Jack')
print(guest_list)
print(len(guest_list))
for item in guest_list:
 print(f'{item} you are here by invited to the ceremony.')
for item in guest_list:
 print(f'{item} sorry but only 2 spots are available at the moment.')
appology= guest_list.pop(0)
print(f'Due to lack of space we are sorry to say you are no longer invited {appology.title()}.')
appology= guest_list.pop(1)
print(f'Due to lack of space we are sorry to say you are no longer invited {appology.title()}.')
appology= guest_list.pop(3)
print(f'Due to lack of space we are sorry to say you are no longer invited {appology.title()}.')
appology= guest_list.pop(3)
print(f'Due to lack of space we are sorry to say you are no longer invited {appology.title()}.')
appology= guest_list.pop(2)
print(f'Due to lack of space we are sorry to say you are no longer invited {appology.title()}.')
print(guest_list)
print( guest_list[0], 'you are still invited to the ceremony')
print( guest_list[1], 'you are still invited to the ceremony')
print(len(guest_list))
del guest_list[0]
del guest_list[0]
print(guest_list)
print(len(guest_list))

