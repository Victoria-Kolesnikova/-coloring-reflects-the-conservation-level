from pymol import cmd

# Conservativeness coding color gradient
color = {
    1: [0, 0, 0], 2: [5, 0, 0], 3: [10, 0, 0], 4: [15, 0, 0], 5: [20, 0, 0],
    6: [25, 0, 0], 7: [30, 0, 0], 8: [35, 0, 0], 9: [40, 0, 0], 10: [45, 0, 0],
    11: [50, 0, 0], 12: [55, 0, 0], 13: [60, 0, 0], 14: [65, 0, 0], 15: [70, 0, 0],
    16: [75, 0, 0], 17: [80, 0, 0], 18: [85, 0, 0], 19: [90, 0, 0], 20: [95, 0, 0],
    21: [100, 0, 0], 22: [105, 0, 0], 23: [110, 0, 0], 24: [115, 0, 0], 25: [120, 0, 0],
    26: [125, 0, 0], 27: [130, 0, 0], 28: [135, 0, 0], 29: [140, 0, 0], 30: [145, 0, 0],
    31: [150, 0, 0], 32: [155, 0, 0], 33: [160, 0, 0], 34: [165, 0, 0], 35: [170, 0, 0],
    36: [175, 0, 0], 37: [180, 0, 0], 38: [185, 0, 0], 39: [190, 0, 0], 40: [195, 0, 0],
    41: [200, 0, 0], 42: [205, 0, 0], 43: [210, 0, 0], 44: [215, 0, 0], 45: [220, 0, 0],
    46: [225, 0, 0], 47: [230, 0, 0], 48: [235, 0, 0], 49: [240, 0, 0], 50: [240, 0, 0],
    51: [241, 0, 0], 52: [243, 10, 10], 53: [245, 20, 20],54:[247, 30, 30],55:[249, 40, 40],    
    56: [251, 51, 51], 57: [253, 61, 61], 58: [255, 71, 71],59:[255, 81, 81],60:[255, 92, 92],    
    61: [255, 102, 102], 62: [255, 112, 112], 63: [255, 122, 122], 64: [255, 133, 133], 
    65: [255, 143, 143], 66: [255, 153, 153], 67: [255, 163, 163], 68: [255, 173, 173],  
    69: [255, 184, 184],  70: [255, 194, 194], 71: [255, 204, 204], 72: [255, 214, 214],  
    73: [255, 224, 224],  74: [255, 235, 235], 75: [255, 255, 255], 75: [255, 255, 255],  
    76: [247, 251, 255],  77: [239, 247, 255], 78: [231, 243, 255], 79: [223, 239, 255],  
    80: [215, 235, 255],  81: [207, 231, 255], 82: [199, 227, 255], 83: [191, 223, 255],  
    84: [183, 219, 255],  85: [175, 215, 255], 86: [167, 211, 255], 87: [159, 207, 255],  
    88: [151, 203, 255],  89: [143, 199, 255], 90: [135, 195, 255], 91: [127, 191, 255],  
    92: [119, 187, 255],  93: [111, 183, 255], 94: [103, 179, 255], 95: [95, 175, 255],  
    96: [87, 171, 255],   97: [79, 170, 255],  98: [72, 170, 255],  99: [66, 170, 255],  
    100: [0, 0, 255]
}

with open("perc.txt", "r") as file:
    lines = file.readlines()

# Applying colors to CA-atoms
for i, line in enumerate(lines):
    try:
        # Removing extra spaces and newline characters
        value_str = line.strip()
        if not value_str:  #Skip the empty lines
            print(f"Skip the empty lines {i+1}.")
            continue

        value = int(value_str)  # Converting a string to a number
        if value in color:  # Checking that the value is in the color scale
            color_rgb = color[value]  # Getting the RGB code from the scale
            color_name = f"color_{value}"  # A unique name for a color

            # Creating a color in PyMOL using RGB code
            cmd.set_color(color_name, color_rgb)

            # Apply the color to the CA-atom
            cmd.color(color_name, f"resi {i+1} and name CA")
        else:
            print(f"The value in row {i+1} is outside the acceptable range (1-100).")
           
    except ValueError:
        print(f"Error in the line {i+1}: '{line.strip()}' It is not a number.")
        # We color the atom yellow in case of an error
        cmd.color("yellow", f"resi {i+1} and name CA")