#!/bin/bash
#Transsion Top Secret

MAKEFILE="$1"

if [ ! -f "${MAKEFILE}" ]
then
    exit 1
fi

grep -Hn '^[^#]* $' "$MAKEFILE"
if [ "$?" == 0 ]
then
    exit 1
else
    exit 0
fi
