from example_utils import generate_example_dicts
from distances import pearson

a, b = generate_example_dicts()

print(pearson(a,b))
# >>> 1.01539364936107