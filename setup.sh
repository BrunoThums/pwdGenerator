#!/bin/bash

echo -e "\033[36m Installing Python package... \033[0m"
pip install termcolor
echo -e "\033[36m Downloading python script... \033[0m"
wget https://raw.githubusercontent.com/BrunoThums/pwdGenerator/main/pwdGenerator.py
mv pwdGenerator.py pwdGenerator
chmod +x pwdGenerator
echo -e "\033[36m Moving script to path \033[0m"
mv pwdGenerator /usr/bin/pwdGenerator
echo -e "\033[36m Done! You can now use pwdGenerator anywhere :) \n Goodbye! \033[0m"
rm setup.sh
