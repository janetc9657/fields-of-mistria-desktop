"""Fields of Mistria Desktop — A local helper for Fields of Mistria farm folders, magic notes, and season photos."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='fields_of_mistria_desktop',
        description='A local helper for Fields of Mistria farm folders, magic notes, and season photos.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Fields of Mistria Desktop')
    print('Keep the farm on disk before the next content drop.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
# update note (2026-11-03)
# tune (2026-11-03)
# wip (2026-11-05)
# small fix (2026-11-06)
# tune (2026-11-06)
# tune (2026-11-16)
# update note (2026-11-16)
# tweak (2026-11-17)
# minor adjust (2026-11-17)
# minor adjust (2026-11-17)
# polish (2026-11-17)
# tweak (2026-11-23)
# refactor bit (2026-11-24)
# update note (2026-11-24)
# update note (2026-11-24)
