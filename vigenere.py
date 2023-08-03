class Vigenere(object):
    def __init__(self, key):
        assert(type(key) == type("Hello, world!"))
        assert(key.isalpha())
        self.key = key
        self.key = self.key.lower()
        self.key_len = len(key)
        self.chr2num = {}
        for i in range(26):
            self.chr2num[chr(ord('a')+i)] = i
        print(self.chr2num)

    def encrypt(self, plaintext):
        assert(type(plaintext) == type("Hello, world!"))
        assert(plaintext.isalpha())
        plaintext = plaintext.lower()
        ciphertext = ""
        for i in range(0, len(plaintext), self.key_len):
            for j in range(self.key_len):
                tmp = i + j
                if tmp < len(plaintext):
                    ciphertext += chr((self.chr2num[plaintext[tmp]] + self.chr2num[self.key[j]]) % 26 + ord('a'))
                else:
                    break
        print(ciphertext)

if __name__ == "__main__":
    v = Vigenere("tvtsidl")

    v1 = Vigenere("tvtddfm")

        

        
