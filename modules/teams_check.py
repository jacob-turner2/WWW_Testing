import socket
import requests

#Code for this function was reviecved through ChatGPT. Prompts and responses can be found here: https://chat.openai.com/share/2be3fbb8-678e-4b2d-9f2e-2b58c6e30864

def check_teams(output_file):
    """
    Connect to remote sockets to ensure the Teams website, and TCP
    ports are responsive. Also check if UDP ports can be sent messages.
    Checks for connectivity to the API.

    Input: The output file to be written to.
    Output: Errors returned by c level sockets api.
    """
    output_file.write("\nMicrosoft Teams Ports Status: \n")
    #https://learn.microsoft.com/en-us/answers/questions/896023/when-does-microsoft-teams-use-tcp
    tcp_ports = [80, 443]
    udp_ports = [3478, 3479, 3480, 3481]
    server = "teams.microsoft.com"

    for tcp_port in tcp_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((server, tcp_port))
        if result == 0:
            output_file.write(f"Port {tcp_port}: Open \n")
        else:
            output_file.write(f"Port {tcp_port}: Closed \n")

    output_file.write("Microsoft Teams API Status: \n")
    api_url = "https://graph.microsoft.com/v1.0/me/joinedTeams"
    response = requests.get(api_url)
    
    if response.status_code == 401:  # Unauthorized, but the API is reachable
        output_file.write(f"{api_url}: API reachable (Authentication required) \n")
    elif response.status_code >= 200 and response.status_code <= 299:
        output_file.write(f"{api_url}: API Success: {response.status_code} \n")
    else:
        output_file.write(f"{api_url}: API Error: {response.status_code} \n")  