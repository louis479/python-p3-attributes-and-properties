class Dog:
    APPROVED_BREEDS = [
        "Mastiff",
        "Chihuahua",
        "Corgi",
        "Shar Pei",
        "Beagle",
        "French Bulldog",
        "Pug",
        "Pointer"
    ]

    def __init__(self, name=None, breed=None):
        self.name = None  # Ensure `name` is always initialized
        self.breed = None  # Ensure `breed` is always initialized
        
        if name is not None:
            self.set_name(name)

        if breed is not None:
            self.set_breed(breed)

    def set_name(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")  # Match test case
        else:
            self.name = name

    def set_breed(self, breed):
        if breed not in self.APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")  # Match test case
            self.breed = None  # Explicitly set breed to None if invalid
        else:
            self.breed = breed  
