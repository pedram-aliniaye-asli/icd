# Interactive Command Line Directory Navigator (`icd`)

`icd` is an interactive command-line directory navigator for Unix-like systems, built using Python. This tool allows you to navigate through your file system in a visually intuitive way, using keyboard inputs such as arrow keys and `Enter` to move between directories. It's especially useful for users who prefer a terminal-based workflow but want a more interactive experience.

## Features
- **Interactive Navigation**: Use arrow keys to navigate up, down, left, and right through directories.
- **Visual Feedback**: The current directory is highlighted, and long directory paths are truncated for a cleaner display.
- **Signal Handling**: Manage the Ctrl+C interruption to prevent abrupt termination.
- **Automatic Directory Change**: Upon selecting a directory, `icd` changes to the chosen directory.
- **Absolute Path Input:** Start the navigator from a specific absolute path by passing it as an argument. If no argument is provided, the navigator starts from the current working directory.
## Installation

Follow the steps below to install the `icd` command on your system:

1. **Clone the Repository**:
   First, clone the repository to your local machine using:
   ```bash
   git clone https://github.com/pedram-aliniaye-asli/icd.git
   ```

2. **Navigate to the Directory**:
   Change to the directory where the repository was cloned:
   ```bash
   cd icd
   ```

3. **Make the Install Script Executable**:
   Add executable permissions to the install.sh script by running the following command:
   ```bash
   chmod +x install.sh
   ```

4. **Run the Install Script**:
   Execute the `install.sh` script to install the `icd` command:
   ```bash
   ./install.sh
   ```
   Note: You will need sudo permissions to run the install.sh script as it involves copying files to system directories and modifying the shell configuration.

5. **Verify the Installation**:
   After the installation, you can start using the `icd` command to navigate your directories. Simply type:
   ```bash
   icd 
   ```

This installation script will:
- Copy the bash script to `/usr/local/bin` and make it executable.
- Copy all Python scripts `/usr/local/lib/icd/`.
- Create a bookmarks directory (`~/.local/share/icd`) and initialize a `bookmarks.json` file if it doesn't exist.
- Add an alias for `icd` to your `.bashrc` file.
- Reload your shell configuration.

## Usage

- **Navigation**:
  - **Right Arrow (`→`)**: Enter a directory.
  - **Left Arrow (`←`)**: Go back to the parent directory.
  - **Up Arrow (`↑`)**: Move up the directory list.
  - **Down Arrow (`↓`)**: Move down the directory list.
  - **Enter**: Confirm the directory selection and exit the navigator.

- **Exiting**:
  - **Ctrl+C**: Exit the navigator gracefully.
    
- **Absolute Path**:
   To start the navigator from a specific directory, pass the absolute path as an argument:
   ```
   icd /path/to/directory
   ```
   If no argument is provided, the navigator defaults to the current working directory.

- **Bookmarks**
   - **Saving Bookmarks**
       You can now save your current directory as a bookmark for easy future access. The bookmarks are stored in a JSON file for easy management and retrieval.

     ```Ctrl + D```
       Save the current directory as a bookmark. You'll be prompted to enter a name for the bookmark.

   - **Loading Bookmarks**
        Quickly navigate to a saved directory bookmark. The saved bookmarks can be accessed from the JSON file.

     ```Ctrl + B```
        Load a saved bookmark. You will be asked to enter the name of the bookmark you wish to load.
## Example

- **Starting from the Current Directory**:
  
   ```bash
   $ icd
   /home/user/[projects]
   [ ] project1
   [*] project2
   [ ] project3
   ```
   Navigate to `project2` by pressing the down arrow and hit `Enter`. Your working directory will change to `/home/user/projects/project2`.
  
- **Starting from a Specific Path**:
  
   ```bash
   $ icd /home/user/documents
   /home/user/documents
   [ ] reports
   [*] drafts
   [ ] invoices
   ```
   Navigate to `drafts` by pressing the down arrow and hit `Enter`. Your working directory will change to `/home/user/documents/drafts`.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
Copyright (c) 2025 Pedram Aliniaye Asli.

## Author

[Pedram Aliniaye Asli](https://github.com/pedram-aliniaye-asli)
