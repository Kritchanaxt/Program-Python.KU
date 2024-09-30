
#* 10.

president_status = {'Obama': 'Hawaii', 'Bush': 'Texas', 'Clinton': 'Arkansas'}
print(type(president_status))

print(president_status["Clinton"])
print(president_status.keys())

for item in president_status.keys():
    print(item)

print(president_status.values())
print(president_status.items())

#* define คือ ค่าคีย์

for item in president_status:
    print(item)
