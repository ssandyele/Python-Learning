# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas                                                                                                                                                 
#  – A maior nota                                                                                                                                                               
#  – A menor nota                                                                                                                                                             
#  – A média da turma                                                                                                                                                     
#  – A situação (opcional)

def notas(*notas, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param notas: uma ou mais notas dos alunos (aceitas várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    info = dict()
    info['total']=len(notas)
    info['maior']=max(notas)
    info['menor']=min(notas)
    info['média']=sum(notas)/len(notas)
    if sit==True:
        if info['média']>=7:
            info['situação']='BOA'
        elif info['média']>=5:
            info['situação']='RAZOÁVEL'
        else:
            info['situação']='RUIM'
    return info


resp=notas(5.5, 9.5, 1.0, 6.5, sit=True)
print(resp)
help(notas)