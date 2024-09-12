
def asteroidsDestroyed(mass, asteroids):
    asteroids.sort()
    for asteroid in asteroids:
        if mass < asteroid:
            return False
        mass += asteroid
    return True


print(asteroidsDestroyed(mass=10, asteroids=[3, 9, 19, 5, 21]))  # True
print(asteroidsDestroyed(mass=5, asteroids=[4, 9, 23, 4]))  # False
