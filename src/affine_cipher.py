""" Affine-Cipher will encrypt a selected file

An affine cipher is applied to encrypt a message whose (unencrypted) message is coded using A = 1, B = 2, ..., Y = 25, Z = 26'
"""
FILE_PATH = 'example_text.txt'

alpha_dict = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6,
              'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10, 'K' : 11, 'L' : 12,
              'M' : 13, 'N' : 14, 'O' : 15, 'P' : 16, 'Q' : 17, 'R' : 18,
              'S' : 19, 'T' : 20, 'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24,
              'Y' : 25, 'Z' : 26, 
            }

upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def affine_cipher(alpha, beta):
    with open(FILE_PATH, 'r') as f1:
            with open('encrypted_file.txt', 'w') as f2:
                for c in f1.read():
                    if (c.upper() in alpha_dict.keys()):
                        f2.write(upper_alphabet[((alpha*alpha_dict[c.upper()] + beta) % 26)])
                        print((alpha*alpha_dict[c.upper()] + beta) % 26)
                    else:
                        f2.write(c)

    



def main():
    print("Affine cypher: f(x) = [alpha*x + beta]mod26")
    alpha = int(input("Enter a value for alpha: "))
    beta = int(input("Enter a value for beta: "))
    affine_cipher(alpha, beta)

    print(((alpha*3 + beta) % 26))

if __name__ == '__main__':
    main()