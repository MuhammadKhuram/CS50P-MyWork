# THE UNIVERSAL FILE RENAMER
#### Video Demo: (https://youtu.be/feIUsTAEIh8)
#### Description:

### Why I Built This Project
I decided to build the Universal File Renamer because I often find myself with folders full of messy files. For example, when I download papers for university or save images from the internet, they all have different naming styles. Some use spaces, some use underscores, and others use dashes. This makes my folders look very disorganized and hard to read. I wanted to create a tool where I could just give a folder path and have every file renamed into one clean style that I choose. My goal was to make a program that is smart enough to understand different naming formats and turn them into a professional look instantly.

### How the Program Works
My program is a command-line tool. This means you run it from the terminal window. I designed the program to take the folder path as an "argument" right when you start it. Once the program starts, I display a clear menu with five different naming styles for the user to pick from:
1. **snake_case**: Everything is lowercase and words are joined by underscores.
2. **kebab-case**: Everything is lowercase and words are joined by dashes.
3. **Title Case**: The first letter of every word is capitalized with spaces in between.
4. **UPPERCASE**: All letters are made big with spaces in between.
5. **lowercase**: All letters are made small with spaces in between.

I also wanted the program to look like a real, professional application. To do this, I used a library called `pyfiglet` to create a large ASCII art title at the start. I also used `termcolor` to add colors, like green for success messages and yellow for the menu borders. This makes the tool much more fun to use than a plain black-and-white script.

### The Files in My Project
I have organized my project into a few specific files to follow the CS50 requirements:
- **`project.py`**: This is the main file where I wrote all my logic. It contains the `main` function, which handles the user's menu choice and renames the files. It also has my three custom functions: `get_file_parts`, `split_name`, and `apply_style`.
- **`test_project.py`**: I used this file to write my automated tests. By using `pytest`, I can make sure that my functions work perfectly every time I change the code. I wrote tests to check if names are split correctly and if the styles are applied right.
- **`requirements.txt`**: Since I used extra libraries like `pyfiglet` and `termcolor`, I created this file. It allows any other user to install everything they need with one simple command.
- **`files/`**: I created this folder inside my project to keep some dummy PDF and text files. This let me test my program over and over again without accidentally renaming any of my important personal documents.

### My Design Choices
I spent a lot of time thinking about how to make this program work well. Here are some of the design choices I made and why:

**1. Using Regular Expressions (Regex) for Splitting**
I realized early on that just using a simple `.split(" ")` would not work. If a file was named `my-cool_file.txt`, a normal split would fail because it wouldn't see the dash or the underscore. I decided to use the `re` module because it allows me to look for multiple separators at the same time. I wrote a pattern that tells Python: "Split this name whenever you see a space, an underscore, OR a dash." This turns any messy name into a clean list of words that I can easily rebuild into a new style.

**2. Protecting the File Extension**
I was very worried that if I turned a filename into uppercase, I might accidentally turn `.pdf` into `.PDF`. I know that some computers can be sensitive about file extensions. To solve this, I wrote a function called `get_file_parts`. I used `os.path.splitext` to "cut" the extension off before I do any renaming. I change the name part, and then I glue the extension back on at the very end. I also decided to force all extensions to be lowercase because I think it makes the folder look much more consistent.

**3. Choosing Command Line Arguments**
I chose to use `sys.argv` for the folder path. I like this because it makes the tool feel fast. Instead of waiting for the program to open and then asking me for the path, I can just type it in the first command. I also added a safety check using `os.path.isdir`. If I make a typo in the path, the program tells me "Error: Directory not found" instead of crashing with a long, confusing error message.

**4. Adding Spaces for Readability**
In my first version, the UPPERCASE option joined words together with no spaces, like `MYFILE.pdf`. I found this very hard to read. I decided to change my `apply_style` function so that it joins the words with a space. Now, it creates names like `MY NEW FILE.pdf`. This looks much better to the human eye. After making this change, I had to update my tests in `test_project.py` to make sure they expected a space too. This taught me a great lesson about how tests and code need to stay in sync.

### Conclusion
I am very proud of this project. It started as a simple idea, but I learned a lot about how to handle the file system and how to process strings safely. I think this tool is very useful, and I plan to keep using it on my own computer to keep my university work organized!
