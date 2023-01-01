
#DEFIS MATRIX


#----------1ere implementation---------------

matrix=[
['7','T','h','i','s','$','#','^'],
['i','s','%',' ','M','a','t','r'],
['3','i','x',' ',' ','#','%',' '],

]

def decripteur(matrix):
    message=''
    count=0
    for colonne in matrix:
        for i in colonne:
            if i.isalpha():
             message+=i
            elif i.isdigit():
             pass
            else:
                count+=1
                #print(f"{i} n'est pas alpha")
                 #print(f"count : {count}")
                if count==2:
                    message+=' '
                    count=0
    return message

message=decripteur(matrix)
print(message)







#-------2eme implementation------------------
'''
matrix="7This$#1is% Matr3ix#"
liste_matrix=list(matrix)
message=''
count=0
for i in liste_matrix:
    if i.isalpha():
        message+=i
    elif i.isdigit():
        pass
    else:
        count+=1
        if count==2:
            message+=' '
            count=0

print(f"le message est : {message}")
#print(f"le message est : This is Matrix")
'''