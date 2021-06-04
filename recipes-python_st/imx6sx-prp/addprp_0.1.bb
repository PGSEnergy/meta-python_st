SUMMARY = "Add prp stack to file system"
SECTION = "PRP"
LICENSE = "CLOSED"

SRC_URI = "file://sw_stack_prp1-master \
		   file://PRP.sh"

S = "${WORKDIR}"


do_install() {
	     install -d 777 ${D}/prp
		 cp -r ${WORKDIR}/sw_stack_prp1-master ${D}/prp/
	    #  install -d 777 sw_stack_prp1-master ${D}/prp/
		 install -m 777 PRP.sh ${D}/prp/
}

FILES_${PN} += "/prp"
