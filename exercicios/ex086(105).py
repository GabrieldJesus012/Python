def notas(*num,situação=False):
    r = {}
    r ["total"] = len(num)
    r ["maior"] = max(num)
    r ["menor"] = min(num)
    r["media"] = sum(num)/r["total"]
    if situação == True:
        if r["media"]<5:
            r ["situação"] = "RUIM"
        elif r["media"]<7:
            r ["situação"] = "RAZOAVEL"
        else:
            r ["situação"] = "BOA"
    return r

resp = notas(5.5,2.5,1.5,situação=True)
print(resp)
