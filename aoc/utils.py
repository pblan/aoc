from __future__ import annotations

import pathlib
from logging import getLogger
import time
import requests
import bs4

from aocd import get_data  # function to get data from aoc website

log = getLogger(__name__)


def read_input(year: int, day: int) -> str:
    """Read input from file.

    Args:
        year (int): year
        day (int): day

    Returns:
        str: input
    """

    return pathlib.Path(f"{year}/day{day:02d}/input.txt").read_text()


# https://github.com/antonio-ramadas/aoc-to-markdown/blob/master/aoc_to_markdown.py
def html_tags_to_markdown(tag, is_first_article):
    children = tag.find_all(recursive=False)

    if tag.name != "code":
        for child in children:
            html_tags_to_markdown(child, is_first_article)

    if tag.name == "h2":
        style = "#" if is_first_article else "##"
        tag.insert_before(f"{style} ")
        tag.insert_after("\n\n")
        tag.unwrap()
    elif tag.name == "p":
        tag.insert_after("\n")
        tag.unwrap()
    elif tag.name == "em":
        style = "**" if tag.has_attr("class") and tag["class"] == "star" else "*"
        tag.insert_before(style)
        tag.insert_after(style)
        tag.unwrap()
    elif tag.name == "a":
        tag.insert_before("[")
        tag.insert_after(f']({tag["href"]})')
        tag.unwrap()
    elif tag.name == "span":
        tag.insert_before("*")
        tag.insert_after("*")
        tag.unwrap()
    elif tag.name == "ul":
        tag.unwrap()
    elif tag.name == "li":
        tag.insert_before(" - ")
        tag.insert_after("\n")
        tag.unwrap()
    elif tag.name == "code":
        if "\n" in tag.text:
            tag.insert_before("```\n")
            tag.insert_after("\n```")
        else:
            tag.insert_before("`")
            tag.insert_after("`")
        tag.unwrap()
    elif tag.name == "pre":
        tag.insert_before("")
        tag.insert_after("\n")
        tag.unwrap()
    elif tag.name == "article":
        pass
    else:
        raise ValueError(f"Missing condition for tag: {tag.name}")


def get_markdown(year, day):
    soup = bs4.BeautifulSoup(
        requests.get(f"https://adventofcode.com/{year}/day/{day}").text,
        features="html.parser",
    )

    articles = soup.body.main.findAll("article", recursive=False)
    content = ""

    for i, article in enumerate(articles):
        html_tags_to_markdown(article, i == 0)
        content += "".join([tag.string for tag in article.contents])

    return content


def create_day(year: int, day: int) -> None:
    """Create a folder for aoc day.

    Args:
        year (int): year >= 2015
        day (int): 1 <= day <= 25

    Returns:
        None
    """

    # check if year is valid
    if year < 2015:
        log.error("Year must be >= 2015")
        return

    # check if day is valid
    if day < 1 or day > 25:
        log.error("Day must be 1 <= day <= 25")
        return

    # create folder
    folder = pathlib.Path(f"{year}/day{day:02d}")
    folder.mkdir(parents=True, exist_ok=True)

    log.info(f"Created folder {folder}")

    # create solution.py
    solution = folder / "solution.py"
    if not solution.exists():
        solution.touch()
        log.info(f"Created file {solution}")
        solution.write_text(
            f"""from aocd import submit 

from aoc.utils import read_input, get_session_token

def part1(data):
    return 0

def part2(data):
    return 0

if __name__ == "__main__":
    data = read_input(day={day}, year={year})
    #submit(part1(data), part=1, day={day}, year={year}, session=get_session_token(), reopen=False)
    #submit(part2(data), part=2, day={day}, year={year}, session=get_session_token(), reopen=False)
"""
        )
    else:
        log.info(f"File {solution} already exists")

    # # create README
    # readme = folder / "README.md"
    # readme.touch()

    # # get contents from aoc website, convert to markdown and write to README
    # log.info("Getting data from aoc website")
    # log.info(f"https://adventofcode.com/{year}/day/{day}")

    # # only get body
    # soup = bs4.BeautifulSoup(
    #     requests.get(f"https://adventofcode.com/{year}/day/{day}").text,
    #     features="html.parser",
    # )
    # body = soup.find("article", {"class": "day-desc"})

    # # convert to markdown
    # readme.write_text(get_markdown(year, day))

    # create input.txt
    input = folder / "input.txt"

    session_token = pathlib.Path(__file__).parent.parent / "session_token.txt"

    # get data from aoc website
    data = get_data(year=year, day=day, session=session_token.read_text())
    input.write_text(data)


def create_year(year: int) -> None:
    """Create a folder for aoc year.

    Args:
        year (int): year

    Returns:
        None
    """

    for day in range(1, 26):
        create_day(year, day)


def update_current_year() -> None:
    """Update current year folder.

    Returns:
        None
    """

    # get current year
    log.info("Getting current year")

    current_year = time.localtime().tm_year
    current_day = time.localtime().tm_yday

    # current day - days until 1st december
    current_day = current_day - (335 if current_year % 4 == 0 else 334)

    log.info(f"Creating folders until day {current_day} of year {current_year}")

    # create folders
    for day in range(1, current_day + 1):
        create_day(current_year, day)


def get_session_token() -> str:
    """Get session token from root folder.

    Returns:
        str: session token
    """

    # get session token from aoc website
    log.info("Getting session token for aoc website")

    session_token = pathlib.Path(__file__).parent.parent / "session_token.txt"

    if not session_token.exists():
        log.error("Session token not found")
        return

    return session_token.read_text()
