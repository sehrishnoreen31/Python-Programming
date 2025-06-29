import uuid

url = 'https://www.geeksforgeeks.org/python/generating-hash-ids-using-uuid3-and-uuid5-in-python/'
id_1 = uuid.uuid1()
print(id_1)
id_3 = uuid.uuid3(uuid.NAMESPACE_URL, url)
print(id_3)
id_4 = uuid.uuid4()
print(id_4)
id_5 = uuid.uuid5(uuid.NAMESPACE_URL, url)
print(id_5)
###########################################################################

print('Formatting........')
new_id = uuid.uuid4()
# max length of uuid is 36
new_id = str(new_id).replace("-", "")[:10].upper()
print(new_id)
new_id = uuid.uuid4()
new_id = str(new_id).replace("-", "")[:20].lower()
print(new_id)
###########################################################################
