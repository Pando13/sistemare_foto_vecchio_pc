# D:\FOTO
# link utili
# https://www.codespeedy.com/delete-all-the-png-images-from-a-folder-in-python/
# http://www.learningaboutelectronics.com/Articles/How-to-get-the-last-modified-date-of-a-file-in-Python.php
# https://www.geeksforgeeks.org/python-move-files-to-creation-and-modification-date-named-directories/
# https://www.geeksforgeeks.org/python-os-chdir-method/
# https://www.geeksforgeeks.org/python-os-getcwd-method/#:~:text=os.getcwd%20%28%29%20method%20tells%20us%20the%20location%20of,a%20string%20which%20represents%20the%20current%20working%20directory.



import os
from datetime import datetime

cartella = r'****\\'
print('cartella = (r\'D:\FOTO\')    -ok\n')

lista = os.listdir(cartella)
print('lista = os.listdir(cartella)    -ok\n')

c2011 = 'D:\sfoto_sistemate\sanno_2011\\'
c2012 = 'D:\sfoto_sistemate\sanno_2012\\'
c2013 = 'D:\sfoto_sistemate\sanno_2013\\'
c2014 = 'D:\sfoto_sistemate\sanno_2014\\'
c2015 = 'D:\sfoto_sistemate\sanno_2015\\'
c2016 = 'D:\sfoto_sistemate\sanno_2016\\'
c2017 = 'D:\sfoto_sistemate\sanno_2017\\'
c2018 = 'D:\sfoto_sistemate\sanno_2018\\'
c2019 = 'D:\sfoto_sistemate\sanno_2019\\'
c2020 = 'D:\sfoto_sistemate\sanno_2020\\'
c2021 = 'D:\sfoto_sistemate\sanno_2021\\'
c2022 = 'D:\sfoto_sistemate\sanno_2022\\'

def main1():
    for file in lista:
        print(cartella+file)
        if os.path.isdir(cartella+file) or os.path.isfile(cartella+file):
            data = datetime.fromtimestamp(os.path.getctime(cartella+file))
            unix = os.stat(cartella+file).st_mtime
            giorno = data.day
            mese = data.month
            anno = data.year
        else:
            print('non so cosa sia')
            continue


        if os.path.isdir(cartella+file):
            print('CARTELLA', end='  | DATA: ')
            print(giorno, mese, anno)
        elif os.path.isfile(cartella+file):
            print('FILE', end='      | DATA: ')
            print(giorno, mese, anno)
        print('\n')

def main2():
    for file in lista:
        print(cartella+file)
        if os.path.isdir(cartella+file) or os.path.isfile(cartella+file):
            data = datetime.fromtimestamp(os.path.getctime(cartella+file))
            unix = os.stat(cartella+file).st_mtime
            giorno = data.day
            mese = data.month
            anno = data.year
        else:
            print('non so cosa sia')
            continue


        if os.path.isdir(cartella+file):
            print('CARTELLA', end='  | DATA: ')
            print(giorno, mese, anno)
        elif os.path.isfile(cartella+file):
            print('FILE', end='      | DATA: ')
            print(giorno, mese, anno)
            try:
                if anno == 2011:
                    os.rename(cartella+file, c2011+file)
                elif anno == 2012:
                    os.rename(cartella+file, c2012+file)
                elif anno == 2013:
                    os.rename(cartella+file, c2013+file)
                elif anno == 2014:
                    os.rename(cartella+file, c2014+file)
                elif anno == 2015:
                    os.rename(cartella+file, c2015+file)
                elif anno == 2016:
                    os.rename(cartella+file, c2016+file)
                elif anno == 2017:
                    os.rename(cartella+file, c2017+file)
                elif anno == 2018:
                    os.rename(cartella+file, c2018+file)
                elif anno == 2019:
                    os.rename(cartella+file, c2019+file)
                elif anno == 2020:
                    os.rename(cartella+file, c2020+file)
                elif anno == 2021:
                    os.rename(cartella+file, c2021+file)
                elif anno == 2022:
                    os.rename(cartella+file, c2022+file)
                else:
                    print('anno buggat')
                print('forse ok')
            except FileExistsError:
                print('file gia esistente')
        print('\n')

main2()
