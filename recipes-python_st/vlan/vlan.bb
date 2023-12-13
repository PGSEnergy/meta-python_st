SUMMARY = "Add vlan configuration script"

LICENSE = "CLOSED"

SRC_URI = "file://vlan.py"

do_install() {
    install -d ${D}/kepm/vlan
    install -m 0777 ${WORKDIR}/vlan.py ${D}/kepm/vlan
}

FILES:${PN} += "/kepm/vlan"
