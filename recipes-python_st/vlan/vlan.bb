SUMMARY = "Add vlan configuration script"

LICENSE = "CLOSED"

SRC_URI = "file://vlan.py"

do_install() {
    install -d ${D}/kepm/vlan
    install -m 0644 ${WORKDIR}/vlan.py ${D}/kepm/vlan
}

FILES:${PN} += "/kepm/vlan"
