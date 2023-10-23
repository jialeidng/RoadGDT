from dataclasses import dataclass

@dataclass

class cam_inf:
    image_ID: int
    image_name: str  # image name
    translation: list  # Tx, Ty, Tz
    rotation: list  # Qw, Qx, Qy, Qz
    coords: list  # qx, qy, qz
