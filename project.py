import os
import shutil
import sys

CSS_CACHE_PATH = './static/CACHE/css'


def clear_cache():
    '''Deletes all cached files from static CSS folder'''
    for filename in os.listdir(CSS_CACHE_PATH):
        file_path = os.path.join(CSS_CACHE_PATH, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


if 'clear_cache' in sys.argv:
    print('Clearing Cache...')
    clear_cache()
    print('Cache cleared!')
