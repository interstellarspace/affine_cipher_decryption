#!/usr/bin/python
import math

'''Read text from the file'''
def read_text_from_file(filename):
    f = open(filename,'r')
    text = f.readlines()
    text = "".join(text)
    return text.strip()

'''Transform text into array'''
def text_to_list(text):
    l = list(text)
    return l

'''Print array into regular string'''
def print_list(l):
    print(''.join(l))

'''Get int value of a letter'''
def let_int(letter):
    return ord(letter)

def Extended_Eucledian_Alg(num, mod):
    qi_list = list()
    remainder_list = list()
    #i_list = list()
    gcd_for_inverse(num, mod, qi_list, remainder_list)
    #print(qi_list)
    #print(remainder_list)
    inv = calculate_inverse(qi_list)
    if inv < 0:
        inv = inv % mod
    if remainder_list[len(remainder_list)-2] == 1.0:
        return inv
    else:
        #print("Error: num '%' mod " + str(mod) + " has not multiplicative inverse")
        return( str(num) + " mod " + str(mod) + " has no multiplicative inverse.")
    
def gcd_for_inverse(a,b, qi_list, remainder_list):
    if b == 0:
        return a
    else:
        qi_list.append(math.trunc(a / b))
        remainder_list.append(a % b)
        return gcd_for_inverse(b, a % b, qi_list, remainder_list)

def calculate_inverse(qi_list):
    xjold = 0
    xjnew = 1
    for x in range(1,len(qi_list)-1):
        inv = xjold - (qi_list[x] * xjnew)
        xjold = xjnew
        xjnew = inv    
    return inv


class Text_Frequencies:
    cipher = ''
    current_freq_list = list()

    def __init__(self, file_name):
        self.cipher = read_text_from_file(file_name)
        print("Using file: " + file_name)
    
    def get_datagram_frequencies(self, length):         #ASCII [0 to 255]
        #print(self.cipher)
        t = self.cipher.lower()                         #A = 65 Z = 90
        #print(t)
        t = t.replace(" ","")
        t = t.replace('\n',"")
        t = t.replace('\t',"")
        freq_list = list()                              #a = 97 z = 122
        gram_list = list()
        gram_freq_list = list()
        
        i = 0
        #print(t)
        #print(len(t))
        while (i + length) <= len(t):
            curr_gram = t[i:i+length]
            if curr_gram not in gram_list:
                gram_list.append(curr_gram)
                freq_list.append(0)
            ind = gram_list.index(curr_gram,)
            freq_list[ind] += 1
            i += 1
        assert(len(freq_list)==len(gram_list))
        for l in gram_list:
            ind2 = gram_list.index(l,)
            gram_freq_list.append(self.Datagram_Freq(l, freq_list[ind2],float(freq_list[ind2])/sum(freq_list)))
        #print (gram_list)
        #print (freq_list)
        gram_freq_list = sorted(gram_freq_list, key=lambda Datagram_Freq: Datagram_Freq.freq, reverse=True)
        self.current_freq_list = gram_freq_list
        #print(self.current_freq_list)
        self.__print_frequencies__()
        return gram_freq_list
    
    class Datagram_Freq:
        letter = ''
        freq = 0
        percent = 0
        def __init__(self, l, f, p):
            self.letter = l
            self.freq = f
            self.percent = p

    def __print_frequencies__(self):
        num_sum = 0
        per_sum = 0
        print("Ciphertext:\n" + self.cipher)
        print("\n\tFREQUENCIES/ANALYSIS")
        for data in self.current_freq_list:
            
            num_sum += data.freq
            per_sum += data.percent
            i_x = int(data.percent*100)
            print(data.letter + ": " + str(data.freq) + " " + "{0:.2f}%".format(data.percent*100) + "\t" + "x"*i_x*2)
        print("Sum of frequencies: " + str(num_sum))
        print("Sum of percentage: " + "{0:.0f}%\n".format(per_sum*100))


def Decrypt_Affine_Cipher(filename, a, b):
    
    ciphertext = read_text_from_file(filename)  #get text from file
    print('Ciphertext:\t' + ciphertext)       #print ciphertext
    ciphertext = text_to_list(ciphertext.lower())
    s = ''
    print("Decryption using: a = " + str(a) + ", b = " + str(b))
    m_inverse = Extended_Eucledian_Alg(a, 26)
    for l in ciphertext:
        decrypted_letter = (((((ord(l)) % 97) - b) * m_inverse) % 26) + 97
        s = s + chr(decrypted_letter)
    return s
