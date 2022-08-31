nota1 = int(input("Informe a nota do bimestre 1 : "))
nota2 = int(input("Informe a nota do bimestre 2 : "))
nota3 = int(input("Informe a nota do bimestre 3 : "))
nota4 = int(input("Informe a nota do bimestre 4 : "))

media_Semestre1 = (nota1 + nota2 ) / 2
media_Semestre2 = (nota3 + nota4 ) / 2

media = (media_Semestre1 + media_Semestre2) / 2
print("A Media do Primeiro semestre é: {:.0f}".format(media_Semestre1))
print("A Media do Segundo semestre é: {:.0f}".format(media_Semestre2))

print("Sua Media Anual é: {:.0f} ".format(media))

estado_Aprovacao = media >= 6
if media >= 60:
  print("Aprovado")
else:
  print ("reprovado")