import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def step(grid):
    return (
        np.roll(grid,  1, axis=0) +  # up
        np.roll(grid, -1, axis=0) +  # down
        np.roll(grid,  1, axis=1) +  # left
        np.roll(grid, -1, axis=1)    # right
    ) % 7
img = Image.open("./resources/bonus_secret_statement.png").convert("L")
grid = np.array(img, dtype=np.int64) % 7
g = grid.copy()

for i in range(50):
    g = step(g)
    print(f"step {i+1}: unique values =", np.unique(g))
h, w = grid.shape
total = grid.sum() % 7

steps = 10**12
multiplier = pow(4, steps, 7)

final_value = (total * multiplier) % 7
final_image = np.full((h, w), final_value, dtype=np.uint8)
out = Image.fromarray(final_image * 36)  # scale for visibility
out.save("final.png")
plt.imshow(final_image)
plt.show()