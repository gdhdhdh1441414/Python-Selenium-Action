import time
import re
import sys

html = os.system ("sudo python src/flaresolverr.py & sleep 3 && curl  'http://localhost:8191/v1' -H 'Content-Type: application/json' --data '{  \"cmd\": \"request.get\",  \"url\":\"https://sharemania.us/\",  \"maxTimeout\": 60000}'")
print (html);
