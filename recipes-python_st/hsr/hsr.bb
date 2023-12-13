SUMMARY = "Add HSR python script to the filesystem"

LICENSE = "CLOSED"

S = "${WORKDIR}"

SRC_URI = "\
    file://HSR.py \
    file://ksz8463.py \
    file://mac.txt \
"

do_install() {
    install -d ${D}/kepm/hsr

    install -m 0777 ${WORKDIR}/HSR.py ${D}/kepm/hsr
    install -m 0777 ${WORKDIR}/ksz8463.py ${D}/kepm/hsr
    install -m 0777 ${WORKDIR}/mac.txt ${D}/kepm/hsr
}

FILES:${PN} += "/kepm/hsr"
