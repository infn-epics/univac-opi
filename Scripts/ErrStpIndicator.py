from org.csstudio.display.builder.runtime.script import PVUtil, ScriptUtil

#Get info from macros
prefx = widget.getEffectiveMacros().getValue("P")
mydev = widget.getEffectiveMacros().getValue("R")

if 'VGA' in mydev:
    pvName=PVUtil.createPV(prefx+":ERROR",100)
    pv_value=PVUtil.getString(pvName)
    if 'No error' in pv_value:
        pv_value="OK"
    else:
        pv_value="ERR"
else:
    pvName=PVUtil.createPV(prefx+":"+mydev+":STPTSTAT_RB",100)
    pv_value=PVUtil.getString(pvName)

widget.setPropertyValue('text',pv_value)
