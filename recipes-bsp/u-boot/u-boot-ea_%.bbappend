SRC_URI += "file://mx6sxea-com.h;subdir=git/include/configs"

FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

PACKAGE_ARCH = "${MACHINE_ARCH}"

