#!/bin/bash

read -p "Enter the URL : " url
wget "$url"
echo "$url" >> log.txt

echo "Completed!"
