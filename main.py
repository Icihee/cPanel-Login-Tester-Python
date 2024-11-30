import argparse
import requests
import logging

# Set up logging to write detailed logs to a file
log_file = "detailed_log.txt"
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(log_file),
    ]
)

# Simple logger for terminal display
console_logger = logging.getLogger("console_logger")
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s", "%Y-%m-%d %H:%M:%S"))
console_logger.addHandler(console_handler)
console_logger.setLevel(logging.INFO)


def test_cpanel_login(url, username, password):
    login_url = f"{url}/login/"
    try:
        # Attempt to login
        response = requests.post(login_url, data={'user': username, 'pass': password}, timeout=10)

        # Check if login was successful
        if "cPanel" in response.text and response.status_code == 200:
            console_logger.info(f"LOGIN SUCCESS | Connection to {url}")
            logging.info(f"Login successful for {username} at {url}")
        else:
            console_logger.error(f"LOGIN FAILED | Connection to {url}")
            logging.warning(f"Login failed for {username} at {url}")
    except requests.ConnectTimeout:
        console_logger.error(f"ERROR | Connection to {url} timed out.")
        logging.error(f"Connection to {url} timed out.")
    except requests.RequestException as e:
        console_logger.error(f"ERROR | Connection to {url}")
        logging.error(f"Error occurred for {username} at {url}: {str(e)}")


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Test cPanel login credentials.")
    parser.add_argument('login_file', help="Path to the file containing login details.")
    args = parser.parse_args()

    try:
        # Read login details from file
        with open(args.login_file, "r") as file:
            for line in file:
                # Each line format: URL|USERNAME|PASSWORD
                line = line.strip()
                if line:
                    parts = line.split("|")
                    if len(parts) == 3:
                        url, username, password = parts
                        test_cpanel_login(url, username, password)
                    else:
                        console_logger.error(f"INVALID FORMAT | {line}")
                        logging.warning(f"Invalid format: {line}")
    except FileNotFoundError:
        console_logger.error(f"ERROR | File not found: {args.login_file}")
        logging.error(f"File not found: {args.login_file}")
    except Exception as e:
        console_logger.error("ERROR | An unexpected error occurred.")
        logging.error(f"Unexpected error: {str(e)}")


if __name__ == "__main__":
    main()
