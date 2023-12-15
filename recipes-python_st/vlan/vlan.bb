SUMMARY = "Add vlan configuration script"

LICENSE = "CLOSED"

SRC_URI = "\
    file://vlan_ars.py \
    file://vlan_apk.py \
"

do_install() {
    install -d ${D}/kepm/vlan

    if [ ${ORION_DEVICE_TYPE} = "ars" ]; then
        install -m 0777 ${WORKDIR}/vlan_ars.py ${D}/kepm/vlan/vlan.py
    elif [ ${ORION_DEVICE_TYPE} = "upza" ]; then
        true # a placeholder
    elif [ ${ORION_DEVICE_TYPE} = "apk_rx" ] || [ ${ORION_DEVICE_TYPE} = "apk_tx" ]; then
        install -m 0777 ${WORKDIR}/vlan_apk.py ${D}/kepm/vlan/vlan.py
    fi
}

FILES_${PN} += "/kepm/vlan"
