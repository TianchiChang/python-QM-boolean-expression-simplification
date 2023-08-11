from itertools import product

class List():
    def __init__(self):
        self.component = []
        self.ones = 0
        self.flag = 0
        self.binary = [0,0,0,0,0,0,0,0]

class Decimal():
    def __init__(self):
        self.value = 0
        self.comp_time = 0
        self.corresponding = []
        self.final = []

def expand_list(list1,comp1):
    if 2 in comp1:
        comp2 = comp1[:]
        comp1[comp1.index(2)] = 0
        comp2[comp2.index(2)] = 1
        list1.append(comp2)
    # if 2 in comp1:
        expand_list(list1, comp1)
        expand_list(list1, comp2)

def compare_binary(comp1,comp2):
    unmatch = 0
    tmp = comp1[:]
    for i in range(8):
        if comp1[i]!=comp2[i]:
            tmp[i] = 2
            unmatch+=1
    if unmatch>1:
        return 0
    else:
        return tmp

def check_flag(flag):
    check = 0
    for i in flag:
        if i.flag==0:
            output.append(i)
            output_binary.append(i.binary)
        else:
            check = 1
    if check==0:
        return 0
    else:
        return 1

def de_identical(list0,list1):
    a = 0
    d = len(list0)-1
    while a <= d:
        b = a+1
        c = len(list0)-1
        while b <= c:
            if list0[a] == list0[b]:
                list0.pop(b)
                list1.pop(b)
                b -= 1
            b += 1
            c = len(list0) - 1
        a += 1
        d = len(list0) - 1
    return list1

def de_identical0(list0):
    a = 0
    d = len(list0)-1
    while a <= d:
        b = a+1
        c = len(list0)-1
        while b <= c:
            if list0[a] == list0[b]:
                list0.pop(b)
                b -= 1
            b += 1
            c = len(list0) - 1
        a += 1
        d = len(list0) - 1
    return list0

def de_identical1(output):
    output = [list(i) for i in set(map(tuple, output))]
    return output

def get_index(lst,item):
    return [index for (index,value) in enumerate(lst) if value == item]

def print_result(result,max_bit):
    out_dict1 = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H"}
    out_dict2 = {1:"A'",2:"B'",3:"C'",4:"D'",5:"E'",6:"F'",7:"G'",8:"H'"}
    to_print = 'Y = '
    for i in range(len(result)):
        for j in range(max_bit):
            if result[i][8-max_bit+j]==1:
                to_print = f'{to_print}{out_dict1[j+1]}'
            elif result[i][8-max_bit+j]==0:
                to_print = f'{to_print}{out_dict2[j+1]}'
        if i<len(result)-1:
            to_print = f'{to_print} + '
    return to_print

total = []
total_next = []
output = []
output_binary = []
output_component = []
decimals = []
decimals_value = []
print("您可以选择三种方式输入：\n方式1：Y=",chr(931),"(eg:6,7,0,4,2)\n方式2：Y=（eg:11X+111+XX0)\n方式3：Y=(eg:AB+ABC+C')\n")
choose = input("您选择:(1/2/3)  ")
if choose=='1':
    inp1 = input("请输入数字:").split(",")
    inp1 = list(set(inp1))
    for x in range(len(inp1)):
        exec("decimals%s=Decimal()"%x)
        exec("decimals.append(decimals%s)"%x)
        decimals[x].value = int(inp1[x])
        decimals_value.append(int(inp1[x]))
    dec_num = len(decimals)
    
    # for i in decimals:
    #     if i.value==0:
    #         decimals.remove(i)
    #         decimals_value.remove(i.value)
    #         dec_num-=1
    
    # have_zero = 0
    # for i in decimals:
    #     if i.value==0:
    #         have_zero = 1
    # if have_zero==0:
    #     dec_num+=1
    #     exec("decimals%s=Decimal()"%dec_num)
    #     exec("decimals.append(decimals%s)"%dec_num)
    #     decimals[dec_num-1].value = 0
    
    max_bit = 0
    for i in range(dec_num):
        current_bit = 0
        exec("list0_%s=List()"%i)
        exec("total.append(list0_%s)"%i)
        total[i].component.append(decimals[i].value)
        tmp = []
        tmp0 = decimals[i].value
        while tmp0>1:
            if tmp0%2==1:
                tmp.append(1)
                tmp0 = (tmp0-1)/2
            else:
                tmp.append(0)
                tmp0 = tmp0/2
            current_bit+=1
        if tmp0==1:
            tmp.append(1)
            current_bit+=1
        if current_bit>max_bit:
            max_bit = current_bit
        for j in range(len(tmp)):
            total[i].binary[7-j] = tmp[j]
            total[i].ones+=tmp[j]

elif choose=='2':
    inp = []
    inp1 = input("请输入组合:").split("+")
    inp1 = list(set(inp1))
    for i in inp1:
        t = list(i)
        for j in range(len(t)):
            if t[j]=='X':
                t[j]=2
            else:
                t[j]=int(t[j])
        inp.append(t)
    for i in inp:
        expand_list(inp,i)
    inp = de_identical1(inp)
    dec_num = len(inp)
    max_bit = len(inp[0])
    for i in range(dec_num):
        exec("list0_%s=List()"%i)
        exec("total.append(list0_%s)"%i)
        total[i].binary[-max_bit:] = inp[i][:]
        for j in inp[i]:
            total[i].ones+=j
    for i in range(dec_num):
        exec("decimals%s=Decimal()"%i)
        exec("decimals.append(decimals%s)"%i)
        for j in inp[i]:
            decimals[i].value = decimals[i].value * 2
            decimals[i].value += j
        decimals_value.append(decimals[i].value)
        total[i].component.append(decimals[i].value)

