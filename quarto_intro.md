#Quarto
Quarto is an open-source scientific and technical publishing system built on Pandoc

1. create doc.qmd file like [reference](https://quarto.org/)
2. install [quarto cli](https://quarto.org/docs/get-started/)
3. edit quarto report with prefered format
4. render the qmd file to document (supply pdf and docx), this may need some extra process and need to install some package in quarto cli or python env
```
quarto render test.qmd --to docx
quarto render test.qmd --to pdf
```
