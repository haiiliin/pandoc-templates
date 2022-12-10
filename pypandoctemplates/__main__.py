from fire import Fire
from .pandoc import pandoc


def main():
    Fire(pandoc)


if __name__ == "__main__":
    main()
