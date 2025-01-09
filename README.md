# Code
    This Health Check Program is designed to monitor the health of HTTP endpoints specified in a configuration file (YAML format). It will log the availability percentage of each domain by periodically checking their status and reporting the results after every 15-second cycle.

      

      ------------1)Overview --------------------

        The Health Check Program checks the status of various HTTP endpoints over time. It sends HTTP requests (either GET or POST) to the endpoints, logs the responses, and calculates the availability percentage for each endpoint. This is especially useful for monitoring APIs, web services, or any system that requires uptime tracking.

        The program uses a configuration file to define the HTTP endpoints and their properties (like request method, headers, and body). Each endpoint is monitored periodically, and availability statistics are logged for easy tracking.

    ---------------- Features ------------------------

        - *HTTP Health Monitoring*: Supports both GET and POST HTTP methods. You can also configure custom headers and request bodies if needed.
        - *Availability Tracking*: Tracks the availability of each domain and logs the cumulative percentage of successful responses.
        - *Error Handling*: Gracefully handles common errors such as connection issues, timeouts, and invalid responses.
        - *Configurable*: All endpoint details (like the URL, request method, headers, etc.) are configurable through a YAML configuration file.


    ----------------- Requirements-----------------

        To run the Health Check Program, you need the following:

        - Python 3.8 or higher
        
        Ensure that you have Python 3.8 or a newer version installed on your system.

        

     -----------Steps to Installing Python (if not installed) -----------------

        If you do not have Python installed on your system, follow the steps below to install it:

         For Windows:
        1. *Download Python*: Go to the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
        - Click on the "Download Python" button. Make sure to download the latest stable version (Python 3.8 or higher).
        
        2. Run the Installer: 
        - Once downloaded, run the installer.
        - IMPORTANT: During installation, make sure to check the box *"Add Python to PATH"* before proceeding. This ensures Python is available globally from the command line.
        
        3. *Verify the Installation*:
        - Open the Command Prompt (press Win + R, type cmd, and press Enter).
        - Type the following command to verify Python is installed correctly:
            bash
            python --version
            
        - You should see something like Python 3.x.x, confirming that Python is installed.

        ### For macOS:
        1. *Download Python*: Visit [https://www.python.org/downloads/](https://www.python.org/downloads/) and download the latest version of Python 3 for macOS.

        2. *Install via Homebrew* (Recommended):
        - If you have *Homebrew* installed, you can install Python by running:
            bash
            brew install python
            

        3. *Verify the Installation*:
        - Open the terminal and type:
            bash
            python3 --version
            
        - You should see something like Python 3.x.x.

        ### For Linux (Ubuntu/Debian):
        1. *Install Python 3*:
        - Open a terminal and run the following command:
            bash
            sudo apt update
            sudo apt install python3 python3-pip
            
        
        2. *Verify the Installation*:
        - After installation, verify Python is installed correctly by running:
            bash
            python3 --version
            

        Once Python is installed, you can proceed with the steps to install dependencies and run the program as described in the rest of this guide.


      -Required Libraries*: 
        - requests: A simple HTTP library for sending HTTP requests.
        - pyyaml: A library for reading and parsing YAML configuration files.
        - time: For controlling the timing of periodic health checks.

        You can install the required libraries using pip by running the following command:
        bash
        pip install requests pyyaml

     -------How to Run the Program in Command Prompt -----

        To run the program, simply execute the following command in your terminal:
        bash
        python health_check.py <path_to_config_file>

        Where <path_to_config_file> is the path to your YAML configuration file.

          ----Example for How to run the program---
                    bash
                    python health_check.py config.yaml

    -----------Conclusion------------------

            This Health Check Program helps you monitor the health of HTTP endpoints by periodically making HTTP requests and tracking their availability. With customizable configuration through YAML files, you can easily monitor a large number of services and track their uptime.
