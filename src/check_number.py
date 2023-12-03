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

def check_number(n: complex, max_iter: int):
    z = 0
    for i in range(0, max_iter):
        z = (z*z) + n
        if abs(z.real) > 2 or abs(z.imag) > 2:
            # // print(i / max_iter)
            
            return int(255 * (i / max_iter))
    else:
        return 255
    
# // check_number(-1, 1000)