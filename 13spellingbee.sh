cd ~/Code/MCB185/data
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "r" | grep -v "[^acinorz]"| grep -E ".{4}" | wc -l
