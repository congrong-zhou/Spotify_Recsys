import sys
import numpy as np
from Dataset import *

def main():
    fileprefix = "mpd.slice."
    num_play_list = 1000
    data = Data()
    data.load_json_to_csv(fileprefix, num_play_list)


if __name__ == "__main__":
    main()


