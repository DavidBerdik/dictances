from example_utils import generate_example_dicts
from distances import chebyshev

a, b = generate_example_dicts()

print(chebyshev(a,b))
# >>> 997.7027254146534