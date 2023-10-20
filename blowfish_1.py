from constants import constant
class Blowfish:
  def __init__(self,input_string):
    c=constant()
    self.__p = c.p_box

    self.__s=c.s_box
    
    self.__key = []
    if len(input_string) > 56:
      input_string=input_string[:56]
    for i in range(0, len(input_string), 4):
      substring = input_string[i:i+4]
      while len(substring) < 4:
          substring += '0'
      hex_value = int('0x' + ''.join(format(ord(char), '02x') for char in substring), 16)
      self.__key.append(hex_value)
    self.subkeyGeneration()
  
  
  def subkeyGeneration(self):
    for i in range(18):
      self.__p[i]=self.__p[i]^self.__key[i%len(self.__key)]
    key_temp=0
    for i in range(0,18,+2):
      key_temp=self.blowFish_encrypt(key_temp)
      self.__p[i]=key_temp>>32
      self.__p[i+1]=key_temp & 0xffffffff 
  
  def F(self,L):
    s_box=self.__s[0][L>>24]
    s_box=(s_box+self.__s[1][L>>16&0xff])%2**32
    s_box=(s_box^self.__s[2][L>>8&0xff])
    s_box=(s_box+self.__s[3][L&0xff])%2**32
    return s_box

  def blowFish_encrypt(self,data):
    L=data>>32
    R=data & 0xffffffff
    for i in range(16):
       L=self.__p[i]^L
       L1=self.F(L)
       R=R^L1
       L,R=R,L
    L,R=R,L
    R=R^self.__p[16]
    L=L^self.__p[17]
    return (L<<32)^R
  
  def blowFish_decrypt(self,data):
    L=data>>32
    R=data & 0xffffffff
    for i in range(17,1,-1):
       L=self.__p[i]^L
       L1=self.F(L)
       R=R^L1
       L,R=R,L
    L,R=R,L
    R=R^self.__p[1]
    L=L^self.__p[0]
    return (L<<32)^R
    
      
          
        
if __name__=='__main__':
  key=input("Enter the key: ")
  bl=Blowfish(key)
  bl.subkeyGeneration()
  enc=int(input("Enter data to encrypt: "))
  enc_data=bl.blowFish_encrypt(enc)
  print("Encrypted data = ",hex(enc_data))
  print("Decrypted data = ",bl.blowFish_decrypt(enc_data))