class Pet:
    pass
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self, name, pet_type, owner = None):
        self.name = name
        self.owner = owner
        Pet.all.append(self)
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")
        
        self.pet_type = pet_type
    

class Owner:
    pass
    def __init__(self, name):
        self.name = name
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Failed to add pet")
        
        pet.owner = self
    def get_sorted_pets(self):
        return sorted(self.pets(), key = lambda pet:pet.name)