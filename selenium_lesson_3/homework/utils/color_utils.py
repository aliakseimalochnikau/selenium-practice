class ColorUtils:
    def rgba_to_hex(rgba_color: str) -> str:
        rgba_str = rgba_color.strip("rgba()").replace(" ", "").split(",")
        rgba_values = [int(color) for color in rgba_str]
        hex_color = "#{:02X}{:02X}{:02X}".format(*rgba_values[:3])
        return hex_color.lower()
