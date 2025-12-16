# Add the article-theme-js script to all documents, if not already present

from os import chdir, listdir

chdir('../APUSH study')

for file in listdir():
    split = file.split()
    if split[len(split) - 1] == 'html':
        with open(file, 'rw') as content:
            if 'article-theme-js' not in content.read():
                modified = content.read().replace('</head>', '<script src="./article-theme-js/theme.js" defer></script>\n</head>')
                file.write(modified)
