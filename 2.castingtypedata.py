# casting adalah merubaj dari satu type ke type yang lain
# merubah satu type data ke type data yang lain
# type data = int, float, str, bool 

# Integer
print("============================Integer==============================")
data_integer = 10;
print("data = ", data_integer, ", type = ",type(data_integer))

data_float  = float(data_integer)
data_string = str(data_integer)
data_boolean = bool(data_integer) # akan false jika nilai int = 0
print("data = ", data_float, ", type = ",type(data_float))
print("data = ", data_string, ", type = ",type(data_string))
print("data = ", data_boolean, ", type = ",type(data_boolean))


# Float
print("============================FLOAT==============================")
data_float = 1.2;
print("data = ", data_float, ", type = ",type(data_float))

data_integer  = int(data_float) # akan dibulatkan ke bawah
data_string = str(data_float)
data_boolean = bool(data_float) #akan false jika nilai float = 0 
print("data = ", data_integer, ", type = ",type(data_integer ))
print("data = ", data_string, ", type = ",type(data_string))
print("data = ", data_boolean, ", type = ",type(data_boolean))


# Boolean
print("============================Boolean==============================")
data_boolean = True;
print("data = ", data_boolean, ", type = ",type(data_boolean))

data_integer  = int(data_boolean) # akan dibulatkan ke bawah
data_string = str(data_boolean)
data_float = float(data_boolean) #akan false jika nilai float = 0 
print("data = ", data_integer, ", type = ",type(data_integer ))
print("data = ", data_string, ", type = ",type(data_string))
print("data = ", data_float, ", type = ",type(data_float))


# String
print("============================String==============================")
data_string = "10";
print("data = ", data_string, ", type = ",type(data_string))

data_integer  = int(data_string) # string harus angka
data_boolean = bool(data_string) # false jika string kosong
data_float = float(data_string) # string harus angka 
print("data = ", data_integer, ", type = ",type(data_integer))
print("data = ", data_boolean, ", type = ",type(data_boolean))
print("data = ", data_float, ", type = ",type(data_float))
