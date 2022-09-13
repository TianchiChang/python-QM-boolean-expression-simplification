# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 18:02:25 2022

@author: AiBuZ
"""
from itertools import product
from PyQt5.QtWidgets import QPushButton,QTextEdit,QMainWindow,QDialog,QApplication
import sqlite3
import sys

text1 = '''您可以选择三种方式输入：
方式1：Y=chr(931)(eg:6,7,0,4,2)
方式2：Y=（eg:11X+111+XX0)
方式3：Y=(eg:AB+ABC+C')\n'''

class List():
    def __init__(self):
        self.component = []
        self.ones = 0
        self.flag = 0
        self.binary = [0,0,0,0,0,0,0]

class Decimal():
    def __init__(self):
        self.value = 0
        self.comp_time = 0
        self.corresponding = []
        self.final = []

class Ui_main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,400,500,360)
        self.setWindowTitle("布尔式化简器")
        self.t1=QTextEdit(self)
        self.t1.setGeometry(15,15,300,330)
        self.t1.append(text1)
        self.Choose_1 = QPushButton("输入模式1", self)
        self.Choose_1.setGeometry(350,15,100,30)
        self.Choose_2 = QPushButton('输入模式2',self)
        self.Choose_2.setGeometry(350,65,100,30)
        self.Choose_3 = QPushButton('输入模式3',self)
        self.Choose_3.setGeometry(350,115,100,30)
        self.history = QPushButton('历史记录',self)
        self.history.setGeometry(350,165,100,30)
        self.B_close=QPushButton('关闭',self)
        self.B_close.setGeometry(350,315,100,30)
        self.Choose_1.clicked.connect(self.create_choose_1)
        self.Choose_2.clicked.connect(self.create_choose_2)
        self.Choose_3.clicked.connect(self.create_choose_3)
        self.history.clicked.connect(self.create_history)
        self.B_close.clicked.connect(self.close)
    
    def create_choose_1(self):
        child_window = Ui_choose_1()
        child_window.exec()
    
    def create_choose_2(self):
        child_window = Ui_choose_2()
        child_window.exec()
    
    def create_choose_3(self):
        child_window = Ui_choose_3()
        child_window.exec()
    
    def create_history(self):
        child_window = Ui_history()
        child_window.exec()
    
class Ui_choose_1(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,400,500,260)
        self.setWindowTitle("输入模式1")
        self.t1=QTextEdit(self)
        self.t1.setGeometry(15,15,300,30)
        self.t1.setPlaceholderText("请输入数字：")
        self.t2=QTextEdit(self)
        self.t2.setGeometry(15,65,300,180)
        self.calculate=QPushButton('运算',self)
        self.calculate.setGeometry(350,15,100,30)
        self.closed=QPushButton('关闭',self)
        self.closed.setGeometry(350,65,100,30)
        self.calculate.clicked.connect(self.process)
        self.closed.clicked.connect(self.close)
    
    def process(self):
        if self.t1:
            self.t2.clear()
            main_calculate_result = main_calculate(self.t1.toPlainText(),'1')
            self.t2.append(main_calculate_result)
            update_result(main_calculate_result,self.t1.toPlainText())

class Ui_choose_2(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,400,500,260)
        self.setWindowTitle("输入模式2")
        self.t1=QTextEdit(self)
        self.t1.setGeometry(15,15,300,30)
        self.t1.setPlaceholderText("请输入组合：")
        self.t2=QTextEdit(self)
        self.t2.setGeometry(15,65,300,180)
        self.calculate=QPushButton('运算',self)
        self.calculate.setGeometry(350,15,100,30)
        self.closed=QPushButton('关闭',self)
        self.closed.setGeometry(350,65,100,30)
        self.calculate.clicked.connect(self.process)
        self.closed.clicked.connect(self.close)
    
    def process(self):
        if self.t1:
            self.t2.clear()
            main_calculate_result = main_calculate(self.t1.toPlainText(),'2')
            self.t2.append(main_calculate_result)
            update_result(main_calculate_result,self.t1.toPlainText())

class Ui_choose_3(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,400,500,260)
        self.setWindowTitle("输入模式3")
        self.t1=QTextEdit(self)
        self.t1.setGeometry(15,15,300,30)
        self.t1.setPlaceholderText("请输入组合：")
        self.t2=QTextEdit(self)
        self.t2.setGeometry(15,65,300,180)
        self.calculate=QPushButton('运算',self)
        self.calculate.setGeometry(350,15,100,30)
        self.closed=QPushButton('关闭',self)
        self.closed.setGeometry(350,65,100,30)
        self.calculate.clicked.connect(self.process)
        self.closed.clicked.connect(self.close)
    
    def process(self):
        if self.t1:
            self.t2.clear()
            main_calculate_result = main_calculate(self.t1.toPlainText(),'3')
            self.t2.append(main_calculate_result)
            update_result(main_calculate_result,self.t1.toPlainText())

class Ui_history(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,400,500,260)
        self.setWindowTitle("历史记录")
        self.t1=QTextEdit(self)
        self.t1.setGeometry(15,15,300,225)
        self.search=QPushButton('查询记录',self)
        self.search.setGeometry(350,15,100,30)
        self.delete=QPushButton('删除记录',self)
        self.delete.setGeometry(350,65,100,30)
        self.closed=QPushButton('关闭',self)
        self.closed.setGeometry(350,115,100,30)
        self.search.clicked.connect(self.search_history)
        self.delete.clicked.connect(self.delete_history)
        self.closed.clicked.connect(self.close)
    
    def search_history(self):
        self.t1.clear()
        to_print1 = 'Input:'
        to_print2 = 'Output:'
        cursor = c.execute("SELECT result,input from QMH")
        for row in cursor:
            self.t1.append(f'{to_print1}{row[1]}')
            self.t1.append(f'{to_print2}{row[0]}')
            self.t1.append('\n')
    
    def delete_history(self):
        self.t1.clear()
        c.execute("DELETE from QMH")
        conn.commit()
        c.execute("INSERT INTO QMH (ID,RESULT,INPUT) \
              VALUES (0, 'NO HISTORY' ,'NO INPUT')")
        conn.commit()

def update_result(main_calculate_result,input1):
    cursor = c.execute("select id,result from QMH order by id desc limit 0,1;")
    for row in cursor:
        if row[1]!='NO HISTORY':
            new_id = row[0]+1
        else:
            c.execute("UPDATE QMH set RESULT = '{value1}', INPUT = '{value2}' where ID=0".format(value1=main_calculate_result,value2=input1))
            conn.commit()
            return
    if new_id>9:
        add_to_end(main_calculate_result,input1,9)
    else:
        c.execute('''INSERT INTO QMH (ID,RESULT,INPUT) \
              VALUES ({value1}, "{value2}", "{value3}")'''.format(value1=new_id,value2=main_calculate_result,value3=input1))
    conn.commit()

def add_to_end(main_calculate_result,input1,length):
    mcr_tmp = []
    input1_tmp = []
    #c.execute("DELETE from QMH where ID=0")
    cursor = c.execute("SELECT result,input from QMH")
    for row in cursor:
        mcr_tmp.append(row[0])
        input1_tmp.append(row[1])
    for i in range(length):
        c.execute('''UPDATE QMH set RESULT="{value1}" where ID={value2}'''.format(value1=mcr_tmp[i+1],value2=i))
        c.execute('''UPDATE QMH set INPUT="{value1}" where ID={value2}'''.format(value1=input1_tmp[i+1],value2=i))
        c.execute('''UPDATE QMH set RESULT="{value1}" where ID={value2}'''.format(value1=main_calculate_result,value2=length))
        c.execute('''UPDATE QMH set INPUT="{value1}" where ID={value2}'''.format(value1=input1,value2=length))

def expand_list(list1,comp1):
    if 2 in comp1:
        comp2 = comp1[:]
        comp1[comp1.index(2)] = 0
        comp2[comp2.index(2)] = 1
        list1.append(comp2)
    if 2 in comp1:
        expand_list(list1, comp1)
        expand_list(list1, comp2)

def compare_binary(comp1,comp2):
    unmatch = 0
    tmp = comp1[:]
    for i in range(7):
        if comp1[i]!=comp2[i]:
            tmp[i] = 2
            unmatch+=1
    if unmatch>1:
        return 0
    else:
        return tmp

def check_flag(flag,output,output_binary):
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
    out_dict1 = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G"}
    out_dict2 = {1:"A\'",2:"B\'",3:"C\'",4:"D\'",5:"E\'",6:"F\'",7:"G\'"}
    to_print = 'Y = '
    for i in range(len(result)):
        for j in range(max_bit):
            if result[i][7-max_bit+j]==1:
                to_print = f'{to_print}{out_dict1[j+1]}'
            elif result[i][7-max_bit+j]==0:
                to_print = f'{to_print}{out_dict2[j+1]}'
        if i<len(result)-1:
            to_print = f'{to_print} + '
    return to_print

def main_calculate(inp1,choose):
    total = []
    total_next = []
    output = []
    output_binary = []
    output_component = []
    decimals = []
    decimals_value = []
    
    if choose=='1':
        inp1 = inp1.split(',')
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
                total[i].binary[6-j] = tmp[j]
                total[i].ones+=tmp[j]
    
    elif choose=='2':
        inp = []
        inp1 = inp1.split('+')
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
        out_dict1 = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G"}
        out_dict2 = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7}
        inp1 = inp1.split('+')
        inp1 = list(set(inp1))
        for i in inp1:
            t = list(i)
            current_bit = 7
            tmp = []
            for j in range(7):
                if out_dict1[7-j] in t:
                    tmp.append(1)
                else:
                    tmp.append(2)
            while "'" in t:
                tmp[7-out_dict2[t[t.index("'")-1]]] = 0
                t.pop(t.index("'"))
            for j in range(7):
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
    cont_or_not = check_flag(total,output,output_binary)
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
        cont_or_not = check_flag(total,output,output_binary)
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
    return final_print

if __name__ == "__main__":
    conn = sqlite3.connect('qm_history.db')
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE QMH
                (ID INT PRIMARY KEY NOT NULL,
                RESULT TEXT NOT NULL,
                INPUT TEXT NOT NULL);''')
        conn.commit()
        c.execute("INSERT INTO QMH (ID,RESULT,INPUT) \
              VALUES (0, 'NO HISTORY' ,'NO INPUT')")
        conn.commit()
        print("创建成功")
    except:
        print("连接成功")
    app = QApplication(sys.argv)
    window = Ui_main()
    window.show()
    sys.exit(app.exec_())
    conn.close()