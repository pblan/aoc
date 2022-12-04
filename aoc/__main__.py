from __future__ import annotations
from aoc import utils

if __name__ == "__main__":
    import logging 

    # set log directory
    logging.basicConfig(
        filename="aoc.log",
        filemode="w",
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    
    utils.update_current_year()