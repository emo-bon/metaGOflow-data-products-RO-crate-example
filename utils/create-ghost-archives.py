#! /usr/bin/env python3

from pathlib import Path
import sys
import os
import logging as log
import argparse
import textwrap
import subprocess
import shutil

desc = """
Create Ghost Archives for MetaGOflow Data Products

This script creates a 'ghost' archive of a bzipped
tarball of the MetaGOflow run archive where the archive
consists of all the files but without any file content
"""


def main(target_directory, debug):
    """Create Ghost Archives for MetaGOflow Data Products

    This script creates a 'ghost' archive of a bzipped
    tarball of the MetaGOflow run archive where the archive
    consists of all the files but without any file content
    """

    # Logging
    if debug:
        log_level = log.DEBUG
    else:
        log_level = log.INFO
    log.basicConfig(format="\t%(levelname)s: %(message)s", level=log_level)

    # Check the target_directory name
    target_directory = Path(target_directory)
    if not target_directory.exists():
        log.error(f"Cannot find the target directory {target_directory}")
        sys.exit()
    log.debug(f"Found target directory {target_directory}")

    # CD to target directory
    log.info(f"Changing directory to {target_directory}")
    home_dir = Path.cwd()
    os.chdir(target_directory)

    # Get list of tarball files
    tarball_files = list(Path.cwd().glob("*.tar.bz2"))

    log.debug(f"Found {len(tarball_files)} tarball files")
    for tarball in tarball_files:
        log.debug(f"Tarball: {tarball}")
        log.debug(f"Tarball name: {tarball.name}")
    tarball_files = [f.name for f in tarball_files]
    if len(tarball_files) == 0:
        log.error(f"Cannot find any tarball files in {target_directory}")
        sys.exit()

    # Un bzip the tarballs
    for tarball_file in tarball_files:
        run_id = Path(str(tarball_file).rsplit(".", 2)[0])
        log.debug(f"run_id = {run_id}")

        if run_id.exists():
            log.debug("Found open archive")
        else:
            log.info(f"Opening archive {tarball_file}...")
            subprocess.call(["tar", "-xjf", f"{tarball_file}"])
            # Archive without top level directory
            if not run_id.exists():
                log.debug(f"Checking for broken archive at {run_id}")
                yml_files = Path.cwd().glob("*.yml")
                log.debug(f"Found {yml_files} yml files")
                if not len(yml_files) == 2:
                    log.error(f"Found {len(yml_files)} yml files")
                    sys.exit()
                if Path("results").exists():
                    log.debug("Found broken archive")
                    Path(run_id).mkdir()
                    Path("results").rename(Path(run_id, "results"))
                    for yf in yml_files:
                        yf.rename(Path(run_id, yf.name))
                else:
                    log.error(f"Archive looks completely broken at {tarball_file}")
                    sys.exit()

        # Recursive glob the open archive
        archive_files = run_id.rglob("*")

        # Make ghost archive structure
        ghost_dir = Path(f"{run_id}" + "-ghost")
        ghost_dir.mkdir(exist_ok=False)
        Path(ghost_dir, "results").mkdir()
        Path(ghost_dir, "results", "sequence-categorisation").mkdir()
        Path(ghost_dir, "results", "functional-annotation", "stats").mkdir(parents=True)
        Path(ghost_dir, "results", "taxonomy-summary", "LSU").mkdir(parents=True)
        Path(ghost_dir, "results", "taxonomy-summary", "SSU").mkdir()
        for af in archive_files:
            nfp = Path(ghost_dir, *af.parts[1:])
            log.debug(f"Writing {nfp}")
            nfp.touch()
        log.info(f"Created ghost archive for {run_id}")

        # Remove the open archive
        shutil.rmtree(run_id)

    # CD back to home directory
    log.info(f"Changing directory to {home_dir}")
    os.chdir(home_dir)

    log.info("Done")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(desc),
    )
    parser.add_argument(
        "target_directory",
        help="Name of target directory containing MetaGOflow output",
    )
    parser.add_argument("-d", "--debug", action="store_true", help="DEBUG logging")
    args = parser.parse_args()
    main(args.target_directory, args.debug)
