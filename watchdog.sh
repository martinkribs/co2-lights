
#!/bin/sh
/bin/python3 /home/pi/serialReadAllOutput.py &
echo "$(date +'%T')-CO2 Script was started with the pi" >> /home/pi/log.txt
