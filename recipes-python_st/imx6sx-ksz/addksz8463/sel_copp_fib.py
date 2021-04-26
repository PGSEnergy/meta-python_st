import ksz8463


if ksz8463.ksz.spitest_silence() == '0X8443':
    ksz8463.ksz.sel_copp_fib()
else:
    print("Spi doesn't work right. Ksz mode not selected")  
