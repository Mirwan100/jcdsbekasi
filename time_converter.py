def timeConverter(bil) :

    if type(bil) != int or bil > 359999 or bil < 0 :
        return "invalid input"
    if bil < 60 :
        jam = 0
        menit = 0
        detik = bil
    elif bil > 60 and bil < 3600 :
        jam = 0
        menit = bil // 60
        detik = bil - 60*menit
    else :
        jam = bil // 3600
        menit = (bil - (3600*jam) )// 60
        detik = bil - jam*3600 - menit*60

    if jam < 10 :
        jam = "0%s" % (jam)
    if menit < 10 :
        menit = "0%s" % (menit)
    if detik < 10 :
        detik = "0%s" % (detik)
    bcg = "%s:%s:%s"%(jam, menit, detik)
    return bcg

print(timeConverter('a'))