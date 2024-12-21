def caesar_cipher(text, shift, mode):
    result = ""
    if mode == "decrypt":
        shift = -shift
    
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result += new_char
        else:
            result += char
    
    return result

def main():
    print("Caesar Cipher Program")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Choose an option (1 or 2): ")
    
    if choice == "1":
        mode = "encrypt"
    elif choice == "2":
        mode = "decrypt"
    else:
        print("Invalid choice! Exiting.")
        return
    
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value (integer): "))
    
    result = caesar_cipher(text, shift, mode)
    print(f"The resulting text is: {result}")

if __name__ == "__main__":
    main()