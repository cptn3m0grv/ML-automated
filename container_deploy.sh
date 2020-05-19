#!/bin/bash

if sudo cat /root/cats\ and\ dogs/CNN.py | grep keras
	then
		if sudo docker ps -a | grep neural
		then
			sudo docker rm -f neural
			sudo docker run -it -v /root/cats\ and\ dogs:/root --name neural pyos:v4
		else
			sudo docker run -it -v /root/cats\ and\ dogs:/root --name neura
l pyos:v4
                fi
elif sudo cat /root/cats\ and\ dogs/CNN.py | grep sklearn
then
	if sudo docker ps -a | grep lr
	then
		sudo docker rm -f lr
                sudo docker run -it -v /root/cats\ and\ dogs:/root --name lr pyos:v6
	else
		sudo docker run -it -v /root/cats\ and\ dogs:/root --name lr pyos:v6
        fi
else
	echo "Not a ML code"
fi
