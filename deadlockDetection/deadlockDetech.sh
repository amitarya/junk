#! /usr/bin/env bash

# This scripts just checks if any thread of the process is not
# sleeping. If all the threads are sleeping it could be a deadlock.

process=$1

if [ "X$process" == "X" ];
then
	echo "Usage: ./deadlockdetech.sh <process-name>";	
fi

pid=`pgrep $1`
if [ -d "/proc/$pid/task" ];
then
	for i in `ls "/proc/$pid/task" `;
	do
		status=`cat /proc/$pid/task/$i/status | egrep -i '^state' | awk -F" " '{print $2}'`;
		if [ "X$status" != "XS" ];
		then
			echo "Not a deadlock";
			exit
		fi
	done
fi

echo "maybe a deadlock."

