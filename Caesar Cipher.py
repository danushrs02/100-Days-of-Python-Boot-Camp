
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



#CASER function for encryption and decryption
def caesar(original_text, shift_amount, encode_or_decode):
    
    cipher=''

    
    if encode_or_decode == "decode":
            shift_amount *= -1
    
        
    for i in original_text:

        if i not in alphabet:
            cipher+=i
            
        else:
            position = alphabet.index(i)+shift_amount

            position %= len(alphabet)

            cipher += alphabet[position]

        
    print(f"HERE IS THE {encode_or_decode}d version:{cipher}")
          
should_continue=True

while should_continue:
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    text = input("Type your message:\n").lower()

    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text,encode_or_decode=direction,shift_amount=shift)

    decide=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()


    if decide == 'no':

        should_continue=False

        print("GOODBYE")




  
