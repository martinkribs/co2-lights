
#!/bin/sh
/bin/python3 /home/pi/co2-lights-main/serialReadAllOutput.py &
echo "$(date +'%T')-CO2 Script was started with the pi" >> /home/pi/co2-lights-main/log.txt
