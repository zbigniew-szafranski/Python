from csv import DictReader
from typing import List, Dict, Any
import click

class Entry:
    def __init__(self, desc: str, time: int, tags: str) -> None:
        self.desc = desc
        self.time = time
        self.tags = tags

    def __repr__(self) -> str:
        return f"Entry(desc={self.desc!r}, time={self.time!r}, tags={self.tags!r})"

    def __str__(self) -> str:
        return f"{self.desc} {self.time} {self.tags}"

class TagSummaries:
    def __init__(self, tag: str, time: int) -> None:
        self.tag = tag
        self.time = time

    def __str__(self) -> str:
        return f"{self.time:10d} #{self.tag}"

    def get_sorting_key(self) -> int:
        return self.time


def divide_tags(tags: str) -> List[str]:
    return tags.split()


def create_entry(row: Dict[str, str]) -> Entry:
    return Entry(desc=row['desc'],
                time=int(row['time']),
                tags=row['tags'])


def load_entries(csv_file: str) -> List[Entry]:
    with open(csv_file) as stream:
        reader = DictReader(stream)
        tracks = [create_entry(row) for row in reader]
    return tracks


def all_tags(tracks: List[Entry]) -> set[str]:
    return set(tag for track in tracks for tag in divide_tags(track.tags))


def tag_time(tag: str, tracks: List[Entry]) -> int:
    return sum(track.time
               for track in tracks
               if tag in divide_tags(track.tags))


def prepare_tag_summaries(tracks: List[Entry]) -> List[TagSummaries]:
    if not tracks:
        return []
    try:
        tags = all_tags(tracks)
        summaries = [TagSummaries(tag, tag_time(tag, tracks)) for tag in tags]
        summaries.sort(key=lambda x: x.get_sorting_key(), reverse=True)
        return summaries
    except Exception as e:
        print(f"Error occurred while preparing tag summaries: {str(e)}")
        return []


def print_track(summaries: List[TagSummaries]) -> None:
    print("TOTAL-TIME TAG")
    for sum_ in summaries:
        print(sum_)

@click.command()
@click.argument("csv_file")
def main(csv_file: str):
    entries = load_entries(csv_file)
    summaries = prepare_tag_summaries(entries)
    print_track(summaries)


if __name__ == "__main__":
    main()