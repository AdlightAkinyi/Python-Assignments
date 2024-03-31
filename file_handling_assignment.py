

def write_to_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("First line\n")
            file.write("Second line\n")
            file.write("Third line\n")
            print("File created and written successfully.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while writing to file: {e}")
    finally:
        print("Write operation completed.")

def read_and_display():
    try:
        with open("my_file.txt", "r") as file:
            contents = file.read()
            print("Contents of the file:")
            print(contents)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while reading file: {e}")
    finally:
        print("Read operation completed.")

def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Fourth line\n")
            file.write("Fifth line\n")
            file.write("Sixth line\n")
            print("Content appended to the file.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while appending to file: {e}")
    finally:
        print("Append operation completed.")

def main():
    write_to_file()
    print("--------------------")
    read_and_display()
    print("--------------------")
    append_to_file()

if __name__ == "__main__":
    main()


