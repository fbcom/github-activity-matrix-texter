# github-activity-matrix-texter
converts your github activity matrix into a text display by rewriting your git commit history


## Usage

```
$ python main.py -h
usage: main.py [-h] --text word [word ...] [--path dir] [--threshold n]
               [--font {5x3,5x4,5x5}] [--customfont customfont]
               [--fontpath fontpath] [--preview]

optional arguments:
  -h, --help            show this help message and exit
  --text word [word ...]
                        textmessage to render
  --path dir            path to your git repository
  --threshold n         minimum number of commits per day
  --font {5x3,5x4,5x5}  font selection
  --customfont customfont
                        font name i.e. "abc" if the font file is
                        "abc_font.txt"
  --fontpath fontpath   path to font files
  --preview             leave git repository untouched
```
