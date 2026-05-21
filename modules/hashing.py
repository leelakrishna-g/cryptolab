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
    pass


# ─────────────────────────────────────────────────────
# Feature 3 — Avalanche Effect Demo
# ─────────────────────────────────────────────────────

def avalanche_effect():
    pass


# ─────────────────────────────────────────────────────
# Feature 4 — File Integrity Checker
# ─────────────────────────────────────────────────────

def file_integrity_checker():
    pass


# ─────────────────────────────────────────────────────
# Feature 5 — Collision Resistance Explainer
# ─────────────────────────────────────────────────────

def collision_explainer():
    pass