import yaml
import requests
import time
import random
from urllib.parse import urlparse
from collections import defaultdict

# Function to load the configuration file
def load_config(file_path):
  
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        print(f"Error loading configuration file: {e}")
        exit(1)

# Function to perform health check on a single endpoint
def check_health(endpoint):
 
    url = endpoint.get("url")
    method = endpoint.get("method", "GET").upper()  # Default to GET if not specified
    headers = endpoint.get("headers", {})
    body = endpoint.get("body", None)

    # Extract domain name from the URL
    domain = urlparse(url).netloc

    try:
        # Simulate a start time
        start_time = time.time()

        # Perform the HTTP request
        response = requests.request(method, url, headers=headers, data=body, timeout=5)

        # Simulate latency with random values for testing (100ms to 900ms)
        latency = random.randint(100, 900)

        # Check if the response is UP
        if 200 <= response.status_code < 300 and latency < 500:
            return domain, latency, "UP"
    except Exception as e:
        print(f"Error checking {url}: {e}")

    # If any condition fails, return DOWN
    return domain, random.randint(500, 900), "DOWN"

# Function to log individual test results
def log_test_results(results):
  
    print("Health Check Results for Current Cycle:")
    for domain, latency, status in results:
        if status == "UP":
            print(f"{domain}: UP (Latency: {latency:.2f} ms)")
        else:
            print(f"{domain}: DOWN (Simulated Latency: {latency:.2f} ms)")

# Function to log cumulative availability percentages
def log_availability(domain_stats, domain_counts):
 
    print("\nCumulative Availability Results:")
    for domain in domain_counts:
        availability = (100 * domain_stats[domain] / domain_counts[domain])
        print(f"{domain} has {availability:.0f}% availability")
    print("-" * 50)

# Main function
def main(file_path):
 
    # Load the configuration file
    endpoints = load_config(file_path)

    # Initialize dictionaries to track stats
    domain_stats = defaultdict(int)
    domain_counts = defaultdict(int)

    try:
        # Infinite loop to continuously check health every 15 seconds
        while True:
            results = []  # Store results for the current cycle

            # Perform health check for each endpoint
            for endpoint in endpoints:
                domain, latency, status = check_health(endpoint)

                # Update stats
                domain_counts[domain] += 1
                if status == "UP":
                    domain_stats[domain] += 1

                # Store the result
                results.append((domain, latency, status))

            # Log individual test results
            log_test_results(results)

            # Log cumulative availability percentages
            log_availability(domain_stats, domain_counts)

            # Wait for 15 seconds before the next cycle
            print("Sleeping for 15 seconds...\n")
            time.sleep(15)
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")

# Entry point of the script
if __name__ == "__main__":
    import sys

    # Ensure a file path is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python health_check_default_get.py <path_to_yaml_file>")
        exit(1)

    # Run the main function with the provided file path
    config_file = sys.argv[1]
    main(config_file)