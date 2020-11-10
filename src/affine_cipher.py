""" Affine-Cipher will encrypt a selected file

An affine cipher is applied to encrypt a message whose (unencrypted) message is coded using A = 1, B = 2, ..., Y = 25, Z = 26'
"""
FILE_PATH = 'test.txt'

def affine_cipher(alpha, beta):
    lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # example letter H
    print((alpha*8 + beta) % 26)

    with open(FILE_PATH, 'r') as f1:
        f1.read()

    
    with open('encrypted_file.txt', 'w') as f2:
        f2.write('something here')


def main():
    print("Affine cypher: f(x) = [alpha*x + beta]mod26")
    alpha = int(input("Enter a value for alpha: "))
    beta = int(input("Enter a value for beta: "))
    affine_cipher(alpha, beta)




if __name__ == '__main__':
    main()