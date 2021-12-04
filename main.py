import os


def main():
    path = "."
    files = os.listdir(path)
    print(" ".join(files))


if __name__ == '__main__':
    main()
