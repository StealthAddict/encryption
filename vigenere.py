
class Vigenere:

    def __init__(self, key, user_inp):
        self.user_input = user_inp
        self.key = self._generate_key(key)

    """
        _generate_key lengthens key to accomodate the length of string.
    """
    def _generate_key(self, key):
        gen_key = [x.upper() for x in key]

        if len(self.user_input) != len(gen_key):
            for i in range(len(self.user_input) - len(gen_key)):
                gen_key.append(gen_key[i % len(gen_key)])

        return("".join(gen_key))
        

    def encrypt(self):
        encrypted_string = []
        key = self.key
        string = self.user_input
        
        for i in range(len(string)):
            cur = ord(string[i])

            if string[i].isalpha():
                cur = (ord(string[i].upper()) + ord(key[i])) % 26

                if string[i].islower():
                    cur += ord('a')
                else:
                    cur += ord('A')
            else:
                key = key[:i] + string[i] + key[i:]
            
            encrypted_string.append(chr(cur))
        return("".join(encrypted_string))


    def decrypt(self):
        decrypted_string = []
        key = self.key
        string = self.user_input

        for i in range(len(string)):
            cur = ord(string[i])

            if string[i].isalpha():
                cur = (ord(string[i].upper()) - ord(key[i]) + 26) % 26

                if string[i].islower():
                    cur += ord('a')
                else:
                    cur += ord('A')
            else:
                key = key[:i] + string[i] + key[i:]

            decrypted_string.append(chr(cur))
        return("" . join(decrypted_string))