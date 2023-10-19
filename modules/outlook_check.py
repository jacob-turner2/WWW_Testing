import requests
import socket

#Code for this function was reviecved through ChatGPT. Prompts and responses can be found here: https://chat.openai.com/share/2be3fbb8-678e-4b2d-9f2e-2b58c6e30864

def check_outlook(output_file):
    """
    Connect to the ports used by outlook for email through a socket conneciton with
    the website and its associated ports. Also checks the API for connectivity.

    Input: The output file to be written to.
    Output: N/A, writes status to output file.
    """
    output_file.write("\nOutlook Ports Status: \n")
    ports = [587, 993, 995]  # SMTP, IMAP, and POP3 respectively
    server = "outlook.office365.com"
    api_url = "https://outlook.office365.com/api/v2.0/me/folders/inbox/messages"
    
    for port in ports:
        outlook_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = outlook_socket.connect_ex((server, port))
        
        if result == 0:
            output_file.write(f"Port {port}: Open \n")
        else:
            output_file.write(f"Port {port}: Closed \n")
        
        outlook_socket.close()
    output_file.write("Outlook API Status: \n")
    response = requests.get(api_url)
    if response.status_code == 401:  # Unauthorized, but the API is reachable
        output_file.write(f"{api_url}: API reachable (Authentication required) \n")
    elif response.status_code >= 200 and response.status_code <= 299:
        output_file.write(f"{api_url}: API Success: {response.status_code} \n")
    else:
        output_file.write(f"{api_url}: API Error: {response.status_code} \n")