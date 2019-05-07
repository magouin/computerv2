import Imaginary as im

class Matrice:
	def __init__(self, ar):
		if (not isinstance(ar, list)):
			raise ValueError
		if (isinstance(ar[0], list)):
			size = len(ar[0])
		self.w = size
		self.h = len(ar)
		self.ar = [[im.Imaginary(0) for x in range(self.w)] for y in range(self.h)]
		for i in range(self.h):
			if (not isinstance(ar[0], list)):
				raise ValueError
			if (size != len(ar[i])):
				raise ValueError
			for j in range(self.w):
				if (not (isinstance(ar[i][j], int) or isinstance(ar[i][j], float) or isinstance(ar[i][j], im.Imaginary))):
					raise ValueError
				self.ar[i][j] = im.Imaginary(ar[i][j])
	def get_size(self):
		return(self.h, self.w)
	def __add__(self,other):
		if not isinstance(other, Matrice):
			raise ValueError
		if (self.get_size() != other.get_size()):
			raise IndexErrors
		ar = [[self[y][x] + other[y][x] for x in range(self.w)] for y in range(self.h)]
		ar = [[self[y][x] + other[y][x] for x in range(self.w)] for y in range(self.h)]
		return (Matrice(ar))
	def __sub__(self,other):
		if not isinstance(other, Matrice):
			raise ValueError
		if (self.get_size() != other.get_size()):
			raise IndexErrors
		ar = [[self[y][x] + other[y][x] for x in range(self.w)] for y in range(self.h)]
		ar = [[self[y][x] - other[y][x] for x in range(self.w)] for y in range(self.h)]
		return (Matrice(ar))
	def __getitem__(self,key):
		if (key >= self.h):
			raise IndexError
		return (self.ar[key])
	def __setitem__(self, key, item):
		if (key >= self.h):
			raise IndexError
		self.ar[key] = item
	def __mul__(self,other):
		if isinstance(other, Matrice):
			if (self.w != other.h):
				raise ValueError
			ar = [[im.Imaginary(0) for x in range(other.w)] for y in range(self.h)]
			for i in range(self.h):
				for j in range(other.w):
					for k in range(self.w):
						ar[i][j] += self[i][k] * other[k][j]
			return (Matrice(ar))
		elif (isinstance(other, int) or isinstance(other, float) or isinstance(other, im.Imaginary)):
			ar = [[self[j][i] * other for i in range(self.w)] for j in range(self.h)]
			return (Matrice(ar))
		else:
			raise ValueError
	def __div__(self, other):
		if (isinstance(other, int) or isinstance(other, float) or isinstance(other, im.Imaginary)):
			if (other == 0): raise ZeroDivisionError
			ar = [[self[j][i] / other for i in range(self.w)] for j in range(self.h)]
			return (Matrice(ar))
		raise ValueError
	def __str__(self):
		ret = ""
		for i in range(self.h):
			ret += "  ["
			for j in range(self.w):
				ret += " {0} ".format(self[i][j])
				if (j != self.w - 1):
					ret += ","
			ret += "]"
			if (i != self.h - 1):
				ret += "\n"
		return (ret)
