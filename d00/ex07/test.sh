#!/bin/bash
python3 filterwords.py "Hello, my friend" 3
echo ""
python3 filterwords.py "A robot must protect its own existence as long as such protection does not conflict with the First or Second Law" 6
echo ""
python3 filterwords.py Hello World
echo ""
python3 filterwords.py 300 3