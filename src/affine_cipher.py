""" Affine-Cipher will encrypt a selected file

An affine cipher is applied to encrypt a message whose (unencrypted) message is coded using A = 1, B = 2, ..., Y = 25, Z = 26'
"""

# file to read from
FILE_PATH = 'test.txt'

ALPHA_DICT = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6,
              'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10, 'K' : 11, 'L' : 12,
              'M' : 13, 'N' : 14, 'O' : 15, 'P' : 16, 'Q' : 17, 'R' : 18,
              'S' : 19, 'T' : 20, 'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24,
              'Y' : 25, 'Z' : 26, 
            }

UPPER_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def affine_cipher(inverse_alpha, beta):
    ciphertext = ''
    with open(FILE_PATH, 'r') as f:
        for c in f.read():
            if (c.upper() in ALPHA_DICT.keys()):
                ciphertext = ciphertext + (UPPER_ALPHABET[(inverse_alpha*(ALPHA_DICT[c.upper()] - beta) % 26) - 1])
            else:
                ciphertext = ciphertext + c
        print(ciphertext)
    return ciphertext

# outputting to a file
def write_to_file(ciphertext):
    with open('encrypted_file.txt', 'w') as f:
        f.write(ciphertext)

def main():
    print("Affine Cipher: f(x) = [inverse_alpha*(x - beta)]mod26")

    while True:
        try:
            inverse_alpha = int(input("Enter a value for inverse alpha: "))
            break
        except ValueError:
            print("incorrect input")
        
    while True:
        try:
            beta = int(input("Enter a value for beta: "))
            break
        except ValueError:
            print("incorrect input")

    write_to_file(affine_cipher(inverse_alpha, beta))

if __name__ == '__main__':
    main()