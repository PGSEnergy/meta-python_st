

FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

PACKAGE_ARCH = "imx6sxea-com"




SRC_URI = "git://github.com/PGSEnergy/linux.git;protocol=git;branch=${SRCBRANCH}"

SRCBRANCH = "UPZA"
SRCREV = "02f74e7a3dd19ddf9cffcccb2b038a91320fb0f6"
addtask copy_defconfig_vf after do_copy_defconfig before do_preconfigure

do_copy_defconfig_vf () {
	install -d ${B}
	mkdir -p ${B}
	cp ${S}/arch/arm/configs/ea_imx_defconfig ${B}/.config
        cp ${S}/arch/arm/configs/ea_imx_defconfig ${B}/../defconfig
}



