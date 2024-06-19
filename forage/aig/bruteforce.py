'''
Forage AIG Cybersecurity Program
Bruteforce starter template
'''

from zipfile import ZipFile

# Use a method to attempt to extract the zip file with a given password
def attempt_extract(zf_handle, password):
    zf_handle.extractall(pwd=password.encode('ascii'))

def main():
    print("[+] Beginning bruteforce ")
    extracted = False
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            # Iterate through password entries in rockyou.txt
            pwds = (f.read().decode('ascii')).split('\n')
            for pwd in pwds:
                # Attempt to extract the zip file using each password
                try:
                    attempt_extract(zf, pwd)
                    extracted = True
                # Handle correct password extract versus incorrect password attempt)
                except RuntimeError as e:
                    pass
    if not extracted:
        print("[+] Password not found in list")

if __name__ == "__main__":
    main()