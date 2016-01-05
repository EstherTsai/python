#!/bin/bash

#echo "BUNDLE_ID= : $1"
export "BUNDLE_ID=com.kkbox.videoplatform"


#列出所有 usb 裝置
#udid=$(system_profiler SPUSBDataType | sed -n -e '/iPad/,/Serial/p' -e '/iPhone/,/Serial/p' | grep "Serial Number:" | awk -F ": " '{printf $2}')
udid=$(ideviceinfo | grep UniqueDeviceID | awk '{ print $2}')
echo $udid

#echo "DEVICE_TARGET : $2"
export DEVICE_TARGET=$udid

echo "DEVICE_ENDPOINT : $1"
export DEVICE_ENDPOINT=$1

bundle exec calabash-ios console 

#> start_test_server_in_background


