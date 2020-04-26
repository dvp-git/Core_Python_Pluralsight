# BMP File Reader
def dimensions(filename):
    """Determine the dimensions in pixels of the image width and height of the BMP image

    Args:
        filename: The name of the BMP file.

    Returns:
        A tuple containing the width and height of the image in pixels.

    Raises:
        ValueError: if the file is not a BMP.
        OSError: if there was a problem in reading the file.
    """

    with open(filename,'rb') as f:
        magic = f.read(2)
        if magic != b'BM':
            raise ValueError(f"{f} is not a BMP file")

        # Move cursor to position after 18 bytes, since this is the point where width and height is defined in the BMP.
        f.seek(18)
        width_bytes = f.read(4) # Read the 4 bytes representing the width.(in bytes)
        height_bytes = f.read(4) # Read the 4 bytes representing the height.(in bytes)

        return (_bytes_to_int32(width_bytes),_bytes_to_int32(height_bytes))


def _bytes_to_int32(byte_num):
    """ Returns the int representation of the bytes"""
    return (byte_num[0] | (byte_num[1])<< 8 | (byte_num[2])<< 16 | (byte_num[3])<< 23)


"""Output:
>>> BMPDimensionRead.dimensions("mandelbrot.bmp")
(448, 256)
>>>
>>> BMPDimensionRead.dimensions("Gray.bmp")
(4, 256)
"""
