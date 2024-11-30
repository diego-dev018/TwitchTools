from extra_functions import make_db
from headers import get_headers


def main():
    make_db()
    HEADER = get_headers()


if __name__ == '__main__':
    main()