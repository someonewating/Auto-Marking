a={'0':'a','1':'b','2':'c','3':'d','4':'e'}
mul='qqq'
client_count=6

def  test(count,module):
    delta_count = count - int(max(a))
    new_a = {}
    for i in range(delta_count):
        new_a[str(i)] = module

    for k, v in a.items():
        new_a[str(int(k) + delta_count)] = v

    return new_a

r=test(client_count,mul)
print(r)
