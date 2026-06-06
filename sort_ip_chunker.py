import ipaddress
import os
import re
import random
import math

IP_REGEX = re.compile(r'\b((?:\d{1,3}\.){3}\d{1,3})(?::\d+)?\b')


def is_valid_ipv4(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except:
        return False


def extract_ips_from_text(text):
    found_ips = []

    for match in IP_REGEX.findall(text):
        ip = match.strip()
        if is_valid_ipv4(ip):
            found_ips.append(ip)

    return found_ips


def save_ips_in_chunks(ips, result_folder, output_file, chunk_size):
    total = len(ips)
    base_name, ext = os.path.splitext(output_file)

    if total <= chunk_size:
        output_path = os.path.join(result_folder, output_file)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(ips))
        print(f"{total} unique IPs saved to {output_path}")
        return [output_path]

    num_parts = math.ceil(total / chunk_size)
    saved_paths = []

    for i in range(num_parts):
        start = i * chunk_size
        end = start + chunk_size
        chunk = ips[start:end]

        part_file = f"{base_name}_part{i + 1}{ext}"
        part_path = os.path.join(result_folder, part_file)

        with open(part_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(chunk))

        saved_paths.append(part_path)
        print(f"  Part {i + 1}: {len(chunk)} IPs saved to {part_path}")

    print(f"\n{total} unique IPs split into {num_parts} parts.")
    return saved_paths


def sort_ip_addresses_from_folder(input_folder, output_file, chunk_size, mode='sorted', port=''):
    all_ips = []
    processed_files = []

    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    ips = extract_ips_from_text(content)
                    all_ips.extend(ips)
                    processed_files.append(file_path)
            except:
                pass

    unique_ips = list(set(all_ips))

    if mode == 'sorted':
        final_ips = sorted(unique_ips, key=lambda x: ipaddress.IPv4Address(x))
    elif mode == 'random':
        random.shuffle(unique_ips)
        final_ips = unique_ips
    else:
        print("Invalid mode. Default sorting was applied.")
        final_ips = sorted(unique_ips, key=lambda x: ipaddress.IPv4Address(x))

    if port.strip():
        final_ips = [f"{ip}:{port.strip()}" for ip in final_ips]

    result_folder = "result"
    os.makedirs(result_folder, exist_ok=True)

    print(f"\nTotal unique IPs found: {len(final_ips)}")
    save_ips_in_chunks(final_ips, result_folder, output_file, chunk_size)

    print("\nIf you want a separate random file to be created from the IPs, enter the number.")
    print("If you don't want to, just press Enter.")
    count_input = input("Number of random IPs: ").strip()

    if count_input.isdigit():
        count = int(count_input)

        if count > 0:
            if count > len(final_ips):
                count = len(final_ips)

            random_subset = random.sample(final_ips, count)

            base_name, ext = os.path.splitext(output_file)
            random_file_name = "random_" + output_file
            random_output_path = os.path.join(result_folder, random_file_name)

            with open(random_output_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(random_subset))

            print(f"Random subset ({count} IPs) saved to {random_output_path}")
        else:
            print("The entered number is not valid, so the random file could not be created.")
    else:
        print("The random file was not created.")

    print("\nDo you want to delete the processed files from the input folder? (y/n)")
    delete_choice = input().strip().lower()

    if delete_choice in ['y', 'yes']:
        deleted = 0

        for file_path in processed_files:
            try:
                os.remove(file_path)
                deleted += 1
            except:
                pass

        print(f"Deleted {deleted} processed file(s) from the input folder.")
    else:
        print("Processed files were kept.")

input_folder = 'input'

print("Please enter the output file name:")
output_file = input().strip() + ".txt"

print("Choose sorting mode (sorted/random):")
mode = input().strip().lower()

print("Enter a port number if you want to add it (or press Enter to skip):")
port = input().strip()

print("Enter chunk size (number of IPs per part file, e.g. 50000):")
print("Press Enter to skip chunking and save everything in one file.")
chunk_input = input().strip()

if chunk_input.isdigit() and int(chunk_input) > 0:
    chunk_size = int(chunk_input)
    print(f"Files will be split into parts of {chunk_size:,} IPs each.")
else:
    chunk_size = float('inf')
    print("No chunking. All IPs will be saved in a single file.")

sort_ip_addresses_from_folder(input_folder, output_file, chunk_size, mode=mode, port=port)
