class Tested():
    def __init__(self, name="Memecoin", symbol="MCOIN", totalSupply=1_000_000_000, owner="friend"):
        self.name = name
        self.symbol = symbol
        self.totalSupply = totalSupply
        self.owner = owner
    
    def info(self):
        return f"{self.name}, {self.symbol}, {self.totalSupply}, {self.owner}"
    
    def mint(self, totalSupply):
        value = 15
        self.totalSupply += value
        return self.totalSupply
    
    def burn(self, totalSupply):
        value = 25
        self.totalSupply -= value
        return self.totalSupply 
    
        
t1 = Tested()
t1.mint(15)

t2 = Tested("Lolcoin", "LOLCOIN", 1_000_000, "Bob")
t2.burn(25)

if __name__ == '__main__':
    print(t1.info())
    print(t2.info())
