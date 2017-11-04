#!/bin/bash

#main gen
number=$1
curl "https://www.searchbug.com/tools/landline-or-cellphone.aspx?FULLPHONE=$number" | head -n385 | tail -n60 > tmp
#end main gen

#init variables
tmpv=`cat tmp | grep -in "Phone Type:" | cut -d":" -f1`
type=`cat tmp | head -n$(($tmpv+2)) | tail -n1`

tmpv=`cat tmp | grep -in "Carrier:" | cut -d":" -f1`
carrier=`cat tmp | head -n$(($tmpv+2)) | tail -n1`

tmpv=`cat tmp | grep -in "Time Zone:" | cut -d":" -f1`
tZone=`cat tmp | head -n$(($tmpv+1)) | tail -n1 | cut -d">" -f2 | cut -d"<" -f1`

tmpv=`cat tmp | grep -in "Time at Location:" | cut -d":" -f1`
locTime=`cat tmp | head -n$(($tmpv+1)) | tail -n1 | cut -d">" -f2 | cut -d"<" -f1`

tmpv=`cat tmp | grep -n ">Location:" | cut -d":" -f1`
location=`cat tmp | head -n$(($tmpv+1)) | tail -n1 | cut -d">" -f2 | cut -d"<" -f1`

tmpv=`cat tmp | grep -in "Local Calling Area:" | cut -d":" -f1`
loCalAre=`cat tmp | head -n$(($tmpv+1)) | tail -n1 | cut -d">" -f2 | cut -d"<" -f1`

tmpv=`cat tmp | grep -in "Area Code:" | cut -d":" -f1`
areaCode=`cat tmp | head -n$(($tmpv+1)) | tail -n1 | cut -d">" -f2 | cut -d"<" -f1`
#end variables

#start options
if [[(-n $2)]]; then
	case "$2" in
		"-type")	echo $type;;
		"-carrier")	echo $carrier;;
		"-timezone")	echo $tZone;;
		"-localtime")	echo $locTIme;;
		"-location")	echo $location;;
		"-callarea")	echo $loCalAre;;
		"-areacode")	echo $areaCode;;
	esac
else
	echo -e "\n"
	echo "Phone Type: $type"
	echo
	echo "Carrier: 	$carrier"
	echo
	echo "Time Zone:		$tZone"
	echo
	echo "Local Time:		$locTime"
	echo
	echo "Location:		$location"
	echo
	echo "Local Calling Area:	$loCalAre"
	echo
	echo "Possible Area Codes:	$areaCode"
fi
rm tmp
