import requests
from bs4 import BeautifulSoup

# open the file with the list of folders and put them all into a list
with open('fodlers', 'r') as file:
    list_of_folders = file.readlines()
    list_of_folders = [folder.strip() for folder in list_of_folders]

print(f"I got the list and {len(list_of_folders)} folders")
base_url = "https://www.vx-underground.org/#E:/root/Samples/Families"

for folder in list_of_folders:



    # Function to filter out the links that end with .7z
    def function(href):
        return href and href.endswith('.7z')


    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a', href=function)
    print(f"Line 28: Found {len(links)} links")

    for link in links:
        print(link['href'])
        file_url = base_url + link['href']
        file_response = requests.get(file_url)

        # Logic to download and save the .7z file
        with open(..., 'wb') as file:
            file.write(file_response.content)
