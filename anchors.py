#!/usr/bin/env python3

from bs4 import BeautifulSoup
from requests import get
from sys import argv

def cli_args() -> str:
    try:
        if len(argv) > 2:
            exit(1)
        url = str(argv[1])
        return url
    except IndexError:
        print("\nPlease Enter URL eg: \"anchors.py https://google.com\"\n")
        exit(1)
    except Exception as e:
        print("\nERROR! in cli_args: " + str(e) + "\n")
        exit(1)

def get_request(url: str) -> get:
    try:
        if url:
            if not url.startswith("http"):
                print("Prepending HTTPS:// to input URL.")
                url = "https://" + url
            print("Sending HTTPS request to " + url)
            return get(url)
        else:
            exit(1)
    except Exception as e:
        print("ERROR! in get_request: " + str(e))
        exit(1)

def get_anchors(response: get):
    try:
        if response:
            soup = BeautifulSoup(response.content, 'html.parser')
            soup = soup.find_all("a")
            if soup:
                return soup
            else:
                exit(1)
        else:
            exit(1)
    except Exception as e:
        print("ERROR! in get_anchors: " + str(e))
        exit(1)

def bruce():
    print("        _         ")
    print("       (_)        ")
    print("        |         ")
    print("   ()---|---()    ")
    print("        |         ")
    print("        |         ")
    print(" __     |     __  ")
    print("|\     /^\     /| ")
    print("  '..-'   '-..'   ")
    print("    `-._ _.-`     ")
    print("        '         ")
    print("     ANCHORS..")

def main():
    bruce()
    url = cli_args()
    links = get_anchors(get_request(url))
    links = [l for l in links if l.has_attr('href')]
    links = [str(l['href']) for l in links]
    print("\n\n  ******  Links embedded in page  ******  \n")
    [print(l + "\n") for l in links if l.startswith("http")]

if __name__ == '__main__':
    main()



