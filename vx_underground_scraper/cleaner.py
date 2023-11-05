import concurrent
from concurrent.futures import ThreadPoolExecutor

import requests
import os


def bar():
    with open("families.txt", 'r') as file:
        # take every line in the file and put it into a list
        list_of_folders = file.readlines()

        # strip every item in the list which is comma separated
        list_of_families = [folder.split(',') for folder in list_of_folders]


def foo(list_of_families):
    for i in range(1, len(list_of_families)):
        perc = (i / len(list_of_families) * 100)
        print(f"Progress: {perc:.2f}%")
        base_url = "https://www.vx-underground.org/#E:/root/Samples/Families"

        family = list_of_families[i][0].split('*')[0].split("/Families/")[1].split("/")[0]
        print(f"Current fam is: {family}")
        list_of_zips = []

        if requests.get(base_url + '/' + family + "/Samples").status_code == 200:
            base_url = "https://samples.vx-underground.org/root/Samples/Families/" + family + "/Samples"
            # print(f"Line 18: Samples folder exists for {family}")
        else:
            base_url = "https://samples.vx-underground.org/root/Samples/Families/" + family
        # print(f"Line 21: base_url is {base_url}")

        # create a folder in the "vx" folder named after the family parameter
        if not os.path.exists("vx/" + family):
            os.makedirs("vx/" + family)

        for item in list_of_families[i]:
            if ".7z" in item:
                zipi = item.split('*')[0].strip('"')
                list_of_zips.append(f"{family}/{zipi}")
                # with open(f"vx/{family}/{zipi}", 'wb') as file:
                #    file_response = requests.get(base_url + '/' + zipi)
                #    print(base_url + '/' + zipi)
                #    file.write(file_response.content)

        # save "list_of_zips" to a file
        with open(f"list_of_zips.txt", 'w') as file:
            for item in list_of_zips:
                file.write(item + "\n")


def saver(malware_path):
    base_url = "https://samples.vx-underground.org/root/Samples/Families/"
    with open(f"vx/{malware_path}", 'wb') as file:
        file_response = requests.get(base_url + malware_path)
        print(malware_path)
        file.write(file_response.content)


def multiculti(list_of_zippis):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(saver, list_of_zippis)


def main():
    with open("list_of_zips.txt", 'r') as file:
        list_of_zips = file.readlines()
        list_of_zips = [zippi.strip() for zippi in list_of_zips]
        multiculti(list_of_zips)


if __name__ == '__main__':
    main()
