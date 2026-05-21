from utils.display import print_result, print_separator, print_header

def main():
    print_header("CRYPTOLAB TERMINAL")
    is_running = True
    while is_running:
        print("\n  Select a module:")
        print("  1. Hashing Lab")
        print("  2. Symmetric Encryption  [coming soon]")
        print("  3. Asymmetric Encryption [coming soon]")
        print("  4. Digital Signatures    [coming soon]")
        print("  5. Certificates          [coming soon]")
        print("  6. PKI Simulator         [coming soon]")
        print("  0. Exit")
        print_separator()
        choice = input("  Enter your choice: ")

        if choice == "1":
            pass  # call hashing module here
        elif choice == "0":
            is_running = False
            print("\n  Goodbye. Stay secure.")
        else:
            print("\n  Invalid choice. Try again.")


if __name__ == "__main__":
    main()