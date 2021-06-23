INF = 999999999


def validate(size: str, date: str, name: str) -> bool:
    if name[-1] != '~':
        # backup file check
        return False

    # size check
    if 'K' not in size and 'M' not in size and 'G' not in size:
        return False
    if 'G' in size:
        return False
    if 'M' in size:
        temp = int(size[:-1])
        if temp >= 14:
            return False

    # date check
    date = int(date.replace('-', ''))
    if date <= 19900131:
        return False

    return True


def solution(S: str) -> str:
    files = S.split('\n')
    # condition
    # 1. include ~
    # 2.  size<14M
    # 3. 19900131< date
    cnt = INF
    for i in range(len(files)):
        size, date, name = files[i].lstrip().split()
        if validate(size, date, name):
            cnt = min(cnt, len(name[:name.index('.')]))

    return str(cnt) if cnt != INF else "NO FILES"


s = """ 715K 2009-09-23 system.zip~
 179K 2013-08-14 to-do-list.xml~
 645K 2013-06-19 blockbuster.mpeg~
  536 2010-12-12 notes.html
 688M 1990-02-11 delete-this.zip~
  23K 1987-05-24 setup.png~
 616M 1965-06-06 important.html
  14M 1992-05-31 crucial-module.java~
 192K 1990-01-31 very-long-filename.dll~"""
a = solution(s)
print(a)
