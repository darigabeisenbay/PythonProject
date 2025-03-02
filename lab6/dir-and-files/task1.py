import os


def list_contents(path):
    dirs = []
    files = []
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            dirs.append(item)
        else:
            files.append(item)
    return dirs, files

def main():
    path = input("Enter directory path: ")
    if not os.path.exists(path):
        print("Path does not exist.")
        return

    dirs, files = list_contents(path)
    print("Directories:", dirs)
    print("Files:", files)
    print("All contents:", dirs + files)


if __name__ == "__main__":
    main()

