# urlDNA

![urlDNA Logo](https://urldna.io/assets/images/urldna_green.png)

urlDNA is a powerful tool for comprehensive URL analysis, advanced brand monitoring, phishing detection, and custom query capabilities. This Python package allows users to interact with the urlDNA API seamlessly through Python.



[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

[![GitHub license](https://img.shields.io/github/license/Day8/re-frame.svg?style=flat-square)](LICENSE)

[Homepage](https://urldna.io/)

## Features

- **Create Scan**: Initiate a new scan for a given URL.
- **Search**: Perform a search query to find relevant data.
- **Get Scan**: Retrieve the results of a all scans.
- **Viewports**: All available viewports by device.
- **User Agents**: All available user agents.
- **Fast Check**: Check if an URL is CLEAN or MALICIOUS (beta).

## Installation

To install the urlDNA Python package, use pip:

```bash
pip install urldna
```

## Usage
### Installation
First, import the package and initialize the client with your API key:

```python
from urldna import UrlDNA

# Initialize the client with your API key
api_key = 'YOUR_API_KEY'
client = UrlDNA(api_key)
```

## Create Scan
Initiate a new scan for a given URL to analyze its content and metadata.

```python
# Create a scan for a URL
url = 'https://example.com'
scan_result = client.create_scan(url)
print(f'Scan ID: {scan_result.scan.id}')
```

## Search
Perform a search query using Custom Query Language to find relevant data.

```python
# Perform a search query
query = 'domain LIKE google.com'
search_results = client.search(query)
print(search_results)
```

## Get Scan
Retrieve the results of a previously initiated scan using its scan ID.

```python
# Get scan results
scan_id = 'your_scan_id'
scan_result = client.get_scan(scan_id)
print(scan_result)
```

## Viewports
List of all available viewports (device, height, width)

```python'
viewports = client.viewports()
print(viewports)
```

## Viewports
List of all available user agents (browser, device, user_agent)

```python'
user_agents = client.user_agents()
print(user_agents)
```

## Fast check
Check if an URL is CLEAN or MALICIOUS (beta).

```python'
fast_check = client.fast_check("https://google.com")
print(fast_check)
```

# API Reference

for all API details, please viti the [API Documentation](https://urldna.io/api) page.

`UrlDNA(api_key)`
- Initializes the client with the provided API key. Copy your API key from [Profile](https://urldna.io/profile) page.

## Methods
- `create_scan(url, device='DESKTOP', width=1920, height=1080, user_agent=None, waiting_time=5, private_scan=False)`: Initiates a scan for the given URL and returns a scan ID.
- `search(query)`: Performs a search based on the given query and returns the results.
- `get_scan(scan_id)`: Retrieves the results of the scan identified by the given scan ID.

# Contributing
Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

# License
This project is licensed under the MIT License. See the LICENSE file for details.

# Support
For any issues or questions, please contact [urldna@urldna.io](mailto:urldna@urldna.io).

# Acknowledgements
Thank you for using urlDNA! We hope our tool helps you gain valuable insights into your URLs and online presence.
