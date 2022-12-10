# upper case the first and the fourth letter of any name

def old_macdonald(name):
    macd = []
    macd.append(name[:3].title())
    macd.append(name[3::].title())
    mac = "".join(macd)
    print(mac)


old_macdonald('macdonald')
