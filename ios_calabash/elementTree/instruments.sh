udid=$(ideviceinfo | grep UniqueDeviceID | awk '{ print $2}')

instruments -w $udid -t \
/Applications/Xcode.app/Contents/Applications/Instruments.app/Contents/PlugIns/\
AutomationInstrument.xrplugin/Contents/Resources/Automation.tracetemplate \
../vodeopass_automation_debug.ipa -e UIASCRIPT uiautomation.js \
-e UIARESULTSPATH .