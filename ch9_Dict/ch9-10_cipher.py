abc='abcdefghijklmnopqrtsuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ'
encry_dict:{}
front=abc[:3]
end=abc[3:]
subText=end+front
encry_dict=dict(zip(subText,abc))
print(encry_dict)
msgText='White White'
cipher=[]
for i in msgText:
    cipher.append(encry_dict[i])
cipherText=''.join(cipher)
print(msgText,cipherText)
