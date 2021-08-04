SUMMARY = "Add prp stack to file system"
SECTION = "PRP"
LICENSE = "CLOSED"

SRC_URI = "file://sw_stack_prp1-master \
		   file://PRP.sh \
		   file://PRP.py \
		   file://end.sh"

S = "${WORKDIR}"


do_install() {
	     install -d 777 ${D}/kepm/prp
		 cp -r ${WORKDIR}/sw_stack_prp1-master ${D}/kepm/prp/
		 install -m 777 PRP.sh ${D}/kepm/prp/
		 install -m 777 end.sh ${D}/kepm/prp/
		 install -m 777 PRP.py ${D}/kepm/prp/
}

FILES_${PN} += "/kepm/prp"
