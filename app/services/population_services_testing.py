from typing import List

from app.models.population import PopulationRecord
from app.services.population_request import fetch_population_data


def print_fetch_population():

    # ✅ write the code to print the response of the request that is coming from population_request and show the data in the console
    
    return


# 🔵 Test 1: devolver data básica con campos renombrados
def fetch_population_modified() -> List[PopulationRecord]:
    # ✅ Parse the response corresponding to the test that has been given to you
    # 💥 Remember that the typing of the object is a must; go to models to see the class
    # ✅ complete the function fetch_population_modified that returns a list of PopulationRecord
    
    
    response = fetch_population_data()
   
    records  = [
        {
            "year": int(entry["Year"]),
            "population": entry["Population"],
            "nation": entry["Nation"],
        }
        for entry in response["data"]
    ]
    return records




if __name__ == "__main__":
    # ✅ To see the data in the console, call the function here using 
    #  python -m app.services.population_services_testing 

    print("Test")
    print_fetch_population()
    print(fetch_population_modified())

