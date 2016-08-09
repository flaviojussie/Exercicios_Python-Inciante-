print('Informe o numero do aluno e sua altrua respectivamente.')
i = True
numeroAluno = 1
while numeroAluno != 0:
    numeroAluno = int(input('Digite o numero do aluno: '))
    if numeroAluno != 0:
        alturaAluno = float(input('Informe a altura do aluno: '))
    if i == True:
        alto = alturaAluno
        baixo = alturaAluno
        codAlto = numeroAluno
        codBaixo = numeroAluno
        i = False
    if alturaAluno > alto:
        alto = alturaAluno
        codAlto = numeroAluno
    if alturaAluno < baixo:
        baixo =alturaAluno
        codBaixo = numeroAluno
print('O aluno mais alto tem o numero %d e mede %5.2f'%(codAlto,alto))
print('O aluno mais baixo tem o numero %d e mede %5.2f'%(codBaixo,baixo))