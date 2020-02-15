import pandas as csv


class Bcolors:
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


class Import:
ICD = 1
OPS = 2


class Titel:
DESCR_NAME = 1
DB_NAME = 2


def get_parentid(konto, category):
if category == Import.ICD:
    for group_row in groups.itertuples():
        if int(group_row.von[1:3]) <= int(konto.code[1:3]) <= int(group_row.bis[1:3]) and konto.code[
                                                                                          :1] == group_row.von[:1]:
            return group_row.id.__str__()
    return "Error ParentID"
elif category == Import.OPS:
    for group_row in groups.itertuples():
        if group_row.von <= int(konto.code[:3]) <= group_row.bis:
            return group_row.id.__str__()
    return "Error ParentID"


def get_descr(changedKontoName):
for title_row in titles.itertuples():
    if changedKontoName == title_row.code:
        return title_row.title.__str__()
return "Error Description"


def get_name(name, category, name_category):
if category == Import.ICD:
    if name_category == Titel.DB_NAME:
        if name.__len__() == 3:
            return name[0:3] + ".-"
        elif name.__len__() == 4 or name.__len__() == 5:
            return name[0:3] + "." + name[3:]
        return "Error name"
    else:
        raise ValueError('Fehlerhafte Namenskategorie')
elif category == Import.OPS:
    if name_category == Titel.DB_NAME:
        if name.__len__() == 4:
            return name[:1] + "." + name[1:]
        elif name.__len__() == 5 or name.__len__() == 6:
            return name[:1] + "." + name[1:4] + "." + name[4:]
        return "Error name"
    elif name_category == Titel.DESCR_NAME:
        if name.__len__() == 4:
            return name[:1] + "-" + name[1:]
        elif name.__len__() == 5 or name.__len__() == 6:
            return name[:1] + "-" + name[1:4] + "." + name[4:]
        return "Error name"
    else:
        raise ValueError('Fehlerhafte Namenskategorie')


def get_sql_name(name):
return "\'" + name + "\'"


def create_sql(id, category, sql_table_string):
error_log = open("error_log.txt", "wt", encoding="utf-8")

if category == Import.ICD:
    output = open("output_icd.txt", "wt", encoding="utf-8")
elif category == Import.OPS:
    output = open("output_ops.txt", "wt", encoding="utf-8")

for konto in konten.itertuples():
    if konto.code.__contains__("Unb") or konto.code.__contains__("Unbeka") or konto.code.__contains__("Unbekannt"):
        continue;

    if category == Import.ICD:
        row = sql_table_string + "(" + id.__str__() + "," + get_parentid(konto, category) + "," + get_sql_name(
            get_name(konto.code, category, Titel.DB_NAME)) + "," + get_sql_name(
            get_descr(konto.code)) + "," + get_sql_name(konto.code) + ")"
    elif category == Import.OPS:
        row = sql_table_string + "(" + id.__str__() + "," + get_parentid(konto, category) + "," + get_sql_name(
            get_name(konto.code, category, Titel.DB_NAME)) + "," + get_sql_name(
            get_descr(get_name(konto.code, category, Titel.DESCR_NAME))) + "," + get_sql_name(
            konto.code) + ")"
    else:
        raise ValueError('Not OPS or ICD selected')

    if not row.__contains__("Error"):
        print(Bcolors.OKBLUE + "Writing row: " + row)
        output.write(row + '\n')
        id += 1
    elif row.__contains__("ParentID"):
        print(Bcolors.WARNING + "Ignoring row: " + row)
        error_log.write("Row failed: " + row + '\n')
    elif row.__contains__("name"):
        print(Bcolors.OKGREEN + "Ignoring row: " + row)
        error_log.write("Row failed: " + row + '\n')
    else:
        print(Bcolors.FAIL + "Ignoring row: " + row)
        error_log.write("Row failed: " + row + '\n')


################################################


# icd

# konten = csv.read_csv('C:\\Users\\mxj\\Documents\\einzelkonten_icd.csv', delimiter=';', names=['code'])
# groups = csv.read_csv('C:\\Users\\mxj\\Documents\\group_icd.csv', delimiter=';', names=['id', 'von', 'bis'])
# titles = csv.read_csv('C:\\Users\\mxj\\Documents\\codes_icd.csv', delimiter=';', names=['code', 'title'])
# create_sql(15859, Import.ICD, "INSERT INTO [icd].[lookupICDCode]([Id],[ParentId],[name],[Description],[Code]) VALUES")

# ops

konten = csv.read_csv('C:\\Users\\mxj\\Documents\\einzelkonten_ops.csv', delimiter=';', names=['code'])
groups = csv.read_csv('C:\\Users\\mxj\\Documents\\group_ops.csv', delimiter=';', names=['id', 'von', 'bis'])
titles = csv.read_csv('C:\\Users\\mxj\\Documents\\Kodes2006.csv', delimiter=';', names=['code', 'title'])
create_sql(35647, Import.OPS, "INSERT INTO [ops].[lookupOPSCode4]([Id],[ParentId],[name],[Description],[Code]) VALUES")


