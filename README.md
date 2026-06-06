# IP Extractor & Sorter

A lightweight Python tool for extracting, deduplicating, sorting, randomizing, and exporting IPv4 addresses from multiple files.

Designed for handling large IP lists collected from logs, scan results, configuration files, proxy lists, server inventories, or any text-based source.

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

✔ Optional cleanup of processed input files

✔ No third-party dependencies required

---

## Use Cases

- Processing server IP lists
- Cleaning scan results
- Extracting IPs from logs
- Preparing proxy lists
- Building CDN node lists
- Network administration tasks
- Data collection and normalization
- Organizing large IP datasets

---

## How It Works

The script scans every file inside the `input` directory and:

1. Reads file content
2. Extracts valid IPv4 addresses
3. Removes duplicate entries
4. Sorts or randomizes the result
5. Optionally appends a custom port
6. Saves the final list into the `result` directory
7. Optionally creates a random subset file
8. Asks whether processed source files should be deleted

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

No external packages are required.

The script uses only Python standard libraries:

- ipaddress
- os
- re
- random

---

## Requirements

- Python 3.8 or newer

Verify your Python version:

```bash
python --version
```

---

## Usage

Run the script:

```bash
python sort_ip.py
```

### Step 1 — Output File Name

```text
Please enter the output file name:
ips
```

Result:

```text
result/ips.txt
```

---

### Step 2 — Sorting Mode

```text
Choose sorting mode (sorted/random):
sorted
```

Available modes:

| Mode | Description |
|--------|-------------|
| sorted | Sort IPs numerically |
| random | Shuffle IPs randomly |

---

### Step 3 — Optional Port Assignment

```text
Enter a port number if you want to add it (or press Enter to skip):
443
```

Output example:

```text
1.1.1.1:443
8.8.4.4:443
8.8.8.8:443
```

---

### Step 4 — Optional Random Subset

After generating the main output file, the script can create an additional random subset.

Example:

```text
Number of random IPs:
100
```

Generated file:

```text
result/random_ips.txt
```

This file contains a randomly selected subset from the processed IP list.

---

### Step 5 — Optional Cleanup

After processing is complete:

```text
Do you want to delete the processed files from the input folder? (y/n)
```

Options:

```text
y
```

or

```text
yes
```

Deletes all processed files from the input directory.

```text
n
```

Keeps all source files unchanged.

---

## Example Workflow

### Input Files

```text
input/file1.txt
input/file2.txt
input/file3.txt
```

### Raw Content

```text
8.8.8.8
1.1.1.1
8.8.8.8
9.9.9.9
```

### Output

```text
1.1.1.1
8.8.8.8
9.9.9.9
```

Duplicates are removed automatically.

---

## Notes

- Only valid IPv4 addresses are accepted.
- Invalid addresses are ignored.
- Duplicate entries are removed automatically.
- Files that cannot be read are skipped.
- Supports UTF-8 and mixed text files.
- Source files are deleted only if the user confirms deletion.
- Existing result files with the same name will be overwritten.

---

## Performance

The tool is suitable for processing:

- Small IP lists
- Medium-sized datasets
- Large collections of text files

Performance depends primarily on:

- Number of files
- Total file size
- Storage speed

---

## Future Improvements

- IPv6 support
- CSV export
- JSON export
- Multi-threaded processing
- GUI version
- Advanced filtering options
- CIDR range support

---

## License

MIT License

You are free to use, modify, distribute, and integrate this project into your own workflows.

---

## Disclaimer

This project is provided for educational, research, and network administration purposes.

Users are responsible for ensuring compliance with all applicable laws, regulations, and policies when processing network-related data.

