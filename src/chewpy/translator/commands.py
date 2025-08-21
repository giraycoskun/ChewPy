"""CLI Commands for Translator

Features:

* Subtitle merging
"""

from pathlib import Path
import tempfile
import shutil
from loguru import logger
from typer import Typer

from chewpy.translator.subtitles import merge

app = Typer()


@app.command()
def subtitles_merge(source_01_path: Path, source_02_path: Path) -> None:
    """Merges two subtitle files.

    Args:
        source_01_path (Path): The path to the first subtitle file.
        source_02_path (Path): The path to the second subtitle file.
    """
    output_path: Path = (
        source_01_path.parent
        / f"{source_01_path.stem}_merged_{source_02_path.stem}{source_02_path.suffix}"
    )
    logger.debug(f"Output Path: {output_path}")
    with (
        open(source_01_path, "r", encoding="utf-8") as file1,
        open(source_02_path, "r", encoding="utf-8") as file2,
        tempfile.NamedTemporaryFile(mode="w", encoding="utf-8") as tmp_file,
    ):
        logger.debug(f"Temporary file created: {tmp_file.name}")
        try:
            merge(file1, file2, tmp_file)
            tmp_file.flush()
            shutil.move(tmp_file.name, output_path)
        except ValueError as e:
            logger.error(f"Error merging subtitles: {e}")


if __name__ == "__main__":
    subtitles_merge(Path("./tests/data/test1.srt"), Path("./tests/data/test2.srt"))
