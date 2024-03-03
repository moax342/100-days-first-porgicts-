import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o'
         ,'p','q','r','s','t','u','v','w','x','y','z']
numbers=['1','2','3','4','5','6','7','8','9']
symbles=['!','@','#','$','%','&','*','(',')']
print("wilcome to the password genrator ")
n_letters=int(input("how many letter do you want "))
n_numbers=int(input("how many number do you want"))
n_symbles=int(input("how many symbel do you want"))

password=''
for let in range(0,n_letters):
    password+=random.choice(letters)
    if let<n_numbers:
        password+=random.choice(numbers)
    if let <n_symbles:
        password+=random.choice(symbles)
    
print(f'your password is : {password}')
