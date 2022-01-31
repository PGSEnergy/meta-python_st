

FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

PACKAGE_ARCH = "imx6sxea-com"




SRC_URI = "git://github.com/Stefan12321/linux.git;protocol=git;branch=${SRCBRANCH}"
SRC_URI += "file://patch.patch;subdir=git/drivers/rpmsg \
            "
SRCBRANCH = "master"
SRCREV = "fe038afcce6fcbd034454034e40b82f0fc729ca5"
addtask copy_defconfig_vf after do_copy_defconfig before do_preconfigure

do_copy_defconfig_vf () {


install -d ${B}
	mkdir -p ${B}
	cp ${S}/arch/arm/configs/ea_imx_defconfig ${B}/.config
        cp ${S}/arch/arm/configs/ea_imx_defconfig ${B}/../defconfig
}



