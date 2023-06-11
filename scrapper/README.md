- [Jupyter](#jupyter)
  - [Interactive Mode on binder](#interactive-mode-on-binder)
  - [Interactive Mode in google colab](#interactive-mode-in-google-colab)
  - [Static Output of Jupyter Notebook at Github](#static-output-of-jupyter-notebook-at-github)
  - [Static Output of jupter Notebook at Nbviwer](#static-output-of-jupter-notebook-at-nbviwer)
- [Docker](#docker)
  - [Dockerfile](#dockerfile)
  - [Docker compose file](#docker-compose-file)
- [Run Docker](#run-docker)


Some cases for some reason the conection to website stuck https://www.bbc.com on that case just interrupt and try again

# Jupyter

## Interactive Mode on binder
https://mybinder.org/v2/gh/SeekingAura/jupyter-examples/master?filepath=/scrapper/article_collector.ipynb

## Interactive Mode in google colab
https://githubtocolab.com/SeekingAura/jupyter-examples/blob/master/scrapper/article_collector.ipynb

## Static Output of Jupyter Notebook at Github
https://github.com/SeekingAura/jupyter-examples/blob/master/scrapper/article_collector.ipynb

## Static Output of jupter Notebook at Nbviwer
https://nbviewer.org/github/SeekingAura/jupyter-examples/blob/master/scrapper/article_collector.ipynb

# Docker
Container

## Dockerfile
https://github.com/SeekingAura/jupyter-examples/blob/master/scrapper/Dockerfile

## Docker compose file
https://github.com/SeekingAura/jupyter-examples/blob/master/scrapper/docker-compose.yaml
# Run Docker
```
docker-compose -f docker-compose.yaml up --build -d
```
