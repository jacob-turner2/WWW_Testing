import socket

def dns_checker(upath, output_file):
    """
    Tests dns connections.

    input: path to dns list
    output: status codes in a list
    """
    output_file.write("\nDNS Statuses: \n")
    dns_file = open(upath, 'r')
    lines = dns_file.readlines()

    dns_record = []
    for line in lines:
        try:
            dns_record += socket.gethostbyaddr(line.strip())
            output_file.write(f"{line.strip()}: Accessable \n")
        except:
            dns_record += [f"{line.strip()}: Unreachable"]
            output_file.write(f"{line.strip()}: Unreachable \n")
    return dns_record