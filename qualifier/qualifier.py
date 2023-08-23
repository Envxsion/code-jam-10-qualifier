import PIL
from PIL import Image

def valid_input(image_size: tuple[int, int], tile_size: tuple[int, int], ordering: list[int]) -> bool:
    """
    Return True if the given input allows the rearrangement of the image, False otherwise.

    The tile size must divide each image dimension without remainders, and `ordering` must use each input tile exactly
    once.
    """
    div = tuple(e1/e2 for e1, e2 in zip(image_size, tile_size))
    if all(isinstance(v, int) for v in div):
        if len(ordering) == len(set(ordering)):
            if all(0 <= i < len(ordering) for i in ordering):
                return True


def rearrange_tiles(image_path: str, tile_size: tuple[int, int], ordering: list[int], out_path: str) -> None:
    """
    Rearrange the image.

    The image is given in `image_path`. Split it into tiles of size `tile_size`, and rearrange them by `ordering`.
    The new image needs to be saved under `out_path`.

    The tile size must divide each image dimension without remainders, and `ordering` must use each input tile exactly
    once. If these conditions do not hold, raise a ValueError with the message:
    "The tile size or ordering are not valid for the given image".
    """
    #load image and split it into tiles depending on length of ordering, give each tile a number from 0 to len(ordering)
    image = Image.open(image_path)
    tiles = []
    for i in range(len(ordering)):
        
        
         
    

rearrange_tiles("images/pydis_logo_scrambled.png", (256, 256), "images/pydis_logo_order.txt",
                     "images/pydis_logyayo_unscrambled.png")