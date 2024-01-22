cd ~/Code/MCB185/data
gunzip -c dictionary.gz | grep "r" | grep -E "[acinorz]{2,5}[acinorz]" | wc -l
