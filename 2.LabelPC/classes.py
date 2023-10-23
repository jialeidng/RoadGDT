from dataclasses import dataclass


@dataclass
class ImageData:
    point : int
    img_name: str
    seg_name: str
    coord_2D: list
    RGB: list

@dataclass
class PointInfo:
    point: int
    coord_3D: list
    asset_type: str
    color: list
    ImageData_list: list


