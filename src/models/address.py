
import pyap
#from src.models.field import Field
from field import Field

class Address(Field):
    """ creates dictionary with address details from provided string """
    def __init__(self, address: str) -> dict:
        self.__address = {}
        self.address = address

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        parsed_address = pyap.parse(address, country='US')[0]
        self.__address["street"] = parsed_address.street_number + " " + parsed_address.street_name
        self.__address["city"] = parsed_address.city
        self.__address["state"] = parsed_address.region1
        self.__address["postal_code"] = parsed_address.postal_code
        self.__address["country"] = parsed_address.country_id
        
            
    def __str__(self):
        address_detail = (f"street:      {self.address["street"]}  {'\n'}"
             f"city:        {self.address["city"]} {'\n'}"
             f"postal_code: {self.address["postal_code"]} {'\n'}"
             f"state:       {self.address["state"]} {'\n'}"
             f"country:     {self.address["country"]}")

        return address_detail




# # Driver Code
if __name__ == '__main__':
    test_address = """
        Lorem ipsum, 225 E. John Carpenter Freeway, Suite 1500 Irving, Texas 75062, Dorem sit amet
        """
    address = Address(test_address)
    print(address)