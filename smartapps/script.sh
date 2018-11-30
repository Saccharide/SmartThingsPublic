#!/bin/sh                                             
find `pwd` -type f -name "*.groovy" | while read i; do
    echo "$i"
    groovy_file=$(cat $i)
    defin="definition("
    descr="description: \""
    end="\","
    first_cut="${groovy_file#$defin*$descr}"
    echo "${first_cut%%$end*\}}"

done

