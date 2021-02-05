shopping_list=["milk","rice","eggs","bread","znger"]

item_to_find = "spam"
found_at = None
#for index in range(6):
#for index in range(len(shopping_list)):
 #     break
if item_to_find in shopping_list:
    found_At = shopping_list.index(item_to_find)
if found_at is not None:
    print("item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))