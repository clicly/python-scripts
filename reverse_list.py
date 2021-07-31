from typing import List, TextIO

def read_file(fileName: str) -> List[str]:
        fileObj: TextIO = open(fileName, "r")
        words: List[str] = fileObj.read().splitlines()
        fileObj.close()
        return words

def write_to_file(list: List[str], fileName: str):
    with open(fileName, 'w') as f:
        for item in list:
            f.write("%s\n" % item.strip())

if __name__ == "__main__":
    lines: List[str] = read_file('input.txt')
    lines.reverse()

    write_to_file(lines, "output.txt")