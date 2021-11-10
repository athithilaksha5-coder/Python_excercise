#empty_dictionary
my_dict = {}

#dictionary with mixed keys
my_dict = {'name' :'john', 101:'raman',1:[5,4,6]}
print(my_dict)

my_dict = {'name':'arjun' ,'age':25}

print(my_dict['name'])
print(my_dict.get('age'))

# used get method avoid keyerror 
print(my_dict.get('address'))

#try to access keys which doesn't exit throws error

print(my_dict.get['address'])




