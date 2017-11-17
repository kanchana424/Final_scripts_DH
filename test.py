f = open('C:\python3.6\Final scripts\disks.txt','r')
f_data = f.read()

list_of_bits = list(f_data)
csv_string = '\n'.join(list_of_bits[0:])

# these 3 lines show what is going on
#print(f_data)
print(list_of_bits)
#print(csv_string)

f_out = open('./disks.csv', 'w')
f_out.write(csv_string)
f_out.close()

