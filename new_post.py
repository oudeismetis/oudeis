from os import listdir

import tinify


tinify.key = ''


# https://tinypng.com/developers/reference/python
# pip install --upgrade tinify
def compress_folder(folder_name):
    for filename in listdir(folder_name):
        # https://github.com/oudeismetis/missed-moment/blob/master/export/usb.py
        full_path = f'{MEDIA_DIR}/{filename}'
        source = tinify.from_file(full_path)
        resized = source.resize(method='scale', width=400)
        resized.to_file("thumbnail.jpg")


if __name__ == '__main__':
    print('hello world')
