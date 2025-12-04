

file_path = "c:/Users/hadiz/OneDrive/Bureau/AOC/day1AOC/input.txt"

# Lecture du fichier
with open(file_path, "r") as file:
    rotations = [line.strip() for line in file.readlines()]

# Initialisation
position = 50   # Position de départ
count_zero = 0  # Compteur pour le nombre de fois où on atteint 0


for rotation in rotations:
    direction = rotation[0]   # 'L' ou 'R'
    steps = int(rotation[1:]) # nombre de pas

    if direction == 'L':
        position = (position - steps) % 100
    else:  
        position = (position + steps) % 100

    if position == 0:
        count_zero += 1


print("Le mot de passe est :", count_zero)
