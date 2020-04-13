from libradiko import radikotoday


def serchfromkey(keyword):
    radio = radikotoday()
    radio.change_keywords([keyword])
    res = radio.search()
    return res


def showtodaysradio():
    radio = radikotoday()
    radio.show()


def splitprint(ls):
    if ls == []:
        print(ls)
        return
    else:
        for item in ls:
            print(item)
        return


if __name__ == "__main__":
    splitprint(serchfromkey("中川緑"))
    # print(showtodaysradio())
