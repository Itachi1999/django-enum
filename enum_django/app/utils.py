from enum import Enum, verify, UNIQUE

# @verify(UNIQUE)
# class Divisions(Enum):
#     HR = "Human Resources"
#     IT = "Information Technology"
#     RD = "Research and Development"
#     ACCOUNTS = "Accounts"
    
@verify(UNIQUE)
class Year(Enum):
    FRESHMAN = 1
    SOPHOMORE = 2
    JUNIOR = 3
    SENIOR = 4

@verify(UNIQUE)
class Mathematics(Enum):
    TOPOLOGY = "Algebraic Topology"
    ALGEBRA = "Abstract Algebra"
    CALC = "Multivariable Calculus"
    LIN_ALG = "Linear Algebra"

@verify(UNIQUE)
class ComputerScience(Enum):
    ALGO = "Data Structures and Algorithms"
    DL = "Deep Learning"
    NLP = "Natural Language Processing"
    
class Subjects(Enum):
    CS = ComputerScience
    MTH = Mathematics