import re

from enum import Enum


class LineType(Enum):
    SEQUENCE_NUMBER = "sequence_number"
    TIMESTAMP = "timestamp"
    SUBTITLE_TEXT = "subtitle_text"
    EMPTY_LINE = "empty_line"
    UNKNOWN = "unknown"


def merge(src_file01, src_file02, output_file):
    lines01 = src_file01.readlines()
    lines02 = src_file02.readlines()
    for l1, l2 in zip(lines01, lines02):
        print(f"LINE01 STRIPED {l1.strip()}")
        print(f"LINE02 STRIPED {l2.strip()}")
        merged_line = merge_lines(l1.strip("\n"), l2.strip("\n"))
        print(f"MERGED LINE: {merged_line}\n")
        output_file.write(merged_line + "\n")

    # Process the lines (e.g., merge subtitles)
    # merged_line = merge_lines(line1.strip('\n'), line2.strip('\n'))


def merge_lines(line01, line02):
    merged_line = ""
    line_type01 = identify_line_type(line01)
    line_type02 = identify_line_type(line02)
    if line_type01 != line_type02:
        raise ValueError("Lines are of different types and cannot be merged.")
    match line_type01:
        case LineType.SEQUENCE_NUMBER:
            line01 = int(line01)
            line02 = int(line02)
            if line01 != line02:
                raise ValueError("Line numbers do not match.")
            merged_line = str(line01)
        case LineType.TIMESTAMP:
            if line01 != line02:
                raise ValueError("Timestamps do not match.")
            merged_line = line01
        case LineType.SUBTITLE_TEXT:
            merged_line = f"{line01}\n{line02}"
    return merged_line


def identify_line_type(line):
    """
    Identifies the type of a subtitle line.

    Args:
        line (str): The subtitle line to analyze.

    Returns:
        LineType: The type of the line (SEQUENCE_NUMBER, TIMESTAMP, SUBTITLE_TEXT, EMPTY_LINE, UNKNOWN).
    """
    patterns = {
        LineType.SEQUENCE_NUMBER: re.compile(r"^\d+$"),
        LineType.TIMESTAMP: re.compile(
            r"^\d{2}:\d{2}:\d{2},\d{3}\s*-->\s*\d{2}:\d{2}:\d{2},\d{3}$"
        ),
        LineType.SUBTITLE_TEXT: re.compile(
            r'^<font color="#[a-fA-F0-9]{6}">.*</font>$'
        ),
        # LineType.EMPTY_LINE: re.compile(r'^\s*$')
    }

    for line_type, pattern in patterns.items():
        if pattern.match(line):
            return line_type

    return LineType.UNKNOWN
