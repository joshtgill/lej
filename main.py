import sys
sys.path.append('services/')
sys.path.append('structures/')
sys.path.append('structures/academics')
sys.path.append('structures/accounts')
from lej import Lej


if __name__ == "__main__":
    Lej().start()
