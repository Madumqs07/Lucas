from django.db import models
from validate_docbr import CPF
from django.core.exceptions import ValidationError


def cpf_validate(value):
    cpf = CPF()
    if not cpf.validate(value):
        raise ValidationError(
            ("%(value)s is not an even number"),
            params={"value": value},
        )
    
class Itinerario(models.Model):
    ITINERARIO_CHOICE = (
        ("DS", "Desenvolvimento de Sistemas"),
        ("CN", "Ciências da Natureza"),
        ("JG", "Jogos"),
    )

class Turma(models.Model):
    
    TURMA_CHOICE = (
        ("1", "1° Ano"),
        ("2", "2° Ano"),
        ("3", "3° Ano"),

    )  
    
        


class Responsavel(models.Model):
    nome_responsavel = models.CharField(max_length=50, verbose_name="Digite o nome do responsável")
    sobrenome_responsavel= models.CharField(max_length=50, verbose_name="Digite o sobrenome do responsável")
    numero_telefone_responsavel = models.CharField(max_length=15, verbose_name="Digite o número do celular (xx) xxxxx-xxxx")
    email_responsavel = models.EmailField(max_length=100, verbose_name="Digite o e-mail do responsável")
    adress = models.CharField(max_length=100) 
    CPF_responsavel = models.CharField(max_length=11, validators=[cpf_validate], verbose_name="Informe o CPF do responsável", blank=True, null=False)
    data_nascimento_responsavel = models.DateField()
    
    def __str__(self):
        return self.nome_responsavel
    
class Aluno(models.Model):

    nome_aluno = models.CharField(max_length=50, verbose_name="Digite o nome do aluno")
    sobrenome_aluno= models.CharField(max_length=50, verbose_name="Digite o sobrenome do aluno")
    numero_telefone_aluno = models.CharField(max_length=15, verbose_name="Digite o número do celular (xx) xxxxx-xxxx")
    email_aluno = models.EmailField(max_length=100, verbose_name="Digite o seu e-mail")
    adress = models.CharField(max_length=100) 
    CPF_aluno = models.CharField(max_length=11, validators=[cpf_validate], verbose_name="Informe o CPF do responsável", blank=True, null=False)  
    data_nascimento_aluno = models.DateField()
    numero_matricula_aluno = models.CharField(max_length=6, verbose_name="Digite o número da sua matricula")
    class_choices = models.ForeignKey(Itinerario, on_delete=models.CASCADE, related_name="Itinerario", blank=True, null=False)    
    class_choices = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name="Turma", blank=True, null=False) 
    
    def __str__(self):
        return self.nome_aluno
    

class Professor(models.Model):

    nome_professor = models.CharField(max_length=50, verbose_name="Digite seu nome")
    sobrenome_professor= models.CharField(max_length=50, verbose_name="Digite o seu sobrenome")
    numero_telefone_professor = models.CharField(max_length=15, verbose_name="Digite o número do celular (xx) xxxxx-xxxx")
    email_professor = models.EmailField(max_length=100, verbose_name="Digite o seu e-mail")
    adress = models.CharField(max_length=100) 
    CPF_professor = models.CharField(max_length=11, validators=[cpf_validate], verbose_name="Informe o CPF do responsável", blank=True, null=False)
    data_nascimento_professor = models.DateField()
    numero_matricula_professor = models.CharField(max_length=6, verbose_name="Digite o número da matricula")
    class_choices = models.ForeignKey(Itinerario, on_delete=models.CASCADE, related_name="Itinerario", blank=True, null=False)    
    class_choices = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name="Turma", blank=True, null=False)    

#O ForeignKey é uma chave estrangeira que estabelece um relacionamento entre duas tabelas, permitindo que você vincule registros de uma tabela a registros de outra tabela. 
# O parâmetro on_delete especifica o que acontece quando o registro relacionado é excluído. 
# O related_name é o nome usado para referenciar o relacionamento reverso.

    def __str__(self):
        return self.nome_professor