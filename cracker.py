import hashlib

def crack_hash(hash_to_crack, wordlist_path):
    with open(wordlist_path, 'r') as f:
        for word in f:
            word = word.strip()
            hashed_word = hashlib.md5(word.encode()).hexdigest()
            if hashed_word == hash_to_crack:
                print(f"[+] Password found: {word}")
                return
    print("[-] Password not found.")

# Example usage:
# Replace with your own hash and wordlist path
hash_input = input("Enter MD5 hash: ")
wordlist_file = input("Enter wordlist path: ")
crack_hash(hash_input, wordlist_file)
