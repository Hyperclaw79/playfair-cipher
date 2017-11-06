def generate_cipher(key):
   key = ''.join(key.split(' ')) #remove spaces from given key and PF cipher is only for letters. 
   mat=[]
   for c in key.upper():
      if c not in mat:
         mat.append(c)
   alphabet="ABCDEFGHIKLMNOPQRSTUVWXYZ"
   pad = [c for c in alphabet if c not in mat] #List comprehension is more pythonic
   mat = mat + pad
   mat_2D = [mat[i*5:(i+1)*5] for i in range(5)] #condensed into one line
   return mat_2D

def prettify(table):      #For a more appealing display.
    res1 = '[{}]\n'.format(' '.join(table[0]))
    res2 = ''
    for i in range(1,len(table)-1,1):
        res2 = res2 + '|{}|\n'.format(' '.join(table[i]))
    res3 = '[{}]\n'.format(' '.join(table[len(table)-1]))
    res = res1 + res2 + res3
    return res

def find_position(key_matrix,letter):
   x=y=0
   for i in range(5):
      for j in range(5):
         if key_matrix[i][j]==letter:
            x=i
            y=j

   return x,y

################################################################################

def mes2pairs(message):
   message = ''.join(message.split(' ')).upper()
   if len(message)%2 == 1:
      message = message + 'X'
   pair = [list(message[i:i + 2]) for i in range(0, len(message), 2)]
   pair2 = [[l[0],'X'] if l[0] == l[1] else [l[0],l[1]] for l in pair]
   pairs = [''.join(l) for l in pair2]
   pairs = ' '.join(pairs)
   print("\nSplitting your message into the following pairs:\n{}".format(pairs))
   return pair2

def encrypt(message):
   message = mes2pairs(message)
   key_matrix = generate_cipher(key)
   cipher=[]
   for e in message:
      p1,q1=find_position(key_matrix,e[0])
      p2,q2=find_position(key_matrix,e[1])
      if p1==p2:
         if q1==4:
            q1=-1
         if q2==4:
            q2=-1
         cipher.append(key_matrix[p1][q1+1])
         cipher.append(key_matrix[p1][q2+1])    
      elif q1==q2:
         if p1==4:
            p1=-1;
         if p2==4:
            p2=-1;
         cipher.append(key_matrix[p1+1][q1])
         cipher.append(key_matrix[p2+1][q2])
      else:
         cipher.append(key_matrix[p1][q2])
         cipher.append(key_matrix[p2][q1])
   return ''.join(cipher)

##########################################################################

def cip2pairs(cipher):
   pair = [list(cipher[i:i + 2]) for i in range(0, len(cipher), 2)]
   pairs = [cipher[i:i + 2] for i in range(0, len(cipher), 2)]
   pairs = ' '.join(pairs)
   print("\nSplitting your cipher into the following pairs:\n{}".format(pairs))
   return pair   
   
def decrypt(cipher): 
   cipher=cip2pairs(cipher)
   key_matrix=generate_cipher(key)
   plaintext=[]
   for e in cipher:
      p1,q1=find_position(key_matrix,e[0])
      p2,q2=find_position(key_matrix,e[1])
      if p1==p2:
         if q1==4:
            q1=-1
         if q2==4:
            q2=-1
         plaintext.append(key_matrix[p1][q1-1])
         plaintext.append(key_matrix[p1][q2-1])    
      elif q1==q2:
         if p1==4:
            p1=-1;
         if p2==4:
            p2=-1;
         plaintext.append(key_matrix[p1-1][q1])
         plaintext.append(key_matrix[p2-1][q2])
      else:
         plaintext.append(key_matrix[p1][q2])
         plaintext.append(key_matrix[p2][q1])

   count = 0
   pt = []
   for c in plaintext:
      if c == 'X':
         count = count + 1
   if count<2 and count>0:          
      plaintext.remove('X')
   elif count == 0:
      pass
   else:                    #In case there were repeated characters
      for i in range(len(plaintext)):
          if plaintext[i]=='X':
              pt.append(plaintext[i-1])
          else:
              pt.append(plaintext[i])
   output = ''
   if len(pt)!=0:
      output=''.join(pt)
   else:
      output=''.join(plaintext)
   return output.lower()

###########################################################

#key="cipher"
#message="effecttreecorrectapple"
#cipher="FNNFHOODPZCIVGFCHOBIBSPZ"

#key="playfairexample"
#message="Hide the gold in the tree stump"
#>>BMODZBXDNABEKUDMUIXMMOUVIF


print("Welcome to Playfair Cipher.\n")
key=input("Please input the key:\n")
print("\nThe cipher matrix based on your key:\n{}".format(prettify(generate_cipher(key)))) 
order = '3'
while(int(order)>2):
   order = input("What would you like to perform?\n1.Encryption\n2.Decryption\n")
   if int(order)<= 2 and int(order)>= 1:
       break
if int(order) == 1:
   message = input("\nPlease input the message:\n")
   print("\nEncrypting the message:\n{}".format(message))
   print("\nHere is the encrypted text:\n{}".format(encrypt(message)))
else:
   cipher = input("\nPlease input the cipher text:\n")
   print("\nDecrypting the cipher:\n{}".format(cipher))
   print("\nHere is the decrypted text:\n{}".format(decrypt(cipher)))
print("\nThank you for using the Playfair Ciphering Script.")
