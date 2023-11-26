gamers = []

def add_gamer(gamer, gamers_list):
    if "name" in gamer and "availability" in gamer:
        gamers_list.append(gamer)

add_gamer({"name": "Kimberly Warner", "availability": ["Mondays", "Tuesdays", "Fridays"]}, gamers)

add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

print(gamers)
