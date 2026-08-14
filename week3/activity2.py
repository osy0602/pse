
class ReadingFile:
    with open("week3/junk.txt","r") as data:
        lines = data.readlines()
        print(len(lines))

    with open("week3/junk.txt","a") as data:
        data.write("text file nanalyssis")

    with open("week3/junk.txt","r") as data:
        lowerfile = data.read().lower()
        print(lowerfile)

if __name__ == "__main__":
    ReadingFile()
