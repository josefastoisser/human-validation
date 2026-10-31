"""Container helper only: retain each head's native row_id,class_id CSV."""
import argparse
from pathlib import Path
import zipfile


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--T1', required=True, type=Path)
    p.add_argument('--T2', required=True, type=Path)
    p.add_argument('--output', default='_submission.zip', type=Path)
    args = p.parse_args()
    with zipfile.ZipFile(args.output, 'x', compression=zipfile.ZIP_STORED) as z:
        for head in ['T1', 'T2']:
            info = zipfile.ZipInfo(head + '_submission.csv', date_time=(1980, 1, 1, 0, 0, 0))
            info.external_attr = 0o100644 << 16
            z.writestr(info, getattr(args, head).read_bytes())


if __name__ == '__main__':
    main()
