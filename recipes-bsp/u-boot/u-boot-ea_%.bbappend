SRC_URI += "file://mx6sxea-com.h;subdir=git/include/configs \
            file://.config;subdir=git \
            "

FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

PACKAGE_ARCH = "imx6sxea-com"