elif choose=='3':
    inp = []
    max_bit = 0
    tmp1 = []
    out_dict1 = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H"}
    out_dict2 = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8}
    inp1 = input("请输入组合:").split("+")
    inp1 = list(set(inp1))
    for i in inp1:
        t = list(i)
        current_bit = 8
        tmp = []
        for j in range(8):
            if out_dict1[8-j] in t:
                tmp.append(1)
            else:
                tmp.append(2)
        while "'" in t:
            tmp[8-out_dict2[t[t.index("'")-1]]] = 0
            t.pop(t.index("'"))
        for j in range(8):
            if tmp[j]==2:
                current_bit-=1
            else:
                break
        if current_bit>max_bit:
            max_bit = current_bit
        tmp1.append(tmp)
    for i in tmp1:
        tmp = []
        for j in range(max_bit):
            tmp.append(i[-j-1])
        inp.append(tmp)
    for i in inp:
        expand_list(inp,i)
    inp = de_identical1(inp)
    dec_num = len(inp)
    for i in range(dec_num):
        exec("list0_%s=List()"%i)
        exec("total.append(list0_%s)"%i)
        total[i].binary[-max_bit:] = inp[i][:]
        for j in inp[i]:
            total[i].ones+=j
    for i in range(dec_num):
        exec("decimals%s=Decimal()"%i)
        exec("decimals.append(decimals%s)"%i)
        for j in inp[i]:
            decimals[i].value = decimals[i].value * 2
            decimals[i].value += j
        decimals_value.append(decimals[i].value)
        total[i].component.append(decimals[i].value)

gen = 1
di = 0
for i in range(dec_num):
    for j in range(dec_num):
        if total[j].ones==total[i].ones+1:
            result = compare_binary(total[i].binary,total[j].binary)
            if result:
                exec("list%s_%s=List()"%(gen,di))
                exec("total_next.append(list%s_%s)"%(gen,di))
                comp = []
                comp.append(decimals[i].value)
                comp.append(decimals[j].value)
                comp = list(set(comp))
                total_next[di].component=comp[:]
                total_next[di].binary = result
                for k in result:
                    if k==1:
                        total_next[di].ones+=1
                total[i].flag = 1
                total[j].flag = 1
                di+=1
cont_or_not = check_flag(total)
output = de_identical(output_binary, output)
for i in output:
    output_component.append(i.component)

while cont_or_not==1:
    gen+=1
    di = 0
    total = total_next[:]
    total_next = []
    dec_num = len(total)
    for i in range(dec_num):
        for j in range(dec_num):
            if total[j].ones==total[i].ones+1:
                result = compare_binary(total[i].binary,total[j].binary)
                if result:
                    exec("list%s_%s=List()"%(gen,di))
                    exec("total_next.append(list%s_%s)"%(gen,di))
                    comp = []
                    comp=total[i].component+total[j].component
                    comp = list(set(comp))
                    total_next[di].component=comp[:]
                    total_next[di].binary = result
                    for k in result:
                        if k==1:
                            total_next[di].ones+=1
                    total[i].flag = 1
                    total[j].flag = 1
                    di+=1
    cont_or_not = check_flag(total)
    output = de_identical(output_binary, output)
    for i in output:
        output_component.append(i.component)
    output_component = de_identical0(output_component)

for i in output:
    for j in i.component:
        for k in decimals:
            if j==k.value:
                k.comp_time+=1
                k.corresponding.append(i.component)

output2 = []
output_tmp = []
for k in decimals:
    if k.comp_time<2:
        output_tmp.append(k.corresponding[0])
        if k.corresponding[0] in output_component:
            output2.append(output_binary[output_component.index(k.corresponding[0])])
            output_component[output_component.index(k.corresponding[0])] = []

for i in output_tmp:
    for j in i:
        for k in output_component:
            if j in k:
                k.remove(j)
        if j in decimals_value:
            decimals.pop(decimals_value.index(j))
            decimals_value.remove(j)

empty = 0
to_process = []
final_process = []
final_result = []
for i in output_component:
    if not i:
        empty+=1
    else:
        to_process.append(i)

decimal_final = []
final_length = []
if empty==len(output_component):
    final_print = print_result(output2,max_bit)
else:
    for i in to_process:
        for j in decimals:
            if j.value in i:
                j.final.append(i)
    for i in decimals:
        decimal_final.append(i.final)
    for i in product(*decimal_final):
        final_process.append(de_identical1(list(i)))
    final_process = de_identical0(final_process)
    for i in final_process:
        final_length.append(len(i))
    for i in get_index(final_length, min(final_length)):
        final_result.append(final_process[i])
    if len(final_result)>1:
        for i in range(len(final_result[1:])):
            exec("output2_%s=output2[:]"%i)
            for j in final_result[1+i]:
                exec("output2_%s.append(output_binary[output_component.index(j)])"%i)
        for i in final_result[0]:
            output2.append(output[output_component.index(i)])
        final_print = print_result(output2,max_bit)
        for i in range(len(final_result[1:])):
            final_print = f'{final_print} or '
            exec("final_print = f'{final_print}{print_result(output2_%s,max_bit)}"%i)
    else:
        for i in final_result[0]:
            output2.append(output_binary[output_component.index(i)])
        final_print = print_result(output2,max_bit)
print(final_print)