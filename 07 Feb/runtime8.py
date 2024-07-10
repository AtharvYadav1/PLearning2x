dict_src = {1:20,2:24,3:25, 4:29, 5:32}
dict_output={key: value for (key,value) in dict_src.items() if value%2==0}

print(dict_src)
print(dict_output)