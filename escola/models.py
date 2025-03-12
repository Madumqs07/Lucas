from django.db import models

class Responsavel(models.Model):
    nome_responsavel = models.CharField(max_length=50, verbose_name="Digite o nome do responsável")
    sobrenome_responsavel= models.CharField(max_length=50, verbose_name="Digite o sobrenome do responsável")
    numero_telefone_responsavel = models.CharField(max_length=15, verbose_name="Digite o número do celular (xx) xxxxx-xxxx")
    email_responsavel = models.EmailField(max_length=100, verbose_name="Digite o e-mail do responsável")
    adress = models.CharField(max_length=100) 
    CPF_responsavel = models.CharField(max_length=11, unique=True, verbose_name="Informe o CPF do responsável")
    data_nascimento_responsavel = models.DateField()
    
    def __str__(self):
        return self.nome_responsavel
    
    
class Aluno(models.Model):
    TURMA_CHOICE = (
        ("1DS", "1° Ano D.S"),
        ("1CN", "1° Ano C.N"),
        ("1JG", "1° Ano J.G"),
        ("2DS", "1° Ano D.S"),
        ("2CN", "1° Ano C.N"),
        ("2JG", "1° Ano J.G"),
        ("3DS", "1° Ano D.S"),
        ("3CN", "1° Ano C.N"),
        ("3JG", "1° Ano J.G"),
    )
    nome_aluno = models.CharField(max_length=50, verbose_name="Digite o nome do aluno")
    sobrenome_aluno= models.CharField(max_length=50, verbose_name="Digite o sobrenome do aluno")
    numero_telefone_aluno = models.CharField(max_length=15, verbose_name="Digite o número do celular (xx) xxxxx-xxxx")
    email_aluno = models.EmailField(max_length=100, verbose_name="Digite o seu e-mail")
    adress = models.CharField(max_length=100) 
    CPF_aluno = models.CharField(max_length=11, unique=True, verbose_name="Informe o seu CPF")
    data_nascimento_aluno = models.DateField()
    numero_matricula_aluno = models.CharField(max_length=6, verbose_name="Digite o número da sua matricula")
    class_choices = models.CharField(max_length=3, choices=TURMA_CHOICE, blank=True, null=False)
    
    def __str__(self):
        return self.nome_aluno
    

class Professor(models.Model):
    TURMA_CHOICE = (
        ("1DS", "1° Ano D.S"),
        ("1CN", "1° Ano C.N"),
        ("1JG", "1° Ano J.G"),
        ("2DS", "1° Ano D.S"),
        ("2CN", "1° Ano C.N"),
        ("2JG", "1° Ano J.G"),
        ("3DS", "1° Ano D.S"),
        ("3CN", "1° Ano C.N"),
        ("3JG", "1° Ano J.G"),
    )
     
    nome_professor = models.CharField(max_length=50, verbose_name="Digite seu nome")
    sobrenome_professor= models.CharField(max_length=50, verbose_name="Digite o seu sobrenome")
    numero_telefone_professor = models.CharField(max_length=15, verbose_name="Digite o número do celular (xx) xxxxx-xxxx")
    email_professor = models.EmailField(max_length=100, verbose_name="Digite o seu e-mail")
    adress = models.CharField(max_length=100) 
    CPF_professor = models.CharField(max_length=11, unique=True, verbose_name="Informe o seu CPF")
    data_nascimento_professor = models.DateField()
    numero_matricula_professor = models.CharField(max_length=6, verbose_name="Digite o número da matricula")
    class_choices = models.CharField(max_length=3, choices=TURMA_CHOICE, blank=True, null=False)
    
    def __str__(self):
        return self.nome_professor
    
    
    

    
    
    
    

    
    
    
    

