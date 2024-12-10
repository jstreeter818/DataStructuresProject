'''contains initializations of all item objects'''

import items.item_class as item_class
import items.item_actions as item_actions
import items.item_descriptions as item_descriptions
import game_objects.rooms as rooms

broken_clock = item_class.Item("Broken Clock", item_descriptions.broken_clock, rooms.foyer, True, item_actions.fix_clock)
rooms.foyer.items.append(broken_clock)

chandelier = item_class.Item("Chandelier", item_descriptions.chandelier, rooms.foyer, True)
rooms.foyer.items.append(chandelier)

painting = item_class.Item("Landscape Painting", item_descriptions.landscape_painting, rooms.main_gallery, True)
rooms.main_gallery.items.append(painting)

old_tome = item_class.Item("Old tome", item_descriptions.old_tome, rooms.library, use_func=item_actions.read_tome)
rooms.library.items.append(old_tome)

map = item_class.Item("Map", ["A map of the museum"], location=None, use_func=item_actions.print_map)

lamp = item_class.Item("Strange lamp", item_descriptions.lamp, rooms.portrait_gallery, static=True, use_func=item_actions.use_lamp)
rooms.portrait_gallery.items.append(lamp)

cat_treats = item_class.Item("Cat treats", item_descriptions.cat_treats, rooms.cafe)
rooms.cafe.items.append(cat_treats)

decoder = item_class.Item("Decoder", item_descriptions.decoder, rooms.secret_room)
rooms.secret_room.items.append(decoder)

stone_statue = item_class.Item("Stone statue", item_descriptions.stone_statue, rooms.sculpture_garden, static=True)
rooms.sculpture_garden.items.append(stone_statue)

water_fountain = item_class.Item("Water fountain", item_descriptions.water_fountain, rooms.courtyard, static=True)
rooms.courtyard.items.append(water_fountain)

coin = item_class.Item("Coin", item_descriptions.coin, rooms.mail_room, use_func=item_actions.toss_coin)
rooms.mail_room.items.append(coin)

lock_box = item_class.Item("Lock Box", item_descriptions.lock_box, rooms.mail_room, True, use_func=item_actions.open_box)
rooms.mail_room.items.append(lock_box)

stool = item_class.Item("Stool", item_descriptions.stool, rooms.closet, use_func=item_actions.place_stool)
rooms.closet.items.append(stool)