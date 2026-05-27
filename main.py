from utils.display import print_result, print_separator, print_header
from modules.hashing import hashing_lab
from modules.symmetric import symmetric_lab

def main():
    print_header("CRYPTOLAB TERMINAL")
    is_running = True
    while is_running:
        print("\n  Select a module:")
        print("  1. Hashing Lab")
        print("  2. Symmetric Encryption")
        print("  3. Asymmetric Encryption [coming soon]")
        print("  4. Digital Signatures    [coming soon]")
        print("  5. Certificates          [coming soon]")
        print("  6. PKI Simulator         [coming soon]")
        print("  0. Exit")
        print_separator()
        choice = input("  Enter your choice: ")

        if choice == "1":
            hashing_lab()
        elif choice == "2":
            symmetric_lab()
        elif choice in ["3", "4", "5", "6"]:
            print("\n  This module is coming soon. Stay tuned.")
        elif choice == "0":
            is_running = False
            print("\n  Goodbye. Stay secure.")
        else:
            print("\n  Invalid choice. Try again.")


if __name__ == "__main__":
    main()