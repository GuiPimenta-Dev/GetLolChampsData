import glob
import xlsxwriter

def generate_account_informations():
    workbook = xlsxwriter.Workbook(f'accounts.xlsx')
    header_cells = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
    header = ['Email', 'Acesso Email', 'Senha Email', 'Senha Facebook', 'Code #1', 'Code #2', 'Code #3', 'Code #4',
              'Code #5', 'Code #6', 'Code #7', 'Code #8', 'Code #9', 'Code #10']
    worksheet = workbook.add_worksheet()

    for i in range(14):
        worksheet.write(f'{header_cells[i]}1', f'{header[i]}')

    arquivos = glob.glob(f"utils/accounts/*")
    for index, arquivo in enumerate(arquivos, start=2):
        values = []
        with open(arquivo) as f_in:
            lines = [line for line in (l.strip() for l in f_in) if line]
            values.append(arquivo.split('\\')[1].replace('.txt', '').strip())
            values.append(lines[1])
            values.append(lines[3])
            values.append(lines[5])
            for i in range(1, 20, 2):
                values.append(lines[-i])


        for i in range(14):
            worksheet.write(f'{header_cells[i]}{index}', f'{values[i]}')

    workbook.close()
