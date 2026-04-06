#!/bin/bash

read -p "Do you want to update citations (y/n)? " update_citations
if [ "$update_citations" == "y" ]; then
    python ./_cite/cite.py
fi

read -p "Do you want to serve or build (s/b)? " serve_build
if [ "$serve_build" == "s" ]; then
    bundle exec jekyll serve
elif [ "$serve_build" == "b" ]; then
    bundle exec jekyll build
fi

read -p "Do you want to sync the site (y/n)? " sync_site
if [ "$sync_site" == "y" ]; then
    lftp -u "saktiwww@chem.waseda.ac.jp", "nB7@w^@IlkK8" -e "set ssl:verify-certificate no; mirror -R _site/ /; quit" ftp://www255.conoha.ne.jp
fi
#
#read -p "Do you want to sync to GitHub (y/n)? " sync_github
#if [ "$sync_github" == "y" ]; then
#    git add .
#    git commit -m "Update site"
#    git push origin main
#fi
