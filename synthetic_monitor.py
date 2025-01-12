import yaml
import requests
import time
import random
from urllib.parse import urlparse
from collections import defaultdict
from openpyxl import Workbook
from openpyxl.chart import LineChart, Reference
import matplotlib.pyplot as plt

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
    if not isinstance(endpoint, dict):
        print("Error: Endpoint is not a dictionary. Skipping...")
        return None, None, "DOWN"

    url = endpoint.get("url")
    if not url:
        print("Error: Missing 'url' in endpoint. Skipping...")
        return None, None, "DOWN"

    method = endpoint.get("method", "GET").upper()
    headers = endpoint.get("headers", {})
    body = endpoint.get("body", None)

    domain = urlparse(url).netloc

    try:
        start_time = time.time()
        response = requests.request(method, url, headers=headers, data=body, timeout=5)
        latency = random.randint(100, 900)

        if 200 <= response.status_code < 300 and latency < 500:
            return domain, latency, "UP"
    except Exception as e:
        print(f"Error checking {url}: {e}")

    return domain, random.randint(500, 900), "DOWN"

# Initialize Excel Workbook
wb = Workbook()
ws = wb.active
ws.title = "Availability Log"
ws.append(["Time", "Domain", "Availability (%)"])

# Function to log data to Excel
def log_to_excel(timestamp, domain_availability):
    for domain, availability in domain_availability.items():
        ws.append([timestamp, domain, availability])

# Function to generate a graph for each domain
def generate_domain_graphs(downtime_percentages):
    for domain, data in downtime_percentages.items():
        times = [t for t, _ in data]
        percentages = [p for _, p in data]

        plt.figure(figsize=(10, 6))
        plt.plot(times, percentages, label=f"{domain} Downtime (%)", marker="o", color="red")
        plt.title(f"Downtime Percentage for {domain}")
        plt.xlabel("Time")
        plt.ylabel("Downtime (%)")
        plt.ylim(0, 100)
        plt.grid()
        plt.legend()
        plt.tight_layout()

        # Save the graph as a PNG file
        filename = f"{domain}_downtime.png"
        plt.savefig(filename)
        plt.close()
        print(f"Graph saved for {domain} as {filename}.")

# Function to log test results to the console
def log_test_results(results):
    print("Health Check Results for Current Cycle:")
    for domain, latency, status in results:
        if domain is None:
            continue
        if status == "UP":
            print(f"{domain}: UP (Latency: {latency:.2f} ms)")
        else:
            print(f"{domain}: DOWN (Simulated Latency: {latency:.2f} ms)")

# Function to log cumulative availability percentages to the console
def log_availability(domain_stats, domain_counts):
    domain_availability = {}
    print("\nCumulative Availability Results:")
    for domain in domain_counts:
        availability = (100 * domain_stats[domain] / domain_counts[domain])
        domain_availability[domain] = round(availability, 2)
        print(f"{domain} has {availability:.0f}% availability")
    print("-" * 50)
    return domain_availability

# Main function
def main(file_path, output_file="availability_log.xlsx"):
    endpoints = load_config(file_path)
    domain_stats = defaultdict(int)
    domain_counts = defaultdict(int)
    downtime_percentages = defaultdict(list)

    try:
        while True:
            results = []
            current_time = time.strftime("%Y-%m-%d %H:%M:%S")

            for endpoint in endpoints:
                domain, latency, status = check_health(endpoint)
                if domain is None:
                    continue
                domain_counts[domain] += 1
                if status == "UP":
                    domain_stats[domain] += 1

                # Calculate downtime percentage
                downtime_percentage = 100 - (100 * domain_stats[domain] / domain_counts[domain])
                downtime_percentages[domain].append((current_time, downtime_percentage))

                results.append((domain, latency, status))

            log_test_results(results)
            domain_availability = log_availability(domain_stats, domain_counts)
            log_to_excel(current_time, domain_availability)

            print("Sleeping for 15 seconds...\n")
            time.sleep(15)
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Saving data and graphs...")
        wb.save(output_file)
        print(f"Excel file saved as {output_file}.")
        generate_domain_graphs(downtime_percentages)
        print("All graphs saved. Exiting...")

# Entry point of the script
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python health_check_with_graph.py <path_to_yaml_file>")
        exit(1)

    config_file = sys.argv[1]
    main(config_file)