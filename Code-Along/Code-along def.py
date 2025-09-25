# Icke-standard representation av siffror
# one = " "
# two = "uf"
# Three = "@£€"

# def plus(a, b):
#     return " " * (len(a) + len(b))

# len(plus(one,two))

class NonStandardInt:
    def __init__(self, num_str):
        self.num_str = num_str

    def __repr__(self):
        return repr(len(self.num_str))
    
    def __add__(self, other):
        if not isinstance(other, NonStandardInt):
            raise ValueError(f"Can't add {repr(other)} to NonStandardInt.")
       
        return NonStandardInt(" " * (len(self) + len(other)))
    
    def __len__(self):
        return len(self.num_str)


a = NonStandardInt("    ")
print(a) 
b = NonStandardInt("htu")
print(a + b)
