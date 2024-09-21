```markdown
# SSH Bruteforce Tool

This Python script is designed to brute-force SSH login credentials by attempting various passwords from a given password list. It takes inspiration from tools like `hydra` and allows users to specify the host, username, and password file via command-line arguments.

## Features

- Attempts SSH login using a specified username and a list of passwords.
- Prints whether each password is valid or invalid.
- Stops when a valid password is found.
- Mimics command-line usage of common tools like `hydra`.

## Requirements

Before running the script, ensure you have the following dependencies installed:

- **pwntools**: The script uses the `ssh` module from `pwntools` for SSH connection attempts.
- **paramiko**: The script handles SSH authentication errors using `paramiko`.

You can install these dependencies via pip:

```bash
pip install pwntools paramiko
```

## Usage

### Command-Line Arguments

The script accepts the following command-line arguments:

- `-H` or `--host`: The target SSH host (IP address or domain).
- `-l` or `--login`: The username for the SSH login attempt.
- `-P` or `--passwords`: A file containing a list of passwords to attempt.

### Example

To run the script, use the following command:

```bash
python ssh_bruteforce.py -H <host> -l <username> -P <password-file>
```

For example, if you're trying to brute-force SSH login for the host `127.0.0.1`, with the username `notroot` and a password list in `ssh-common-passwords.txt`, run:

```bash
python ssh_bruteforce.py -H 127.0.0.1 -l notroot -P ssh-common-passwords.txt
```

### Output

The script will print each password attempt and whether it was valid or invalid. If a valid password is found, it will stop further attempts and display the correct password.

Example output:

```bash
[0] Attempting password: 'password123'
[X] Invalid password!
[1] Attempting password: 'admin'
[X] Invalid password!
[2] Attempting password: 'letmein'
[>] Valid password found: 'letmein'!
```

## Notes

- **Legal Disclaimer**: This script is intended for educational purposes only. Ensure you have proper authorization to brute-force the target SSH service before using this tool. Unauthorized access to computer systems is illegal.
  
- Make sure the password list (`.txt` file) is properly formatted, with one password per line.

## License

This project is open-source and available under the MIT License.

```

This `README.md` provides a comprehensive guide on how to install, use, and run the script while also emphasizing legal disclaimers and including an example for clarity.
