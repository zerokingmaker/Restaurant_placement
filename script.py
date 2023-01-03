tables = {
  1: {
    'name': 'Jiho',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes',
      'total': [534.50, 20.0, 5]
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}

# de quoi assigner une table 
def assign_table(table_number, name, vip_status=False): 
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = {}

# de quoi rajouter de la nourriture
def assign_food_items(table_number, **order_items):
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  tables[table_number]['order']['food_items'] = food
  tables[table_number]['order']['drinks'] = drinks

# calculer le prix individuel en fonction du total précisé dans le diction
def calculate_price_per_person(table_number, tip, split):
    total =  sum(tables[table_number]['total'])
    total_tip = total * (tip/100)
    split_price = (total + total_tip) / split
    print('Your total is {}'.format(total))
    print(split_price)

# pour enlever le guest
def remove_guests(table_number):
  tables[table_number] = {}

# Pour enlever ou supprimer une commande. Par défaut je laisse ça sur 'False' donc on ajoute des plats
def update_order_items(table_number, remove=False, **order_items):
  
  food = order_items.get('food', '')
  drinks = order_items.get('drinks', '')
  # On vérifie si on modifie ou non
  if not remove:
    # ici on rajoute donc 
    tables[table_number]['order']['food_items'] += ', {}'.format(food)
    tables[table_number]['order']['drinks'] += ', {}'.format(drinks)
  else :
    # Là on enlève
    # On va d'abord transformer le string en array puis loop dessus
    food_array = tables[table_number]['order']['food_items'].split(',')
    for food in food.split(','):
      if food in food_array:
        # on vérifi si la nourriture était déjà présente, si c'est le cas on l'enlève
        food_array.remove(food)
    # ici à la fin on retourne donc une string    
    food_string = (' ,'.join(food_array))
    # même principe mais pour les boissons
    drinks_array = tables[table_number]['order']['drinks'].split(',')
    for drink in drinks.split(','):
      if drink in drinks_array:
        drinks_array.remove(drink)
    
    drinks_string = (' ,'.join(drinks_array))
    tables[table_number]['order']['food_items'] = food_string
    tables[table_number]['order']['drinks'] = drinks_string

# Ceci permet de vérifier si on a une table disponible
queue_list = []
def see_availabilyty(table_number, name, vip_status=False):
  if tables[table_number] == {}:
    print("Your table is available. We will assign you to it")
     # donc si la table est disponible on ajoute le client dessus
    assign_table(table_number, name, vip_status)
  else :
    # s'il n'y pas de table disponible on le met sur la file d'attente et on lui dit combien de client reste t'il avant lui
    print("We will put you on reservation")
    queue_list.append(name)
    print('There is {} clients before you'.format(len(queue_list) - 1))

assign_table(2, 'Fred')
tables[2]['total'] = [23, 40, 55]

calculate_price_per_person(2, 0.2, 2)

assign_food_items(2, food='Pizza, burger', drinks='Coca, Sprite')
update_order_items(2,True ,food='Pizza')

see_availabilyty(3, 'Jean')
print(tables)
