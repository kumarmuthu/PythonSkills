__version__ = "2023.04.01.01"
__author__ = "Muthukumar Subramanian"

'''
Python Banner Utility, the Banner text will display with Foreground(text) and Background colours.
Banner package - pyfiglet
Colour package - colorama
'''

from colorama import Fore, Back, Style
import pyfiglet
import random


# Define banner text
banner_text = "Muthukumar S"

# Get all fonts
get_all_fonts = pyfiglet.FigletFont.getFonts()
# print(f"Get all fonts: {get_all_fonts}")

# Random number for fonts
get_random_number_for_font = random.randint(0, len(get_all_fonts) - 1)

# Scenario: 1 - Print all fonts for Banner text
print("{:*^30}".format(" Scenario - 1 Start "))
for each_font in get_all_fonts:
    length = len(banner_text)
    font_obj = pyfiglet.Figlet(font=each_font)
    # Calculate width, it is based on the banner text and fonts
    font_width = sum([font_obj.renderText(char).find('\n') for char in banner_text])
    width = max(length, font_width)
    output_text = pyfiglet.figlet_format(banner_text, font=each_font, width=width, justify='center')
    # Print the banner
    print(output_text)
print("{:*^30}".format(" Scenario - 1 End "))

# Scenario: 2 - Colour Banner text
print("{:*^30}".format(" Scenario - 2 Start "))
# Get all colours for Foreground and Background
colour_dict = Fore.__dict__
bg_colour_dict = Back.__dict__
# Shuffle colours
list_of_colours = list(colour_dict.keys())
random.shuffle(list_of_colours)
list_of_bg_colours = list(bg_colour_dict.keys())
random.shuffle(list_of_bg_colours)

# Avoid colour conflict for Foreground and Background
while True:
    a = random.randint(0, len(list_of_colours) - 1)
    b = random.randint(0, len(list_of_bg_colours) - 1)
    if list_of_bg_colours[b] != list_of_colours[a]:
        # print("list_of_colours[a]: ", list_of_colours[a])
        text_colour = Fore.__getattribute__(list_of_colours[a])
        bg_colour = Back.__getattribute__(list_of_bg_colours[b])  # Back.BLACK
        break

# Format the Banner text
banner = pyfiglet.figlet_format(banner_text)
# Add colours for the formatted banner text
formatted_text = f"{text_colour}{bg_colour}{banner}{Style.RESET_ALL}"
# Print the banner
print(formatted_text)
print("{:*^30}".format(" Scenario - 2 End "))

# Scenario: 3 - Foreground and Background Colours with permutation and combination for the Banner text
print("{:*^30}".format(" Scenario - 3 Start "))
# Get all colours for Foreground and Background
colour_dict = Fore.__dict__
bg_colour_dict = Back.__dict__
list_of_colours = list(colour_dict.keys())
list_of_bg_colours = list(bg_colour_dict.keys())

# Generate Permutation and Combination List
permutation_list = []
for i in list_of_colours:
    for j in list_of_bg_colours:
        permutation_list.append((i, j))
print(f"Permutation and Combination List: {permutation_list}\n Permutation Length: {len(permutation_list)}")

index_count = 0
for ind, each_tuple in enumerate(permutation_list):
    # Avoid same colour combination
    if each_tuple[0] == each_tuple[1] or each_tuple[0] == 'RESET' and each_tuple[1] == 'RESET':
        continue
    text_colour = Fore.__getattribute__(each_tuple[0])
    bg_colour = Back.__getattribute__(each_tuple[1])

    # Method - 1
    # Custom font, width with banner text
    # length = len(banner_text)
    # font_obj = pyfiglet.Figlet(font=get_all_fonts[get_random_number_for_font])
    # font_width = sum([font_obj.renderText(char).find('\n') for char in banner_text])
    # width = max(length, font_width)
    # output_text = pyfiglet.figlet_format(banner_text, font=get_all_fonts[get_random_number_for_font],
    #                                      width=width, justify='center')

    # Method - 2
    # Default font, width with banner text
    output_text = pyfiglet.figlet_format(banner_text)

    # Add colours for the formatted banner text
    formatted_banner_text = f"{text_colour}{bg_colour}{output_text}{Style.RESET_ALL}"
    index_count += 1
    # Print the banner
    print(formatted_banner_text)
print(f"Formatted Banner Text Length: {index_count}")
print("{:*^30}".format(" Scenario - 3 End "))
