import yaml
import requests
import time
from collections import defaultdict

# Load configuration file
def load_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Perform health check on an endpoint
def check_health(endpoint):
    url = endpoint.get("url")
    method = endpoint.get("method", "GET").upper()
    headers = endpoint.get("headers", {})
    body = endpoint.get("body", None)
    # print(f"checking health for url:{url}")

    try:
        if method == "GET":
            response = requests.get(url, headers=headers, timeout=5)
        elif method == "POST":
                response = requests.post(url, headers=headers, data=body, timeout=5)
        else:
            print(f"Unsupported HTTP method: {method}")
            return False, 0

        latency = response.elapsed.total_seconds() * 1000  # Convert to milliseconds
        if 200 <= response.status_code < 300 and latency < 500:
            return True, latency
        else:
            return False, latency
    except Exception as e:
        print(f"Error checking {url}: {e}")
        return False, 0

# Calculate and log availability percentage
def log_availability(availability_tracker):
    print("\n--- Availability Report ---")
    for domain, stats in availability_tracker.items():
        total = stats["total"]
        up = stats["up"]
        percentage = round(100 * up / total) if total > 0 else 0
        print(f"{domain} has {percentage}% availability percentage")

# Main program
def main(file_path):
    config = load_config(file_path)
    availability_tracker = defaultdict(lambda: {"up": 0, "total": 0})

    try:
        while True:
            for endpoint in config:
                url = endpoint.get("url")
                domain = url.split("//")[1].split("/")[0]  # Extract domain from URL

                is_up, latency = check_health(endpoint)
                availability_tracker[domain]["total"] += 1
                if is_up:
                    availability_tracker[domain]["up"] += 1

                status = "UP" if is_up else "DOWN"
                print(f"{endpoint.get('name')} - {url} - {status} (Latency: {latency:.2f} ms)")

            log_availability(availability_tracker)
            time.sleep(15)  # Wait for the next cycle
    except KeyboardInterrupt:
        print("\nExiting program. Final report:")
        log_availability(availability_tracker)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python health_check.py <config_file_path>")# we need to update the config file path.Copy the config filepath and paste it "<config-file path>"
        sys.exit(1)
    main(sys.argv[1])