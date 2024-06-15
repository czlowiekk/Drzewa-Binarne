import random
import time
import numpy as np

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class SplayTree:
    def __init__(self):
        self.root = None

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def splay(self, key):
        if self.root is None or self.root.key == key:
            return self.root

        dummy = Node(None)
        left = right = dummy
        cur = self.root

        while True:
            if key < cur.key:
                if cur.left is None:
                    break
                if key < cur.left.key:
                    cur = self.rotate_right(cur)
                    if cur.left is None:
                        break
                right.left = cur
                right = cur
                cur = cur.left
                right.left = None
            elif key > cur.key:
                if cur.right is None:
                    break
                if key > cur.right.key:
                    cur = self.rotate_left(cur)
                    if cur.right is None:
                        break
                left.right = cur
                left = cur
                cur = cur.right
                left.right = None
            else:
                break

        left.right = cur.left
        right.left = cur.right
        cur.left = dummy.right
        cur.right = dummy.left
        self.root = cur

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return

        self.splay(key)

        if key < self.root.key:
            node = Node(key)
            node.left = self.root.left
            node.right = self.root
            self.root.left = None
            self.root = node
        elif key > self.root.key:
            node = Node(key)
            node.right = self.root.right
            node.left = self.root
            self.root.right = None
            self.root = node

    def search(self, key):
        self.splay(key)
        if self.root.key == key:
            return True
        return False


class Node2:
    def __init__(self, data = None, par = None):
        self.data = data
        self.left = self.right = None
        self.parent = par
        
class Tree:
    def __init__(self):
        self.dummy = Node('u')
        self.root = self.dummy.right
        # do korzenia dodajemy sztucznego rodzica
    
    def find(self, node, value):
        if node is None:
            return None, False
        
        if value == node.data:
            return node, True
        
        if value < node.data:
            if node.left:
                return self.find(node.left, value)
        
        if value > node.data:
            if node.right:
                return self.find(node.right, value)
        
        return node, False
    
    def append(self, obj):
        if self.root is None:
            self.root = obj
            self.root.parent = self.dummy
        
        s, fl_find = self.find(self.root, obj.data)
        
        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
                obj.parent = s
            else:
                s.right = obj
                obj.parent = s
        
    def show_tree(self, node):
        if node is None:
            return
        
        self.show_tree(node.left)
        print(node.data, end = ",")
        self.show_tree(node.right)
    
    
    def suma(self, node):
        if node is None:
            return 0
         
        return self.suma(node.left) + node.data + self.suma(node.right)
    
    def count(self, node):
        if node is None:
            return 0
         
        return self.count(node.left) + 1 + self.count(node.right)
    
    def height(self, node):
        if node is None:
            return 0
        
        l = self.height(node.left)
        r = self.height(node.right)
        
        if (l>r):
            return l+1
        # ja + lewa noga
        
        return r+1
        # ja + prawa noga
        
    def mini(self, node):
        while node is None:
            return node
        while node.left:
            node =  node.left
        return node
            

    def myk(self, node, depth = 0):
        # wyświetla drzewo tak, żeby wyglądało w miarę jak drzewo
        if node is None:
            return
        
        if node.right:
            self.myk(node.right, depth + 1)
        
        for _ in range(0, depth):
            print("    ", end = "")
        
        print(node.data)
        
        if node.left:
            self.myk(node.left, depth + 1)
     
    def del_leaf(self, node):
        if node.parent.left == node:
            node.parent.left = None
        if node.parent.right == node:
            node.parent.right = None
    
    def del_one_child(self, node):
        if node.parent.right == node:
            if node.right:
                node.parent.right = node.right
            if node.left:
                node.parent.left = node.left
        elif node.parent.left == node:
            if node.left:
                node.parent.left = node.left
            if node.right:
                node.parent.right = node.right
                
            
    
    def del_node(self, key):
        s, pl_find = self.find(self.root, key)
        
        if not pl_find:
            return
        
        if s.left is None and s.right is None:
            self.del_leaf(s)
        elif s.left is None or s.right is None:
            self.del_one_child(s)
        else:
            nd = self.mini(s.right)
            s.data = nd.data
            self.del_one_child(nd)
            
    def Rotate(self,B):
        if (B == self.dummy or B == None or B == self.root):
            return
        
        A = B.parent
        P = A.parent
        
        #rotacja w prawo
        if A.left == B:
            B.parent = p
            
            if (P.right == A):
                P.right = B
            else:
                P.left = B
                
            beta = B.right
            
            B.parent = B
            B.right = A
            
            A.left = beta
            
            if beta:
                beta.append = A
                
            if self.root.parent != self.dummy:
                self.root = self.dummy.right
                



def measure_BST_creation_time():
    # Tworzenie drzewa BST
    t = Tree()

    # Dodawanie wszystkich liczb naturalnych z przedziału [1 - zakres] w losowej kolejności
    czas_poczatkowy = time.time()
    numbers = list(range(1, 10001))
    random.shuffle(numbers)
    for number in numbers:
        t.append(Node2(number))
    czas_koncowy = time.time()

    czas_tworzenia = czas_koncowy - czas_poczatkowy

    # Wyświetlenie czasu utworzenia drzewa
    print(f'Utworzono nierównoważone drzewo BST w {czas_tworzenia} sekund')

