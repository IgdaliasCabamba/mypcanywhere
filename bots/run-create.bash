#! /usr/bin/bash
cd ~/Ideas/MyPCAnyWhere
yarn create vite app --template svelte
virtualenv pyenv
git init .
touch .gitignore
git config core.excludesFile .gitignore