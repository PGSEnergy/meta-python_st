
do_cop() {
  cp ~/ea-bsp/sources/meta-python_st/recipes-bsp/u-boot/u-boot-ea/imx6sxea-com/defconfig ${WORKDIR}/.config
}
addtask do_cop after do_configure before do_compile
