gamers = []

def add_gamer(gamer, gamers_list):
    if "name" in gamer and "availability" in gamer:
        gamers_list.append(gamer)

add_gamer({"name": "Kimberly Warner", "availability": ["Monday", "Tuesday", "Friday"]}, gamers)

add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

def build_daily_frequency_table():
    return {
        "Monday": 0,
        "Tuesday": 0,
        "Wednesday": 0,
        "Thursday": 0,
        "Friday": 0,
        "Saturday": 0,
        "Sunday": 0,
    }

count_availability = build_daily_frequency_table()

def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day in gamer['availability']:
            count_availability[day] += 1

calculate_availability(gamers, count_availability)
print(count_availability)

def find_best_night(availability_table):
    highest_count = 0
    best_night = ""
    for day, frequency in availability_table.items():
        if frequency > highest_count:
            highest_count = frequency
            best_night = day
    return best_night

game_night = find_best_night(count_availability)
print(game_night)

def available_on_night(gamers_list, day):
    people_available_on_night = []
    for gamer in gamers_list:
        if day in gamer['availability']:
            people_available_on_night.append(gamer['name'])
    return people_available_on_night

attending_game_night = available_on_night(gamers, game_night)
print(attending_game_night)

def send_email(gamers_who_can_attend, day, game):
    for name in gamers_who_can_attend:
        form_email = f"""
            Dear {name},
            the {game} game night will be on {day} night.
            See you then!
        """
        print(form_email)

send_email(attending_game_night, game_night, "Abruptly Goblins!")
