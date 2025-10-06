# utils/ip_validator.py
import sys

def validate_ip(ip):
    """
    Validates an IPv4 address.

    Parameters:
    - ip: string, the IP address to validate.

    Returns:
    - True if valid, raises SystemExit with error message if invalid.
    """
    campos = ip.split(".")
    if len(campos) != 4:
        raise SystemExit(f"The address '{ip}' is not a valid IP.")
    
    for c in campos:
        try:
            n = int(c)
            if n < 0 or n > 255:
                raise SystemExit(f"The address '{ip}' contains an invalid number: {n}.")
        except ValueError:
            raise SystemExit(f"The address '{ip}' contains a non-integer value: '{c}'.")
    
    return True

if __name__ == "__main__":
    # Get IP from command line arguments or input
    if len(sys.argv) > 1:
        ip_address = sys.argv[1]
    else:
        ip_address = input("Enter an IP address to validate: ")
    
    if validate_ip(ip_address):
        print(f"The address '{ip_address}' is a valid IPv4 address.")
