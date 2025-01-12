----------------- Requirements-----------------

    To run the Health Check Program, you need the following:

    - Python 3.8 or higher
    
    Ensure that you have Python 3.8 or a newer version installed on your system.
    

-----------Steps to Installing Python (if not installed) -----------------

If you do not have Python installed on your system, follow the steps below to install it:

Windows:
        1. Download Python*: Go to the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
        - Click on the "Download Python" button. Make sure to download the latest stable version (Python 3.8 or higher).
        
        2. Run the Installer: 
        - Once downloaded, run the installer.
        - IMPORTANT: During installation, make sure to check the box *"Add Python to PATH"* before proceeding. This ensures Python is available globally from the command line.
        
        3. Verify the Installation*:
        - Open the Command Prompt (press Win + R, type cmd, and press Enter).
        - Type the following command to verify Python is installed correctly:
            bash
            python --version
            
        - You should see something like Python 3.x.x, confirming that Python is installed.

macOS:
        1. Download Python*: Visit [https://www.python.org/downloads/](https://www.python.org/downloads/) and download the latest version of Python 3 for macOS.

        2. Install via Homebrew* (Recommended):
        - If you have *Homebrew* installed, you can install Python by running:
            bash
            brew install python
            
        3. Verify the Installation*:
        - Open the terminal and type:
            bash
            python3 --version
            
        - You should see something like Python 3.x.x.

Linux (Ubuntu/Debian):

        1. Install Python 3*:
        - Open a terminal and run the following command:
            bash
            sudo apt update
            sudo apt install python3 python3-pip
            
        
        2. Verify the Installation*:
        - After installation, verify Python is installed correctly by running:
            bash
            python3 --version
            

Setup python environment with version installed and install the packages to install pyyaml and requests 
python3 -m venv path/to/venv
source path/to/venv/bin/activate
python3 -m pip install pyyaml
python3 -m pip install requests
pip3 install matplotlib  
pip3 install openpyxl
pip3 install matplotlib



-------How to Run the Program in Command Prompt -----

            To run the program, simply execute the following command in your terminal:
            bash
            python synthetic_monitor.py <path_to_config_file>

            Where <path_to_config_file> is the path to your YAML configuration file.

----Example for How to run the program---
            bash
            python3 filename.py config.yaml

---- How to exit---
      User presses CTRL+C and the program exits

-----------Conclusion------------------

            This Health Check Program helps you monitor the health of HTTP endpoints by periodically making HTTP requests and tracking their availability. With customizable configuration through YAML files, you can easily monitor a large number of services and track their uptime.
