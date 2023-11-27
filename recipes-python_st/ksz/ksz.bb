SUMMARY = "Add ksz8463 python script to the filesystem"

LICENSE = "CLOSED"

inherit systemd

SRC_URI = "\
    file://ksz8463.py \
    file://sel_copp_fib.py \
    file://ksz8463.service \
"

SYSTEMD_SERVICE:${PN} = "ksz8463.service"

do_install() {
    install -d ${D}/kepm/ksz
    install -d ${D}${systemd_unitdir}/system

    install -m 0755 ${WORKDIR}/ksz8463.py ${D}/kepm/ksz
    install -m 0755 ${WORKDIR}/sel_copp_fib.py ${D}/kepm/ksz

    install -m 0644 ${WORKDIR}/ksz8463.service ${D}${systemd_unitdir}/system
}

FILES:${PN} += "/kepm/ksz"
FILES:${PN} += "${system_unitdir}/system"
