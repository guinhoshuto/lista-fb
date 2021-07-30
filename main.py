#importar bibliotecas
import pandas as pd

#importar arquivo xlsx e lista de cursos com categorias
df = pd.read_excel('', dtype={"Celular1":str, "Celular2":str})
cursos = pd.read_csv('')
print(df.describe())
print(df.head())

#fazer formatação de telefone numa lista

#formatar telefones
celular1 = df["Celular1"].str.replace(" ", "").str.replace("(", "+55 ").str.replace(")", " ") 
celular2 = df["Celular2"].str.replace(" ", "").str.replace("(", "+55 ").str.replace(")", " ") 

#se começa com 679 trocar pra +55 67 
celular1.loc[(celular1.str[0:3] == '679')] = "+55 67 " + celular1.str[3:]
celular2.loc[(celular2.str[0:3] == '679')] = "+55 67 " + celular2.str[3:]

#se começa com 9 trocar pra +55 67
celular1.loc[(celular1.str[0] == '9')] = "+55 67 " + celular1 
celular2.loc[(celular2.str[0] == '9')] = "+55 67 " + celular2

#se não tiver hífem inserir
celular1.loc[(celular1.str[-5] != "-")] = celular1.str[:-4] + "-" + celular1.str[-4:]
celular2.loc[(celular2.str[-5] != "-")] = celular2.str[:-4] + "-" + celular2.str[-4:]

#reorganizar tabela conforme template do fb
email = df["Email"]
fn = df["Nome"].str.split(" ").str.get(0)
ln = df["Nome"].str.split(" ").str.get(-1)

curso = df["Curso"]

fb_lista = pd.DataFrame({'email': email,'celular1': celular1, 'celular2': celular2, 'fn': fn, 'ln':ln, 'curso': curso}, dtype=object)
print("----------")
fb_lista = pd.merge(fb_lista, cursos,on='curso', how='inner')
print(fb_lista)

#fazer fórmula p transformar cat em csv

#filtrar registros em técnico de enfermagem
fb_lista['curso'] = fb_lista['curso'].fillna("-")
saude = fb_lista[fb_lista['tipo'].str.contains("Saúde")]
print(saude)

tecnologia = fb_lista[fb_lista['tipo'].str.contains("Tecnologia")]
print(tecnologia)

adm = fb_lista[fb_lista['tipo'].str.contains("Administrativo")]
print(adm)

beleza = fb_lista[fb_lista['tipo'].str.contains("Beleza")]
print(beleza)

gastronomia = fb_lista[fb_lista['tipo'].str.contains("Gastronomia")]
print(gastronomia)

#gerar csv
saude.to_csv('saude.csv', encoding='utf-8')
tecnologia.to_csv('tech.csv', encoding='utf-8')
adm.to_csv('adm.csv', encoding='utf-8')
beleza.to_csv('beleza.csv', encoding='utf-8')
gastronomia.to_csv('gastronomia.csv', encoding='utf-8')
