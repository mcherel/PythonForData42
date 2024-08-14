from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_blue
from pimp_image import ft_grey

...
array = ft_load("landscape.jpg")
ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)
print(ft_invert.__doc__)
""" Expected output: (docstrings can be different)
$> python tester.py
The shape of image is: (257, 450, 3)
[[[19 42 83]
[23 42 84]
[28 43 84]
...
[ 0 0 0]
[ 1 1 1]
[ 1 1 1]]]
...
Inverts the color of the image received. """
