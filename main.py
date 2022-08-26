import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
from operator import itemgetter
# from pprint import pprint

def open_file(file_sours): 
  with open(file_sours) as f:
    rows = csv.reader(f, delimiter=",")
    c_l = list(rows)
  return c_l
# pprint(c_l)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

def cut_list(c_l):
  '''поскольку в задании должно быть 7 элементов в каждой записи, а в исходном файле одна запись имеет 8 элементов, то откидываем лишние элементы записи, предполагая, что они пустые/не нужные'''
  for i in range(len(c_l)):
    if len(c_l[i]) > 7:      
      for k in range(7,len(c_l[i])):
        del c_l[i][k]
  return c_l
  
def re_list(c_l):  
  for i in range(len(c_l)):
    line = ','.join(c_l[i]) 
    pattern = [[r"^(\w+)\s(\w+)\s(\w+),,", r"\1,\2,\3"], [r"^(\w+),(\w+)\s(\w+),", r"\1,\2,\3"], ["^(\w+)\s(\w+),,", r"\1,\2,"], [r",\+7\s\((\d*)\)\s(\d*)\-(\d*)\-(\d*)", r",+7(\1)\2-\3-\4"], [r",\+7(\d{3})(\d{3})(\d{2})(\d{2})", r",+7(\1)\2-\3-\4"], [r",8\s(\d*)\-(\d*)\-(\d{2})(\d{2})", r",+7(\1)\2-\3-\4"], [r",8\((\d*)\)(\d*)\-(\d*)\-(\d*)", r",+7(\1)\2-\3-\4"], [r"\s\(доб.\s(\d+)\)", r" доб.\1"], [r"\sдоб.\s(\d+)", r" доб.\1"]]  
    for k in range(len(pattern)):
      line = re.sub(pattern[k][0], pattern[k][1], line)   
    c_l[i] = line.split(',')
  return c_l
  
def not_duble(c_l):    
  c_l = sorted(c_l, key=itemgetter(0, 1))  
  cl = c_l
  for i in range(len(cl)-1, 0, -1):    
    if cl[i][0] == cl[i-1][0] and cl[i][1] == cl[i-1][1]:    
      for k in range(len(c_l[i])):
        if c_l[i][k] == '' or c_l[i-1][k] == '':
          c_l[i-1][k] += c_l[i][k]
      del c_l[i]
  return c_l
   
# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
def whrite_file(c_l, file_exit):
  with open(file_exit, "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(c_l)

if __name__ == '__main__':
  file_sours = 'phonebook_raw.csv'
  file_exit = 'phonebook_new.csv'
  whrite_file(not_duble(re_list(cut_list(open_file(file_sours)))), file_exit)




