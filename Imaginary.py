import Matrice as mat

class Imaginary:
	def __init__(self, rel, im = None):
		if (im == None):
			self.im = 0
		elif (isinstance(im, float) or isinstance(im, int)):
			self.im = im
		else:
			raise ValueError
		if (isinstance(rel, Imaginary)):
			self.rel = rel.rel
			self.im = rel.im
		elif (isinstance(rel, float) or isinstance(rel, int)):
			self.rel = float(rel)
		else:
			raise ValueError
	def conju(self):
		return (Imaginary(self.rel, -self.im))
	def __add__(self,other):
		if (isinstance(other, Imaginary)):
			return (Imaginary(self.rel + other.rel, self.im + other.im))
		elif (isinstance(other, float) or isinstance(other, int)):
			return (Imaginary(self.rel + other));
		elif (isinstance(other, mat.Matrice)):
			return (other + self);
		else:
			raise ValueError
	def __sub__(self,other):
		if (isinstance(other, Imaginary)):
			return (Imaginary(self.rel - other.rel, self.im - other.im))
		elif (isinstance(other, float) or isinstance(other, int)):
			return (Imaginary(self.rel - other));
		elif (isinstance(other, mat.Matrice)):
			return (other - self);
		else:
			raise ValueError
	def __div__(self,other):
		if (isinstance(other, float) or isinstance(other, int)):
			if (other == 0): raise ZeroDivisionError
			return (Imaginary(self.rel / other, self.im / other))
		elif (isinstance(other, Imaginary)):
			return (self * other.conju() / (other.rel * other.rel + other.im * other.im))
		elif (isinstance(other, mat.Matrice)):
			return (other / self);
		else:
			raise ValueError
	def __mul__(self,other):
		if (isinstance(other, Imaginary)):
			return (Imaginary(self.rel * other.rel - self.im * other.im, self.rel * other.im + self.im * other.rel))
		elif (isinstance(other, float) or isinstance(other, int)):
			return (Imaginary(self.rel * other, self.im * other))
		elif (isinstance(other, mat.Matrice)):
			return (other * self);
		else:
			raise ValueError
	def __iadd__(self, other):
		if (isinstance(other, Imaginary)):
			self.rel += other.rel
			self.im += other.im
			return (self)
		elif (isinstance(other, float) or isinstance(other, int)):
			self.rel += other;
			return (self)
		else:
			raise ValueError
	def __isub__(self,other):
		if (isinstance(other, Imaginary)):
			self.rel -= other.rel
			self.im -= other.im
			return (self)
		elif (isinstance(other, float) or isinstance(other, int)):
			self.rel -= other;
			return (self)
		else:
			raise ValueError
	def __idiv__(self,other):
		if (isinstance(other, float) or isinstance(other, int)):
			if (other == 0): raise ZeroDivisionError
			self.rel /= other
			self.im /= other
		elif isinstance(other, Imaginary):
			self *= other.conju()
			self /= other.rel * other.rel + other.im * other.im
		else:
			raise ValueError
		return (self)
	def __imul__(self,other):
		if (isinstance(other, Imaginary)):
			tmp = self.rel
			self.rel = self.rel * other.rel - self.im * other.im
			self.im = tmp * other.im + self.im * other.rel
			return (self)
		elif (isinstance(other, float) or isinstance(other, int)):
			self.rel *= other
			self.im *= other
			return (self)
		raise ValueError
	def __str__(self):
		ret = ""
		r = str(self.rel)
		i = str(self.im)
		iabs = str(abs(self.im))
		if (int(self.rel) == self.rel): r = str(int(self.rel))
		if (int(self.im) == self.im): i = str(int(self.im))
		if (int(self.im) == self.im): iabs = str(abs(int(self.im)))
		if (not self.rel and not self.im):
			return ("0")
		if (not self.im):
			return ("{0}".format(r))
		if (not self.rel):
			if (self.im == 1): return ("i")
			if (self.im == -1): return ("-i")
			return ("{0}i".format(i))
		ret += "{0} ".format(r)
		if (self.im < 0): ret += "- "
		else: ret += "+ "
		if (self.im == 1 or self.im == -1): ret += ("i")
		else: ret += "{0}i".format(iabs)
		return (ret)
