ALPHA_NUM = list('abcdefghijklmnopqrstuvwxyz')

class A1Z26: 

    def __init__(self, salt=''):
        self.salt = salt


    """
    Helper encryption function.
    Ignores whitespace.
    """
    def _encrypt_string(self, string):
        enc_str = []   

        string = string.split()
        for word in string:
            for letter in word:
                if letter.isalpha():
                    enc_str.append(str(ALPHA_NUM.index(letter.lower()) + 1))
                else:
                    enc_str.append(letter)

            # enc_str.append(' ')  # keep spaces

        return ' '.join(enc_str)

    """
    Custom encryption:
        Input is encrypted with a1z26 then salted with another string of any length
        by adding the a1z26 of the salt to the original input.
    """ 
    def encrypt(self, string):
        result = []

        enc_str = self._encrypt_string(string).split()
        
        if self.salt:
            enc_salt = self._encrypt_string(self.salt).split()
            
            # extend salt to have the same length as the string
            while len(enc_salt) < len(enc_str):
                enc_salt = enc_salt + enc_salt

            for i in range(len(enc_str)):
                result.append(str(int(enc_str[i]) + int(enc_salt[i])))
        
            return ' '.join(result)
        
        return ' '.join(enc_str)


    """
    Helper decryption function.
    """
    def _decrypt_string(self, string):
        decrypted_string = []
        string = string.split()

        for number in string:
            if number.isdigit():
                decrypted_string.append(ALPHA_NUM[int(number) - 1])
            else:
                decrypted_string.append(number)

        return ''.join(decrypted_string)
    
    def decrypt(self, string):
        result = []

        enc_str = string.split()

        if self.salt:
            enc_salt = self._encrypt_string(self.salt).split()

            while len(enc_salt) < len(enc_str):
                enc_salt = enc_salt + enc_salt

            for i in range(len(enc_str)):
                result.append(str(int(enc_str[i]) - int(enc_salt[i])))
        else:
            result = enc_str

        result = self._decrypt_string(' '.join(result))

        return ''.join(result)
