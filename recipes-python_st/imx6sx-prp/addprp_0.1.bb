SUMMARY = "Add prp stack to file system"
SECTION = "PRP"
LICENSE = "CLOSED"

SRC_URI = "file://sw_stack_prp1-master \
		   file://PRP.sh \
		   file://start.py \
		   file://end.sh"

S = "${WORKDIR}"


do_install() {
	     install -d 777 ${D}/prp
		 cp -r ${WORKDIR}/sw_stack_prp1-master ${D}/prp/
		 install -m 777 PRP.sh ${D}/prp/
		 install -m 777 end.sh ${D}/prp/
		 install -m 777 start.py ${D}/prp/
}

FILES_${PN} += "/prp"
