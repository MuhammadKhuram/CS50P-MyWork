import os
import sys
import re
import pyfiglet
from termcolor import cprint

def main():
    # Generate the ASCII art
    title = pyfiglet.figlet_format("FILE RENAMER", font="small") # big doom
    cprint(title, 'green', attrs=['bold'])

    # You can also use plain characters to build the rest of your menu box
    cprint("=" * 54, 'yellow')
    cprint("           WELCOME TO THE FILE RENAMER", 'white', attrs=['bold'])
    cprint("=" * 54, 'yellow')

    # 1. Check for command line argument
    if len(sys.argv) < 2:
        sys.exit("Usage: python project.py <directory_path>")

    path = sys.argv[1]
    if not os.path.isdir(path):
        sys.exit("Error: Directory not found.")

    # 2. Display the menu
    cprint("\n1. snake_case")
    cprint("2. kebab-case")
    cprint("3. Title Case")
    cprint("4. UPPERCASE")
    cprint("5. lowercase")

    choice = input("\nSelect a naming style (1-5): ")
    styles = {"1": "snake", "2": "kebab", "3": "title", "4": "upper", "5": "lower"}

    if choice not in styles:
        sys.exit("Invalid choice.")

    style = styles[choice]

    # 3. Process files
    files = os.listdir(path)
    count = 0

    for filename in files:
        # Skip hidden files
        if filename.startswith('.'):
            continue

        # Function 1: Separate name and extension
        name_part, extension = get_file_parts(filename)

        # Function 2: Split the name into words
        words = split_name(name_part)

        # Function 3: Apply the chosen style
        new_name = apply_style(words, style)

        # Reconstruct the full filename
        final_filename = new_name + extension

        # Rename the actual file
        old_path = os.path.join(path, filename)
        new_path = os.path.join(path, final_filename)

        os.rename(old_path, new_path)
        count += 1

    print(f"\nSuccess! Renamed {count} files.")


def get_file_parts(filename):
    """Separates filename from extension and returns them as a tuple."""
    # Use os.path.splitext to handle dots correctly
    name, ext = os.path.splitext(filename)
    return name, ext.lower()


def split_name(name):
    """Takes a filename string and returns a list of words using regex."""
    # This regex splits by space, underscore, or dash
    words = re.split(r'[ _-]+', name)
    # Remove any empty strings if they exist
    return [word for word in words if word]


def apply_style(words, style):
    """Joins a list of words into the requested naming style."""
    if style == "snake":
        return "_".join(words).lower()
    elif style == "kebab":
        return "-".join(words).lower()
    elif style == "title":
        return " ".join(word.capitalize() for word in words)
    elif style == "upper":
        return " ".join(words).upper()  # Changed "" to " "
    elif style == "lower":
        return " ".join(words).lower()  # Changed "" to " "
    return " ".join(words)

if __name__ == "__main__":
    main()
