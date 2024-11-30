# cPanel Login Tester

A Python script to test login credentials for cPanel accounts across multiple URLs. This tool is designed to simplify testing with clean output for terminal users and detailed logs for debugging.

## Features
- **Cross-Platform:** Works seamlessly on Windows and Linux.
- **Custom Login File:** Specify the path to the login file (`login.txt`) as an argument when running the script.
- **Simple Output:** Displays concise results in the terminal (e.g., `LOGIN SUCCESS`, `TIMEOUT`, or `ERROR`).
- **Detailed Logging:** Saves comprehensive logs to a file (`cpanel_test.log`) for later review.
- **Timeout Handling:** Handles and reports connection timeouts gracefully.
- **Secure Connections:** Utilizes HTTPS for all requests.

## Requirements
- Python 3.8 or higher
- Required libraries: `requests`, `logging`, `argparse`

Install dependencies with:
```bash
pip install -r requirements.txt
```
Usage
Create a login.txt file in the following format:
```arduino
https://example.com:2083|username|password
https://anotherdomain.com:2083|user2|pass2
```
Run the script from the terminal with the path to your login.txt:
```bash
python main.py <path_to_login_file>
```
Example:

```bash
python main.py login.txt
```
Output
Terminal Output:
Displays essential information for each login attempt:

```rust
2024-11-30 13:32:40 | LOGIN SUCCESS | Connected to https://example.com:2083/
2024-11-30 13:33:08 | TIMEOUT | Connection to https://anotherdomain.com:2083/
2024-11-30 13:33:56 | ERROR | Failed to resolve host for https://invalid-url.com:2083/
```
Log File (cpanel_test.log):
Detailed logs for debugging:

```rust
2024-11-30 13:32:40 | DEBUG | Starting HTTPS connection to https://example.com:2083/
2024-11-30 13:32:40 | INFO  | Login successful for https://example.com:2083/
2024-11-30 13:33:08 | ERROR | Connection to https://anotherdomain.com:2083/ timed out.
2024-11-30 13:33:56 | ERROR | Could not resolve host for https://invalid-url.com:2083/: getaddrinfo failed.
```
Example
Given the following login.txt file:

```arduino
https://botocol.com:2083|username|password
https://slrb-540-7.slc.westdc.net:2083|user2|pass2
https://invalid-url.com:2083|user3|pass3
```

The terminal might display:

```rust

2024-11-30 13:32:40 | LOGIN SUCCESS | Connected to https://botocol.com:2083/
2024-11-30 13:33:08 | TIMEOUT | Connection to https://slrb-540-7.slc.westdc.net:2083/
2024-11-30 13:33:56 | ERROR | Failed to resolve host for https://invalid-url.com:2083/
```
Contributing
Feel free to fork the repository, submit issues, or create pull requests to improve this project.

License
This project is licensed under the MIT License. See the LICENSE file for details.
