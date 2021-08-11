import glob
import xlsxwriter
workbook = xlsxwriter.Workbook('../accounts.xlsx')
header_cells = [ 'A', 'B', 'C', 'D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N']
header = ['Email','Acesso Email', 'Senha Email', 'Senha Facebook','Code #1','Code #2','Code #3','Code #4','Code #5','Code #6','Code #7','Code #8','Code #9','Code #10']
worksheet = workbook.add_worksheet()

for i in range(14):
    worksheet.write(f'{header_cells[i]}1',f'{header[i]}')

arquivos = glob.glob(f"accounts/*")
for index, arquivo in enumerate(arquivos, start=2):
    values = []
    with open(arquivo) as f_in:
        lines = [line for line in (l.strip() for l in f_in) if line]
        lines.pop(6)
        lines.pop(6)
        values.append(arquivo.split('\\')[1].replace('.txt','').strip())
        for key,value in enumerate(lines):
            if key % 2 == 1:
                values.append(value)

    for i in range(14):
        worksheet.write(f'{header_cells[i]}{index}', f'{values[i]}')

workbook.close()