from dataclasses import dataclass

@dataclass

class cam_inf:
    image_ID: int
    image_name: str  # image name
    translation: list  # Tx, Ty, Tz
    rotation: list  # Qw, Qx, Qy, Qz
    coords: list  # qx, qy, qz

class get_pixel_info:
    x_coord: int
    y_coord: int
    rgb: list  # R, G, B


