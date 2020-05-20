#!/bin/bash

acc_str=$(sudo tail -1 /root/cats\ and\ dogs/output.txt)
acc_int=$acc_str | bc -l

if [ $acc_int >= 85 ]
then
	exit 0
else
    sudo cd /root/cats\ and\ dogs/
    sudo python3 tweak.py
    sudo git add CNN.py
    sudo git commit CNN.py -m "Change made"
fi
