import re
import math
import json
# This square is custom to an ARG
# TODO: choose which letter gets left out: currently its 'y', normally its 'j'

class Nihilist:
   
  def __init__(self, poly_key, nihil_key):
      self.poly_key = poly_key
      self.nihil_key = nihil_key

      self.square = self.__create_square()
      self.square_dict = self.__create_square_dict()
  
  def __create_square(self):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXZ' # missing 'Y'

    square = []
    alpha = [_ for _ in alphabet]

    for c in self.poly_key[::-1]:
       alpha.remove(c)
       alpha.insert(0, c)
      
    for i in range(0, 25, 5):
       square.append([alpha[i], alpha[i+1], alpha[i+2], alpha[i+3], alpha[i+4]])
    
    return square
  
  def __create_square_dict(self):
    square_dict = {}

    for r in range(len(self.square)):
      for c in range(len(self.square[r])):
        square_dict[self.square[r][c]] = (r, c) 

    return square_dict

  def _generate_key(self, inp, key):
    enc_key = [((self.square_dict[x.upper()][0] + 1) * 10) + self.square_dict[x.upper()][1] + 1 for x in key]

    if len(inp) != len(enc_key):
        for i in range(len(inp) - len(enc_key)):
            enc_key.append(enc_key[i % len(enc_key)])

    return enc_key
	
  def encrypt(self, user_input): 
    # Format input string
    enc_string = re.sub(r'[^a-zA-Z]', '', user_input)
    enc_string = [((self.square_dict[x.upper()][0] + 1) * 10) + self.square_dict[x.upper()][1] + 1 for x in enc_string]

    # Convert key
    encrypted_key = self._generate_key(enc_string, self.nihil_key)

    # Combine string & key
    result = ''
    for i in range(len(enc_string)):
      result += str(enc_string[i] + encrypted_key[i]) + ' '

    return result

  def decrypt(self, user_input):
    if not re.match('^[0-9\s]*$', user_input):
       return 'ERROR: Input is not valid.'
    
    formatted_string = [int(x) for x in user_input.split()]
    encrypted_key = self._generate_key(formatted_string, self.nihil_key)

    result = []
    for i in range(len(formatted_string)):
      raw_code = formatted_string[i] - encrypted_key[i]
      this_tup = (math.floor(raw_code / 10) - 1, (raw_code % 10) - 1)
      if this_tup[0] >=0 and this_tup[0] < 5 and this_tup[1] >= 0 and this_tup[1] < 5:
        result.append(self.square[this_tup[0]][this_tup[1]])
      else:
         return 'none'

    return ''.join(result)


# -- "BRUTEFORCE" --

target = './text files/target.json'
with open(target) as json_data:
   data = json.load(json_data)

res_file = open('./text files/target_results.txt', 'a')

for key in data['keys']:
   nihil = Nihilist('', key)

   for seq in data['sequences']:
      res_file.write(nihil.decrypt(seq) + '\n')
      

res_file.close()