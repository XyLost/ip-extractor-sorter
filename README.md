# IP Extractor & Sorter

A lightweight Python tool for extracting, deduplicating, sorting, randomizing, and exporting IPv4 addresses from multiple files.

Designed for handling large IP lists collected from logs, scan results, configuration files, or any text-based source.

---

## Features

✔ Extract valid IPv4 addresses from multiple files

✔ Detect IPs with or without ports

✔ Automatically remove duplicates

✔ Sort IPs numerically

✔ Randomize output order

✔ Add a custom port to every IP

✔ Generate a random subset file

✔ Skip corrupted or unreadable files

✔ Automatically clean processed input files

---

## Use Cases

- Processing server IP lists
- Cleaning scan results
- Extracting IPs from logs
- Preparing proxy lists
- Building CDN node lists
- Network administration tasks
- Data collection and normalization

---

## How It Works

The script scans every file inside the `input` directory and:

1. Reads file content
2. Extracts valid IPv4 addresses
3. Removes duplicates
4. Sorts or randomizes the result
5. Optionally appends a port
6. Saves the final list into the `result` directory
7. Optionally creates a random subset file
8. Deletes processed source files

---

## Project Structure

```text
project/
│
├── input/
│   ├── file1.txt
│   ├── file2.txt
│   └── ...
│
├── result/
│
└── sort_ip.py
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/ip-extractor-sorter.git
cd ip-extractor-sorter
```

No external dependencies are required.

Python standard libraries used:

- ipaddress
- os
- re
- random

---

## Usage

Run:

```bash
python sort_ip.py
```

### Step 1

Enter the output filename:

```text
Please enter the output file name:
ips
```

### Step 2

Choose sorting mode:

```text
Choose sorting mode (sorted/random):
sorted
```

Available modes:

| Mode | Description |
|--------|-------------|
| sorted | Sort IPs numerically |
| random | Shuffle IPs randomly |

### Step 3

Optional port assignment:

```text
Enter a port number if you want to add it:
443
```

Result:

```text
1.1.1.1:443
8.8.4.4:443
8.8.8.8:443
```

---

## Random Subset Generation

After creating the main output file, the script can generate an additional random subset.

Example:

```text
Number of random IPs:
100
```

Output:

```text
result/random_ips.txt
```

This file contains 100 randomly selected IP addresses from the final dataset.

---

## Example Workflow

Input files:

```text
input/file1.txt
input/file2.txt
input/file3.txt
```

Extracted IPs:

```text
8.8.8.8
1.1.1.1
8.8.8.8
9.9.9.9
```

Final output:

```text
1.1.1.1
8.8.8.8
9.9.9.9
```

---

## Notes

- Only valid IPv4 addresses are accepted.
- Invalid addresses are ignored.
- Duplicate entries are removed automatically.
- Files that cannot be read are skipped.
- Source files are deleted after processing.
- Supports UTF-8 and mixed text files.

---

## Requirements

- Python 3.8 or newer

Check your version:

```bash
python --version
```

---

## Future Improvements

- IPv6 support
- Export to CSV
- Export to JSON
- Multi-threaded processing
- GUI version
- Custom filtering rules

---

## License

This project is released under the MIT License.

Feel free to use, modify, and distribute it.

---

## Disclaimer

This tool is intended for educational, research, and network administration purposes only.

Users are responsible for complying with all applicable laws and regulations when processing network-related data.
