from libradiko import *


if __name__ == "__main__":
    print(Authorization().get_auththenticated_headers())
    print(radikotoday().show())