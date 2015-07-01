#! /usr/bin/env bash


./rot64 .links

echo $1 >> output.txt

mv output.txt .links

./rot64 .links

mv output.txt .links
