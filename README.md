**cPanel Login Tester
**
A Python script to test login credentials for cPanel across multiple URLs. This script is designed to handle timeout errors and network issues gracefully while providing clean, user-friendly output for terminal users. All detailed error logs are saved to a log file for further analysis.

Features
Multi-Platform Support: Works on both Windows and Linux.
Dynamic Input: Accepts a custom path to the login.txt file as a command-line argument.
Clean Output: Displays only essential information (success, timeout, or error) in the terminal for each attempt.
Detailed Logs: Saves all connection details and errors to a log file (cpanel_test.log) for troubleshooting.
Timeout Handling: Handles connection timeouts gracefully.
Secure Requests: Utilizes HTTPS for secure login attempts.
Usage
Prerequisites
Python 3.8+
Required Python modules: requests, logging, argparse

Install dependencies:

bash
Salin kode
pip install -r requirements.txt
How to Run
Prepare your login.txt file in the following format (one entry per line):
arduino
Salin kode
https://example.com:2083|username|password
https://anotherdomain.com:2083|user2|pass2
Run the script from the terminal:
bash
Salin kode
python main.py <path_to_login_file>
Example:
bash
Salin kode
python main.py login.txt
Output
The terminal displays a one-line summary for each login attempt (e.g., LOGIN SUCCESS or TIMEOUT).
Detailed logs are saved to cpanel_test.log for debugging.
Example Output
Terminal Output:

rust
Salin kode
2024-11-30 13:32:40 | LOGIN SUCCESS | Connected to https://example.com:2083/  
2024-11-30 13:33:08 | TIMEOUT | Connection to https://anotherdomain.com:2083/  
2024-11-30 13:33:56 | ERROR | Failed to resolve host for https://invalid-url.com:2083/  
Log File (cpanel_test.log):

rust
Salin kode
2024-11-30 13:32:40 | DEBUG | Starting HTTPS connection to https://example.com:2083/  
2024-11-30 13:32:40 | INFO | Login successful for https://example.com:2083/  
2024-11-30 13:33:08 | ERROR | Connection to https://anotherdomain.com:2083/ timed out.  
2024-11-30 13:33:56 | ERROR | Could not resolve host for https://invalid-url.com:2083/: getaddrinfo failed.  
Contribution
Feel free to fork this repository and submit pull requests to improve the script or add new features.

License
This project is licensed under the MIT License.
