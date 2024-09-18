import math

#Questao 1

#É provado que o número de maneiras distintas de se subir a escada e igual
#elemento n da sequencia de fibonacci, logo o codigo é apenas a sequencia

def escadas(x):
    a, b = 1, 1
    for i in range(x):
        a, b = b, a + b
    return a    

#-----------------------------

#Questao 2

#-----------------------------

class Field:
    pass

class VectorSpace:
    
    def __init__(self, dim: int, field: 'Field'):
        self.dim = dim
        self._field = field
        
    def getField(self):
        return self._field
    
    def getVectorSpace(self):
        return f'dim = {self.dim!r}, field = {self._field!r}'

    def __repr__(self):
        return self.getVectorSpace()
    
    def __mul__(self, f):
        raise NotImplementedError
    
    def __rmul__(self, f):
        return self.__mul__(f)
    
    def __add__(self, v):
        raise NotImplementedError
    
#-----------------------------

class RealVector(VectorSpace):
    _field = float
    def __init__(self, dim, coord):
        super().__init__(dim, self._field)
        self.coord = coord
    

    @staticmethod
    def _builder(coord):
        raise NotImplementedError

    def __add__(self, other_vector):
        n_vector = []
        for c1, c2 in zip(self.coord, other_vector.coord):
            n_vector.append(c1+c2)
        return self._builder(n_vector)
    
    def __sub__(self, other_vector):
        n_vector = []
        for c1, c2 in zip(self.coord, other_vector.coord):
            n_vector.append(c1-c2)
        return self._builder(n_vector)

    def __mul__(self, alpha):
        n_vector = []
        for c in self.coord:
            n_vector.append(alpha*c)
        return self._builder(n_vector)
    
    def iner_prod(self, other_vector):
        res = 0
        for c1, c2 in zip(self.coord, other_vector.coord):
            res += c1*c2
        return res

    def __str__(self):
        ls = ['[']
        for c in self.coord[:-1]:
            ls += [f'{c:2.2f}, ']
        ls += f'{self.coord[-1]:2.2f}]'
        s =  ''.join(ls)
        return s
    
    #Norma do vetor

    def __abs__(self):
        k = self.iner_prod(self)
        return math.sqrt(k)

#-----------------------------

#Questão 2

#-----------------------------

class Vector2D(RealVector):
    _dim = 2
    def __init__(self, coord):
        if len(coord) != 2:
            raise ValueError
        super().__init__(self._dim, coord)

    def __add__(self, other_vector):
        return super().__add__(other_vector)
    
    def __sub__(self, other_vector):
        return super().__sub__(other_vector)
    
    def negative(self):
        n_vec = []
        for i in self.coord:
            n_vec.append(-i)
        return n_vec

    def __mul__(self, alpha):
        return super().__mul__(alpha)
    

    @staticmethod
    def _builder(coord):
        return Vector2D(coord)
    
    def CW(self):
        return Vector2D([-self.coord[1], self.coord[0]])
    

    def CCW(self):
        return Vector2D([self.coord[1], -self.coord[0]])
    
#-----------------------------
    
#Questão 3

#-----------------------------
    
class Vector3D(RealVector):
    _dim = 3
    def __init__(self, coord):
        if len(coord) != 3:
            raise ValueError
        super().__init__(self._dim, coord)

    def __add__(self, other_vector):
        return super().__add__(other_vector)
    
    def __sub__(self, other_vector):
        return super().__sub__(other_vector)
    
    def negative(self):
        n_vec = []
        for i in self.coord:
            n_vec.append(-i)
        return n_vec

    def __mul__(self, alpha):
        return super().__mul__(alpha)
    

    @staticmethod
    def _builder(coord):
        return Vector3D(coord)
    
    def CW(self):
        return Vector2D([-self.coord[1], self.coord[0]])
    

    def CCW(self):
        return Vector2D([self.coord[1], -self.coord[0]])    
    
'''
O polinomio vai ser escrito com as potencias crescendo da esquerda para a direita,
por exemplo, o polinomio 1 - 6x^1 + 3x^2 é escrito como [1, -6, 3]
'''   
    
class Polinomio(RealVector):

    def __init__(self, coord):
        super().__init__(len(coord), coord)

    def __add__(self, other_vector):
        return super().__add__(other_vector)

    def __sub__(self, other_vector):
        return super().__sub__(other_vector)
    
    def __mul__(self, alpha):
        return super().__mul__(alpha)

    def __str__(self):
        poli = ''
        for i in range(len(self.coord)):
            if self.coord[i] == 0:
                continue
            if i == 0:
                poli += f'{self.coord[i]} '
                continue
            if self.coord[i] > 0:
                poli += f'+ {self.coord[i]}x^{i} '  
            else:
                poli += f'- {abs(self.coord[i])}x^{i} '  
        if poli[0] == '+' or poli[0:1] == '- ':
            poli = poli[2:]
        return poli[:-1]
    
    @staticmethod
    def _builder(coord):
        return Polinomio(coord)
    
#-----------------------------
    
#Questão 5

#-----------------------------

import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards) 
    
    def __getitem__(self, position):
        return self._cards[position]
    
myDeck = FrenchDeck()

random.shuffle(myDeck._cards)   

#-----------------------------


if __name__ == '__main__':
    print('Vetores 3D')
    vetor3d1 = Vector3D([2, 4, 8])
    print('V1: ' , vetor3d1)
    vetor3d2 = Vector3D([7, 3, 5])
    print('V2: ' , vetor3d2)
    print('V1 + V2: ', vetor3d2 + vetor3d1)
    print('V1 - V2: ', vetor3d1 - vetor3d2)
    print('-V1: ', vetor3d1.negative())
    print('\nPolinomios')
    poli1 = Polinomio([2, 5, 1])
    print('P1: ', poli1)
    poli2 = Polinomio([4, 2, 7])
    print('P2: ', poli2)
    print('P1 + P2: ', poli1 + poli2)
    print('P1 - P2: ', poli1 - poli2)
