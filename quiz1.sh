echo "Akshat Khandelwal"
echo $USER

gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "a" | grep -v "[^acfmotu]"| grep -E ".{4}" | wc -l

gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "b" | grep -v "[^abilnrt]"| grep -E ".{4}" | wc -l

gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "c" | grep -v "[^acdimno]"| grep -E ".{4}" | wc -l

gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "z" | grep -v "[^aginorz]"| grep -E ".{4}" | wc -l


gunzip -c ~/Code/MCB185/data/jaspar2024_core.transfac.gz | grep -v "^#"| cut -f 3 | sort -n | uniq -c | grep "tax_group"

echo "Yutong and Roger"
