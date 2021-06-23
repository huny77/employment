# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(name:str, company:str) -> str:
    company = company.lower()
    mapper = name.split(';')
    duplicate_counter = {}
    result = ""
    for i in range(len(mapper)):
        name = mapper[i].lstrip()
        item = name.lower().replace('-', '').split()
        first, last = item[0], item[-1]
        if len(last) > 8:
            last = last[:8]

        if first+last not in duplicate_counter:
            duplicate_counter[first+last] = 1
        else:
            duplicate_counter[first+last] += 1
            last += str(duplicate_counter[first+last])

        email = first + "." + last + "@" + company + ".com"
        result += (name + " " + "<" + email + ">; ")
    result = result.rstrip()[:-1]
    print(result)
    return result


s = "John Doe; Peter Benjamin Parker; Mary Jane Watson-Parker; John Elvis Doe; John Evan Doe; Jane Doe; Peter Brian Parker"
c = "example"
solution(s, c)
