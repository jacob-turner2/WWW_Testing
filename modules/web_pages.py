import requests

def web_check(upath, output_file):
    '''
    test list of web pages
    gmail, CIS, google, chatGPT, venmo, EAMS-A, Branching, youtube, instagram
    
    input: text file of URLs and the output file to be written to
    output: status codes in a list
    '''
    output_file.write("\nWebsite Statuses: \n")
    url_file = open(upath, 'r')
    lines = url_file.readlines()
    results = []
    for line in lines:
        response = requests.get(line.strip())
        if response.status_code >= 200 and response.status_code <= 299 :
            results.append("Connection Success")
            output_file.write(f"{line.strip()}: Connection Success: {response.status_code} \n")
        elif response.status_code >= 300 and response.status_code <= 399:
            results.append("Client error")
            output_file.write(f"{line.strip()}: Client error: {response.status_code} \n")
        elif response.status_code >= 400 and response.status_code <= 499:
            results.append("Server error")
            output_file.write(f"{line.strip()}: Server error: {response.status_code} \n")
        else:
            results.append("unknown")
            output_file.write(f"{line.strip()}: unknown: {response.status_code} \n")
    return results