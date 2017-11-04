#!/bin/bash

staticIp=`wget http://ipecho.net/plain -O - -q`
echo $staticIp
