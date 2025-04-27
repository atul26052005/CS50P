import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    pattern = re.search(r'<iframe src="http(s)?:\/\/(?:www.)?youtube\.com\/embed\/(.*?)"></iframe>',s)
    if pattern:
        return "https://youtu.be/" + pattern.group(2)
    else:
        return None

if __name__ == "__main__":
    main()
