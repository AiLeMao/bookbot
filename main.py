def main():
    # Define the path to the file
    path_to_file = "books/frankenstein.txt"

    # Open the file and read its contents
    with open(path_to_file) as f:
        file_contents = f.read()

    # Print the contents to the console
    print(file_contents)

# Call the main function to execute the program
if __name__ == "__main__":
    main()