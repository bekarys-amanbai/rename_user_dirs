#!/usr/bin/env python

# version: 0.2

import argparse
from pathlib import Path


langs = {
    'ru_RU': {
        'desktop': 'Рабочий стол',
        'download': 'Загрузки',
        'templates': 'Шаблоны',
        'publicshare': 'Общедоступные',
        'documents': 'Документы',
        'music': 'Музыка',
        'pictures': 'Изображения',
        'videos': 'Видео'
    },
    'en_US': {
        'desktop': 'Desktop',
        'download': 'Download',
        'templates': 'Templates',
        'publicshare': 'Publicshare',
        'documents': 'Documents',
        'music': 'Music',
        'pictures': 'Pictures',
        'videos': 'Videos'
    },
}


home = Path.home()
user_dirs = home / Path('.config/user-dirs.dirs')
user_dirs_locale = home / Path('.config/user-dirs.locale')

parser = argparse.ArgumentParser(
        description='Renames or creates (if not present) user \
                     folders and changes the ".config/user-dirs.dirs" \
                     and ".config/user-dirs.locale" files to the \
                     appropriate language.\
                     Currently only 2 languages are supported:\
                     ru_RU and en_US'
        )
parser.add_argument('lang_code_now', help='current folder language code (can be viewed in ".config/user-dirs.locale")')
parser.add_argument('lang_code_renaming', help='language code to which you want to rename folders')
args = parser.parse_args()

if args.lang_code_now not in langs or args.lang_code_renaming not in langs:
    raise ValueError('Error lang code')

current_dirs = langs[args.lang_code_now]
renamed_dirs = langs[args.lang_code_renaming]

user_dirs_str = ('# This file is written by xdg-user-dirs-update\n\
# If you want to change or add directories, just edit the line you\'re\n\
# interested in. All local changes will be retained on the next run.\n\
# Format is XDG_xxx_DIR="$HOME/yyy", where yyy is a shell-escaped\n\
# homedir-relative path, or XDG_xxx_DIR="/yyy", where /yyy is an\n\
# absolute path. No other format is supported.\n#\n')

user_dirs_str += '\n'.join([f'XDG_{k.upper()}_DIR="$HOME/{v}"'
                            for k, v in renamed_dirs.items()]) + '\n'

user_dirs.write_text(user_dirs_str)
user_dirs_locale.write_text(args.lang_code_renaming)

for folder in home.iterdir():
    if folder.is_dir():
        dir_name = str(folder).split('/')[-1]
        for k, v in current_dirs.items():
            if dir_name == v:
                folder.replace(home / renamed_dirs[k])
                dir_name += '"' #кастыль для красивого вывода
                print(f'renamed "{dir_name:<14}-> "{renamed_dirs[k]}"')

for folder in renamed_dirs.values():
    try:
        (home / folder).mkdir()
    except FileExistsError:
        continue
    print(f'create "{folder}"')
