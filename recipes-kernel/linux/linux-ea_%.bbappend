

FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

PACKAGE_ARCH = "imx6sxea-com"




SRC_URI = "git://github.com/PGSEnergy/linux.git;protocol=git;branch=${SRCBRANCH}"

SRCBRANCH = "APK"
SRCREV = "a18fcee4718724353e4b82c825aa96f993a681dd"
addtask copy_defconfig_vf after do_copy_defconfig before do_preconfigure

do_copy_defconfig_vf () {
	install -d ${B}
	mkdir -p ${B}
	cp ${S}/arch/arm/configs/ea_imx_defconfig ${B}/.config
        cp ${S}/arch/arm/configs/ea_imx_defconfig ${B}/../defconfig
}



