    # mandelbrot-explorer-py: A mandelbrot set exploration tool
    # Copyright (C) 2023  Ari Kanbur

    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.

    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with this program.  If not, see <https://www.gnu.org/licenses/>.

from PIL import Image, ImageDraw
from check_number import check_number

def render():
    RESULUTION = 1000

    # iterate through complex numbers from -2 + 2i to 2 + -2i
    # and append to mandelbrot_set array
    mandelbrot_set = []
    n = -2 + 2j
    # // n = -174666 + 0.525333j
    for i in range(0, RESULUTION+1):
        mandelbrot_set.append([])
        for j in range(0, RESULUTION+1):
            mandelbrot_set[i].append(check_number(n, 80))
            n += 4 / RESULUTION
        n -= 4 + (4 / RESULUTION)
        n -= 4j / RESULUTION

    print(mandelbrot_set)

    image = Image.new('RGB', (RESULUTION, RESULUTION), (0, 0, 0))
    draw = ImageDraw.Draw(image)

    # draw the mandebrot set from the mandelbrot_set array
    x = 0
    y = 0
    for i in mandelbrot_set:
        for j in i:                          
            draw.point([x, y], (j, j, j))
            x += 1
        y += 1
        x = 0

    image.save("mandelbrot_set.png", 'PNG')