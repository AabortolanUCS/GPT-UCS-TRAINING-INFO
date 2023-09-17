import csv
import os
import pathlib

def my_function(path, pasta, arquivo):
  
  print(arquivo)
  with open(path+"\\"+pasta+"\\"+arquivo, 'r') as file, open('.\\Dados-Migrados\\dados.jsonl','a') as migrateFile:
        csvreader = csv.reader(file)
        for row in csvreader:
            migrateFile.write("{\"prompt\": \"" + row[0] + "\", \"completion\": \"" + row[1] + "\"}\n")


if pathlib.Path(".\\Dados-Migrados\\dados.jsonl").is_file():
    os.remove(".\\Dados-Migrados\\dados.jsonl")

path = ".\\Dados"
dir_list = os.listdir(path)

for pasta in dir_list:
    subdir_list = os.listdir(path+"\\"+pasta)
    for arquivo in subdir_list:
        my_function(path, pasta, arquivo)
        