def measure_splay_creation_time():
    # Tworzenie drzewa Splay
    splay_tree = SplayTree()

    # Dodawanie wszystkich liczb naturalnych z przedziału [1 - zakres] w losowej kolejności
    czas_poczatkowy = time.time()
    liczby = list(range(1, 10001))
    random.shuffle(liczby)
    for liczba in liczby:
        splay_tree.insert(liczba)
    czas_koncowy = time.time()
    
    czas_tworzenia = czas_koncowy - czas_poczatkowy

    # Wyświetlenie czasu utworzenia drzewa
    print(f'Utworzono drzewo Splay w {czas_tworzenia} sekund')


def nazwa_rozkładu(rozklad):
    if rozklad is None:
        return "jednostajnego"
    elif rozklad == Rozkład_normalny:
        return "normalnego"
    elif rozklad == Rozkład_odwrotny:
        return "odwrotnego"
    elif rozklad == Rozkład_liniowy:
        return "liniowego"
    elif rozklad == Rozkład_kwadratowy:
        return "kwadratowego"
    elif rozklad == Rozkład_potęgowy:
        return "potęgowy"


def measure_BST_search_time(tree,rozklad_prawdopodobienstwa=None):
    zakres = range(1, 10001)
    
    if rozklad_prawdopodobienstwa:
        random_numbers = np.random.choice(zakres, 50000, p=rozklad_prawdopodobienstwa)
    else:
        random_numbers = np.random.randint(1, 10001, 50000)

    czas_poczatkowy_szukania = time.time()
    for random_number in random_numbers:
        result = tree.find(tree.root, random_number)
    czas_koncowy_szukania = time.time()

    # Obliczanie czasu wykonania testów
    czas_szukania = czas_koncowy_szukania - czas_poczatkowy_szukania

    # Wyświetlenie wyników wyszukiwania
    nazwa = nazwa_rozkładu(rozklad_prawdopodobienstwa)
    print(f"Dla rozkładu {nazwa}")
    print(f"Wyszukanie 50000 razy w drzewie losowej liczby zajeło {czas_szukania} sekund")


def measure_splay_search_time(tree, rozklad_prawdopodobienstwa=None):
    zakres = range(1, 10001)
    
    if rozklad_prawdopodobienstwa:
        random_numbers = np.random.choice(zakres, 50000, p=rozklad_prawdopodobienstwa)
    else:
        random_numbers = np.random.randint(1, 10001, 50000)

    czas_poczatkowy_szukania = time.time()
    for random_number in random_numbers:
        result = tree.search(random_number)
    czas_koncowy_szukania  = time.time()

    # Obliczanie czasu wykonania testów
    czas_szukania = czas_koncowy_szukania - czas_poczatkowy_szukania 

    # Wyświetlenie wyników wyszukiwania
    nazwa = nazwa_rozkładu(rozklad_prawdopodobienstwa)
    print(f"Dla rozkładu {nazwa}")
    print(f"Wyszukanie 50000 razy w drzewie losowej liczby zajeło {czas_szukania} sekund")



print('Zakres liczb: (1, 10000)')

measure_BST_creation_time()
measure_splay_creation_time()  

print('\n')


# Definicje różnych rozkładów prawdopodobieństwa

# Rozkład prawdopodobieństwa normalny
mu, sigma = 5000, 2000  # średnia i odchylenie standardowe
Rozkład_normalny = [random.normalvariate(mu, sigma) for _ in range(10000)]
Rozkład_normalny = [min(max(x, 1), 10000) for x in Rozkład_normalny]  # Ograniczenie wartości do przedziału [1, 10000]
Rozkład_normalny = [x / sum(Rozkład_normalny) for x in Rozkład_normalny]  # normalizacja

# Rozkład prawdopodobieństwa odwrotnie proporcjonalny do wartości:
Rozkład_odwrotny = [1/i for i in range(1, 10001)]
Rozkład_odwrotny = [x / sum(Rozkład_odwrotny) for x in Rozkład_odwrotny]  # normalizacja

# Rozkład prawdopodobieństwa liniowy:
Rozkład_liniowy = [i for i in range(1, 10001)]
Rozkład_liniowy = [x / sum(Rozkład_liniowy) for x in Rozkład_liniowy]  # normalizacja

# Rozkład prawdopodobieństwa kwadratowy:
Rozkład_kwadratowy = [i**2 for i in range(1, 10001)]
Rozkład_kwadratowy = [x / sum(Rozkład_kwadratowy) for x in Rozkład_kwadratowy]  # normalizacja

# Rozkład potęgowy
k = 6
Rozkład_potęgowy = [1/i**k for i in range(1, 10001)]
Rozkład_potęgowy = [x / sum(Rozkład_potęgowy) for x in Rozkład_potęgowy]  # normalizacja



# Lista różnych rozkładów prawdopodobieństwa
rozklad_prawdopodobienstwa = [
    None,  # Jednostajny rozkład prawdopodobieństwa
    Rozkład_normalny,
    Rozkład_odwrotny,
    Rozkład_liniowy,
    Rozkład_kwadratowy,
    Rozkład_potęgowy
]

 
print('Dla drzewa BST:')
t = Tree()
numbers = list(range(1, 10001))
random.shuffle(numbers)
for number in numbers:
    t.append(Node2(number))
for rozklad in rozklad_prawdopodobienstwa:
    measure_BST_search_time(t,rozklad)
    print('\n')
    
root_splay = None
liczby = list(range(1, 10001))
random.shuffle(liczby)
splay_tree = SplayTree()
for liczba in liczby:
    splay_tree.insert(liczba)

print('Dla drzewa splay:')
for rozklad in rozklad_prawdopodobienstwa:
    measure_splay_search_time(splay_tree, rozklad)
    print('\n')


