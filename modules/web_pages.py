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
        name, url = line.split(",")
        current_line = url.strip()
        try:
            response = requests.get(current_line)
            if response.status_code >= 200 and response.status_code <= 299 :
                output_file.write(f"{name}: Connection Success: {response.status_code} \n")
            elif response.status_code >= 300 and response.status_code <= 399:
                output_file.write(f"{name}: Client error: {response.status_code} \n")
            elif response.status_code >= 400 and response.status_code <= 499:
                output_file.write(f"{name}: Server error: {response.status_code} \n")
            else:
                output_file.write(f"{name}: unknown: {response.status_code} \n")
        except:
            if "cis" in line:
                output_file.write(f"{name}: CIS only accessable from WREN \n")
    return results