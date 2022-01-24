SRC_URI += "file://imx6sxea-com-kit.dts;subdir=git/arch/${ARCH}/boot/dts \
            file://imx6sx-board.dtsi;subdir=git/arch/${ARCH}/boot/dts \
            file://imx6sxea-com.dtsi;subdir=git/arch/${ARCH}/boot/dts \
            file://imx6sxea-com-kit_v2.dts;subdir=git/arch/${ARCH}/boot/dts \
            file://imx6sxea-com-kit_v2-m4.dts;subdir=git/arch/${ARCH}/boot/dts \
	    file://patch.patch;subdir=git/drivers/rpmsg \
            file://.config;subdir=git/build \
  	    file://imx6sx.dtsi;subdir=git/arch/${ARCH}/boot/dts \
            "

FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

PACKAGE_ARCH = "imx6sxea-com"

