# Interactive Command Line Directory Navigator (`icd`)

`icd` is an interactive command-line directory navigator for Unix-like systems, built using Python. This tool allows you to navigate through your file system in a visually intuitive way, using keyboard inputs such as arrow keys and `Enter` to move between directories. It's especially useful for users who prefer a terminal-based workflow but want a more interactive experience.

## Features
- **Interactive Navigation**: Use arrow keys to navigate up, down, left, and right through directories.
- **Visual Feedback**: The current directory is highlighted, and long directory paths are truncated for a cleaner display.
- **Signal Handling**: Gracefully handle interruptions like `Ctrl+C` with custom exit messages.
- **Automatic Directory Change**: Upon selecting a directory, `icd` changes to the chosen directory.

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
- Copy the Python script to `/usr/local/lib/icd/`.
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

## Example

```bash
$ icd
/home/user/[projects]
[ ] project1
[*] project2
[ ] project3
```

Navigate to `project2` by pressing the down arrow and hit `Enter`. Your working directory will change to `/home/user/projects/project2`.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Author

[Pedram Aliniaye Asli](https://github.com/pedram-aliniaye-asli)
