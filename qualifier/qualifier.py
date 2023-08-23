from PIL import Image

def valid_input(image_size: tuple[int, int], tile_size: tuple[int, int], ordering: list[int]) -> bool:
    """
    Return True if the given input allows the rearrangement of the image, False otherwise.

    The tile size must divide each image dimension without remainders, and `ordering` must use each input tile exactly
    once.
    """
    div = tuple(e1 // e2 for e1, e2 in zip(image_size, tile_size))
    if all(isinstance(v, int) for v in div):
        if len(ordering) == len(set(ordering)) == div[0] * div[1]:
            if all(0 <= i < len(ordering) for i in ordering):
                return True
    return False


def rearrange_tiles(image_path: str, tile_size: tuple[int, int], ordering: list[int], out_path: str) -> None:
    """
    Rearrange the image.

    The image is given in `image_path`. Split it into tiles of size `tile_size`, and rearrange them by `ordering`.
    The new image needs to be saved under `out_path`.

    The tile size must divide each image dimension without remainders, and `ordering` must use each input tile exactly
    once. If these conditions do not hold, raise a ValueError with the message:
    "The tile size or ordering are not valid for the given image".
    """
    image = Image.open(image_path)
    if not valid_input(image.size, tile_size, ordering):
        raise ValueError("The tile size or ordering are not valid for the given image")

    
    image_width, image_height = image.size
    tile_width, tile_height = tile_size

    new_image = Image.new(image.mode, image.size)
    for new_index, old_index in enumerate(ordering):
        row, col = divmod(old_index, image_width // tile_width)
        left = col * tile_width
        upper = row * tile_height
        right = left + tile_width
        lower = upper + tile_height

        tile = image.crop((left, upper, right, lower))
        new_row, new_col = divmod(new_index, image_width // tile_width)  #Calc new row and column
        new_image.paste(tile, (new_col * tile_width, new_row * tile_height)) 

    new_image.save(out_path)
    return None


#with open('images/pydis_logo_order.txt', 'r') as f:
#    ordering = [int(line.strip()) for line in f.readlines()]
#
#rearrange_tiles("images/pydis_logo_scrambled.png", (256, 256), ordering, "images/output.png")
