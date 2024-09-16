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
    """VectorSpace:
    Abstract Class of vector space used to model basic linear structures
    """
    
    def __init__(self, dim: int, field: 'Field'):
        """
        Initialize a VectorSpace instance.

        Args:
            dim (int): Dimension of the vector space.
            field (Field): The field over which the vector space is defined.
        """
        self.dim = dim
        self._field = field
        
    def getField(self):
        """
        Get the field associated with this vector space.

        Returns:
            Field: The field associated with the vector space.
        """
        return self._field
    
    def getVectorSpace(self):
        """
        Get a string representation of the vector space.

        Returns:
            str: A string representing the vector space.
        """
        return f'dim = {self.dim!r}, field = {self._field!r}'
        # return self.__repr__()

    def __repr__(self):
        """
        Get a string representation of the VectorSpace instance.

        Returns:
            str: A string representing the VectorSpace instance.
        """
        # return f'dim = {self.dim!r}, field = {self._field!r}'
        return self.getVectorSpace()
    
    def __mul__(self, f):
        """
        Multiplication operation on the vector space (not implemented).

        Args:
            f: The factor for multiplication.

        Raises:
            NotImplementedError: This method is meant to be overridden by subclasses.
        """
        raise NotImplementedError
    
    def __rmul__(self, f):
        """
        Right multiplication operation on the vector space (not implemented).

        Args:
            f: The factor for multiplication.

        Returns:
            The result of multiplication.

        Note:
            This method is defined in terms of __mul__.
        """
        return self.__mul__(f)
    
    def __add__(self, v):
        """
        Addition operation on the vector space (not implemented).

        Args:
            v: The vector to be added.

        Raises:
            NotImplementedError: This method is meant to be overridden by subclasses.
        """
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
        return Vector2D(coord)
    
    def CW(self):
        return Vector2D([-self.coord[1], self.coord[0]])
    

    def CCW(self):
        return Vector2D([self.coord[1], -self.coord[0]])    
    



if __name__ == '__main__':
    V2 = Vector2D([1, 2])
    print('V2 = ', V2)
    W2 = Vector2D([3, 4])
    print('W2 = ', W2)

    print(V2.getVectorSpace())

    r = V2+4*W2
    print('V2 + 4*W2 =', r)
    print('(V2 + 4*W2).CW() = ', r.CW())
    print('W2.CCW() = ', W2.CCW())
    print('V2.iner_prod(W2) = ', V2.iner_prod(W2))
