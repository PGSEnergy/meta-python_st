SUMMARY = "Add HSR python script to the filesystem"

LICENSE = "CLOSED"

SRC_URI = "\
    file://HSR.py \
    file://ksz8463.py \
    file://mac.txt \
"

do_install() {
    install -d ${D}/kepm/hsr

    install -m 0755 ${WORKDIR}/HSR.py ${D}/kepm/hsr
    install -m 0755 ${WORKDIR}/ksz8463.py ${D}/kepm/hsr
    install -m 0644 ${WORKDIR}/mac.txt ${D}/kepm/hsr
}

FILES:${PN} += "/kepm/hsr"
