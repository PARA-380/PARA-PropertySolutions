from Entity import Entity
class Property(Entity):
    #put the instance variables here like (name : string, ...)
    #TODO: create the Tenant Class and include
    def __init__(self, address : str = None, tenant : str = None, size : str = None, type : str = None, maximum_living : int = None): 
        pass


def main() -> None:
    obj = Property()
    print(obj)
    obj.toJSON()

if __name__ == "__main__":
    pass