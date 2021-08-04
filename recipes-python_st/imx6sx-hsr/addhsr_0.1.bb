SUMMARY = "Add HSR python script to file system"
SECTION = "HSR"
LICENSE = "CLOSED"

SRC_URI = "file://HSR.py"

S = "${WORKDIR}"


do_install() {
	     install -d 777 ${D}/kepm/hsr
	     install -m 777 HSR.py ${D}/kepm/hsr/
}

FILES_${PN} += "/kepm/hsr"