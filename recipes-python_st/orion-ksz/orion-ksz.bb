SUMMARY = "Add ksz8463 python script to the filesystem"

LICENSE = "CLOSED"

inherit systemd

SRC_URI = "\
    file://ksz8463_ars.py \
    file://sel_copp_fib_ars.py \
    file://ksz8463_apk.py \
    file://sel_copp_fib_apk.py \
    file://ksz8463.service \
"

SYSTEMD_SERVICE_${PN} = "ksz8463.service"

do_install() {
    install -d ${D}/kepm/ksz
    install -d ${D}${systemd_unitdir}/system

    install -m 0644 ${WORKDIR}/ksz8463.service ${D}${systemd_unitdir}/system
    if [ ${ORION_DEVICE_TYPE} = "ars" ]; then
        install -m 0777 ${WORKDIR}/ksz8463_ars.py ${D}/kepm/ksz/ksz8463.py
        install -m 0777 ${WORKDIR}/sel_copp_fib_ars.py ${D}/kepm/ksz/sel_copp_fib.py
    elif [ ${ORION_DEVICE_TYPE} = "upza" ]; then
        # NOTE: UPZA has the same files as APK for now
        install -m 0777 ${WORKDIR}/ksz8463_apk.py ${D}/kepm/ksz/ksz8463.py
        install -m 0777 ${WORKDIR}/sel_copp_fib_apk.py ${D}/kepm/ksz/sel_copp_fib.py
    elif [ ${ORION_DEVICE_TYPE} = "apk_rx" ] || [ ${ORION_DEVICE_TYPE} = "apk_tx" ]; then
        install -m 0777 ${WORKDIR}/ksz8463_apk.py ${D}/kepm/ksz/ksz8463.py
        install -m 0777 ${WORKDIR}/sel_copp_fib_apk.py ${D}/kepm/ksz/sel_copp_fib.py
    fi
}

FILES_${PN} += "/kepm/ksz"
FILES_${PN} += "${system_unitdir}/system"
