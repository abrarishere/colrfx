# colrfx/main.py

import json
import os

path = os.path.dirname(os.path.abspath(__file__))

with open(f"{path}/colors.json", "r") as f:
    data = json.load(f)

def main():
    # Lets use while loop to make sure that the user enter a text;not submit empty
    while True:
        color = input("Enter a color name, hex value, or RGB value: ")
        if color:
            break
        else:
            print("Please enter a valid color name, hex value, or RGB value.")

    check_type(color)

def check_type(color):
    if color.startswith("#"):
        hex_color(color)
    elif color.startswith("(") or color[0].isdigit():
        rgb_color(color)
    else:
        color_name(color)

def hex_color(color):
    color = color.lower()
    if len(color) == 4:
        color = "#" + color[1]*2 + color[2]*2 + color[3]*2  # Convert short hex to full hex
    print("Hex value: ", color)
    
    found = False
    for key, value in data.items():
        if value['hex'] == color or color[:4] == value['hex']:
            print("Color name: ", key)
            print("RGB value: ", value['rgb'])
            show_color(value['rgb'])
            found = True
    
    if not found:
        print("Color in data is not found.")
        show_color(hex_to_rgb(color))
    
    print("\nSimilar Colors:")
    for key, value in data.items():
        if color in value['hex']:
            print(f"Name: {key}, Hex: {value['hex']}, RGB: {value['rgb']}")

def rgb_color(color):
    try:
        if not color.startswith("("):
            color = f"({color})"
        color = color.replace("(", "").replace(")", "").replace(" ", "").split(",")
        rgb = tuple(map(int, color))
        print("RGB value: ", rgb)
        
        found = False
        for key, value in data.items():
            if tuple(value['rgb']) == rgb:
                print("Color name: ", key)
                print("Hex value: ", value['hex'])
                show_color(rgb)
                found = True
        
        if not found:
            print("Color in data is not found.")
            show_color(rgb)
        
        print("\nSimilar Colors:")
        for key, value in data.items():
            if rgb in value['rgb']:
                print(f"Name: {key}, Hex: {value['hex']}, RGB: {value['rgb']}")
    except ValueError:
        print("Invalid RGB value. Please enter valid integers separated by commas.")

def color_name(color):
    color = color.lower()
    found = False
    if color in data:
        print("Hex value: ", data[color]['hex'])
        print("RGB value: ", data[color]['rgb'])
        show_color(data[color]['rgb'])
        found = True
    else:
        print("Color in data is not found.")
    
    print("\nSimilar Colors:")
    for key, value in data.items():
        if color in key:
            print(f"Name: {key}, Hex: {value['hex']}, RGB: {value['rgb']}")
            if not found:
                show_color(value['rgb'])

def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

def show_color(rgb):
    print(f"\033[48;2;{rgb[0]};{rgb[1]};{rgb[2]}m{' ' * 50}\033[0m")
    print(f"\033[48;2;{rgb[0]};{rgb[1]};{rgb[2]}m{' ' * 50}\033[0m")
    print(f"\033[48;2;{rgb[0]};{rgb[1]};{rgb[2]}m{' ' * 50}\033[0m")

if __name__ == '__main__':
    main()
