data_types = ("Boolean", "Integer", "Float", "Dictionary", "Set", "Strings", "List")
for i in range(len(data_types)):
  print(data_types[i])

data_type = input("\nChoose a data type\n")


if data_type.lower() == "boolean":
  value = input("Choose True or False\n")
  if value == "True":
    print(True)
  else:
    print(False)
elif data_type.lower() == "integer":
  print("Integer")
elif data_type.lower() == "float":
  print("Float")
elif data_type.lower() == "dictionary":
  length = int(input("How many values?\n"))
  new_dict = {}
  for i in range(length):
    key = input(f"Key {i} ")
    value = input(f"Value {i} ")
    new_dict[key] = value
  print(new_dict)
elif data_type.lower() == "set":
  print("Set")
elif data_type.lower() == "strings":
  print("Strings")
elif data_type.lower() == "list":
  length = int(input("How many values?\n"))
  new_list = []
  for i in range(length):
    new_list.append(input(f"Value{i} "))
  print(new_list)
