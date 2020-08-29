## html_crawler

This script takes 2 html files (--source_file, --diff_file) searchs for --element on source and finds the most similar element on diff file.

It uses xpath to locate elements.
*Returns*: the location of the element in diff_file


###Requirements:
python3
lxml to parse the files

`pip3 install lxml`




## To execute:
python3 html_crawler.py -s <source_file> -e <element_id> -d <diff_file>

*Example*:
`
python3 html_crawler.py -s inputs/sample-0-origin.html -e make-everything-ok-button -d inputs/sample-1-evil-gemini.html

/html/body/div/div/div[3]/div[1]/div/div[2]/a[2]

`

## TODO
- Error handling