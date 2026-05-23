import hashlib
from utils.display import print_header, print_result, print_separator

# ─────────────────────────────────────────────────────
# HASHING LAB - Main Menu
# ─────────────────────────────────────────────────────

def hashing_lab():
    is_running = True
    while is_running:
        print_header("HASHING LAB")
        print("\n  Select a feature:")
        print("  1. Hash Generator")
        print("  2. Algorithm Comparator")
        print("  3. Avalanche Effect Demo")
        print("  4. File Integrity Checker")
        print("  5. Collision Resistance Explainer")
        print("  0. Back to Main Menu")
        print_separator()

        choice = input("  Enter your choice: ")

        if choice == "1":
            hash_generator()
        elif choice == "2":
            algorithm_comparator()
        elif choice == "3":
            avalanche_effect()
        elif choice == "4":
            file_integrity_checker()
        elif choice == "5":
            collision_explainer()
        elif choice == "0":
            is_running = False
        else:
            print("\n  Invalid choice. Try again.")


# ─────────────────────────────────────────────────────
# Feature 1 — Hash Generator
# ─────────────────────────────────────────────────────

def hash_generator():
    print_header("HASH GENERATOR")
    
    text = input("  Enter text to hash: ")
    
    print("\n  Select algorithm:")
    print("  1. MD5")
    print("  2. SHA-1")
    print("  3. SHA-256")
    print("  4. SHA-512")
    print_separator()
    
    algo = input("  Your choice: ")
    
    if algo == "1":
        hash_value = hashlib.md5(text.encode()).hexdigest()
        algo_name = "MD5"
        bits = "128"
    elif algo == "2":
        hash_value = hashlib.sha1(text.encode()).hexdigest()
        algo_name = "SHA-1"
        bits = "160"
    elif algo == "3":
        hash_value = hashlib.sha256(text.encode()).hexdigest()
        algo_name = "SHA-256"
        bits = "256"
    elif algo == "4":
        hash_value = hashlib.sha512(text.encode()).hexdigest()
        algo_name = "SHA-512"
        bits = "512"
    else:
        print("\n  Invalid choice.")
        return

    print_separator()
    print_result("Algorithm", algo_name)
    print_result("Input", text)
    print_result("Hash", hash_value)
    print_result("Length", f"{bits} bits")
    print_separator()


# ─────────────────────────────────────────────────────
# Feature 2 — Algorithm Comparator
# ─────────────────────────────────────────────────────

def algorithm_comparator():
    print_header("ALGORITHM COMPARATOR")
    
    text = input("  Enter text to compare: ")

    md5 = ["MD5", "128", hashlib.md5(text.encode()).hexdigest()]
    sha1 =  ["SHA-1", "160", hashlib.sha1(text.encode()).hexdigest()]
    sha256 = ["SHA-256", "256", hashlib.sha256(text.encode()).hexdigest()]
    sha512 = ["SHA-512", "512", hashlib.sha512(text.encode()).hexdigest()]
    hashalgo = [md5, sha1, sha256, sha512]

    for result in hashalgo:
        algoinfo = f"{result[0]:<8} ({result[1]} bits)"
        print_result(algoinfo,result[2])


    print_separator()


# ─────────────────────────────────────────────────────
# Feature 3 — Avalanche Effect Demo
# ─────────────────────────────────────────────────────

def avalanche_effect():
    print_header("Avalanche Effect")
    print("\n  The Avalanche Effect: even a tiny change in input")
    print("  produces a completely different hash output.")
    print("  Enter two similar inputs below to witness this.\n")
    user_input1  = input("Enter the Input1: ")
    user_input2 = input("Enter the Input2: ")
    print_result("Input1", user_input1)
    print_result("Hash1", hashlib.sha256(user_input1 .encode()).hexdigest())
    print_result("Input2", user_input2)
    print_result("Hash2", hashlib.sha256(user_input2.encode()).hexdigest())
    print_separator()
    print("  One character changed. Hash changed completely. This is the Avalanche Effect.")

    print_separator()

# ─────────────────────────────────────────────────────
# Feature 4 — File Integrity Checker
# ─────────────────────────────────────────────────────

def file_integrity_checker():
    print_header("File Integrity Checker")
    # Provide the input file here to check the integrity 
    file_path = input("  Enter file path: ")

    print("\n  1. Hash a file and save")
    print("  2. Verify a file against saved hash")
    print_separator()
    sub_choice = input("  Your choice: ")

    # open the input file and generate the hash
    with open(file_path, "rb") as file:
        content = file.read()
    current_hash = hashlib.sha256(content).hexdigest()

    if sub_choice == "1":
        #Save the hash for input file
        hashfilepath = file_path + ".hash"
        with open(hashfilepath,"w") as file:
            file.write(current_hash)
        print_result("Hash saved to", hashfilepath)
        print_result("SHA-256 Hash", current_hash[:32] + "...")
        
    elif sub_choice == "2":
        # Read the Stored Hash
        hashfilepath = file_path + ".hash"
        with open(hashfilepath, "r") as file:
            stored_hash = file.read()

        # Compare the Stored Hash with the Current Hash
        print_result("Stored Hash", stored_hash[:32] + "...")
        print_result("Current Hash", current_hash[:32] + "...")
        if(stored_hash == current_hash):
            print_result("Status", "✓ FILE INTEGRITY VERIFIED")
        else:
            print_result("Status", "✗ TAMPERED - HASHES DO NOT MATCH")
        

    else:
        print("\n  Invalid choice. Please select 1 or 2.")

    print_separator()
    


# ─────────────────────────────────────────────────────
# Feature 5 — Collision Resistance Explainer
# ─────────────────────────────────────────────────────

def collision_explainer():
    pass