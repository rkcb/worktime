#!/usr/bin/python
import re
import sys
def ftToMins(ft):
    [hours, mins] = map(int, ft.split(":"))
    assert hours < 24
    assert mins < 60
    return hours * 60 + mins

def pauses(args):
    f = lambda t: re.search("^\d+$", t)
    ps = list(filter(f, args))
    assert max( map(len, ps) ) < 3, "Tauossa on vain yksi tai kaksi numeroa"
    return sum(map(int, ps))

def ends(ts):
    f = lambda t: re.search("^\d{1,2}:\d{2}$", t)
    es = list( filter(f , ts))
    assert len(es) < 3
    return es

def minsToFt(mins):
    hours = str(mins // 60)
    minutes = str(mins % 60)
    minutesStr = minutes if len(minutes) > 1 else "0" + minutes
    return hours + ":" + minutesStr

def workTime(args):
    es = ends(args)
    ps = pauses(args)
    sz = len(es)
    defWork = 7 * 60 + 36
    es = list(map(ftToMins, es))
    if sz == 2:
        start = min(es)
        end = max(es)
        total = end - start - ps
        mins = total % 60
        minsFormatted =  "0" + str(mins) if mins < 10 else str(mins)
        print("Lounastauko: " + str(ps) + " minuuttia")
        print("Työaika: " + str(total // 60) + ":" + minsFormatted)
    elif sz == 1:
        print("Lounastauko: " + str(ps) + " minuuttia")
        print("Kokonainen työpäivä päättyy " + minsToFt(min(es) + ps + defWork))
    else:
        print("Tarkista aloitus- ja lopetusaika")

if (len(sys.argv) < 2):
    print("Lisää työn aloitusaika ja mahdollinen tauko")
else:
    workTime(sys.argv)




