car_list_get="""
every user can just see list of your's car 
and user should log in 
"""
car_list_post = """
user should log in 
user should create car 
user can :
        manay small car 
        one  big car 
type:
  type 1 --> small car
  type 2 --> big car 
  
model create car sample:
        {
            "type": "2",
            "color": "blue",
            "length": 45,
            "load_valume": 0
        }
"""
car_list_color_get ="""

user should  log in 
you can get list car color has red or blue 

"""

car_list_age_get ="""

user should  log in 
you can get list car owner's or creater greater than 70

"""

carfine_list_get="""
all  car across a width add that car to this models 
this api show all big car across a route that width lower than 20
sample :
        {
            "id": 1,
            "car": {
                "id": 1,
                "owner": 1,
                "type": "2",
                "color": "white",
                "length": 6,
                "load_valume": 300
            },
            "route": 1,
            "date": "2023-01-15"
        }
    

"""