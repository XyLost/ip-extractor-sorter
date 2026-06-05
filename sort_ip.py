import ipaddress
import os
import re
import random

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


def sort_ip_addresses_from_folder(input_folder, output_file, mode='sorted', port=''):
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

    main_output_path = os.path.join(result_folder, output_file)
    with open(main_output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(final_ips))

    print(f"{len(final_ips)} unique IPs extracted and saved to {main_output_path}")

    print("\nIf you want a separate random file to be created from the IPs, enter the number.")
    print("If you don't want to, just press Enter.")
    count_input = input("Number of random IPs: ").strip()

    if count_input.isdigit():
        count = int(count_input)

        if count > 0:
            if count > len(final_ips):
                count = len(final_ips)

            random_subset = random.sample(final_ips, count)

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

sort_ip_addresses_from_folder(input_folder, output_file, mode=mode, port=port)