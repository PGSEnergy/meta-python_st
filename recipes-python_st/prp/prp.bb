SUMMARY = "Add prp stack to file system"

LICENSE = "CLOSED"

SRC_URI = "\
    file://prp_stack \
    file://prp_conf.txt \
    file://prpstart.sh \
    file://prp.py \
    file://prpstop.sh \
"

S = "${WORKDIR}"

do_install() {
    install -d ${D}/kepm/prp

    install -m 777 prpstop.sh ${D}/kepm/prp
    install -m 777 prpstart.sh ${D}/kepm/prp

    install -m 777 prp.py ${D}/kepm/prp

    install -m 777 ${WORKDIR}/prp_stack ${D}/kepm/prp
    install -m 777 ${WORKDIR}/prp_conf.txt ${D}/kepm/prp
}

FILES_${PN} += "/kepm/prp"
