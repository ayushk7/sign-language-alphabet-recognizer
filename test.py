def my_generator():
    for i in range(5):
        yield i

# Create a generator object
gen = my_generator()

# Set an attribute on the generator object
# setattr(gen, 'mode', 'normal')

gen.mode = 'normal'

# Try to access the attribute before it has been set
print(gen.mode)