SUMMARY = "Add prp stack to file system"

LICENSE = "CLOSED"

inherit systemd

SRC_URI = "\
    file://prp_stack \
    file://prp_conf.txt \
    file://prpstart.sh \
    file://prp.py \
    file://prpstop.sh \
    file://prp.service \
"

DEPEDS = "libpcap"
RDEPENDS:${PN} = "libpcap"

S = "${WORKDIR}"

SYSTEMD_SERVICE:${PN} = "prp.service"
SYSTEMD_AUTO_ENABLE:${PN} = "disable"

do_install() {
    install -d ${D}/kepm/prp
    install -d ${D}${systemd_unitdir}/system

    install -m 0777 ${WORKDIR}/prpstop.sh ${D}/kepm/prp
    install -m 0777 ${WORKDIR}/prpstart.sh ${D}/kepm/prp

    install -m 0777 ${WORKDIR}/prp.py ${D}/kepm/prp

    install -m 0777 ${WORKDIR}/prp_stack ${D}/kepm/prp
    install -m 0777 ${WORKDIR}/prp_conf.txt ${D}/kepm/prp

    install -m 0644 ${WORKDIR}/prp.service ${D}${systemd_unitdir}/system
}

FILES:${PN} += "/kepm/prp"
FILES:${PN} += "${systemd_unitdir}/system"
