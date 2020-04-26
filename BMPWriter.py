# BMPWriter  using gray scale rectangular image which has the property of 1 pixel having 1 byte .
"""A module for dealing with BMP image files"""

def write_grayscale(filename, pixels):
    """Creates and writes a grayscale BMP files

    Args:
        filename: The name of the BMP file to be created.
        pxiels: A rectangular image stored as a sequence of rows. Each row is an iterable series of integers in range 0 - 255.
                Each row is a list of pixels from left to right
                Each coloum is a representation of the pixels from top to bottom.
    Raises :
        OSError: If file cannot be written.
        ValueError : If any of the pixel value is out of range.
    """

# =====BMP files are of the form :====
# BITMAPFILEHEADER bmfh;
# BITMAPINFOHEADER bmih;
# RGBQUAD aColors[];
# BYTE aBitmapBits[];


    height = len(pixels)
    width  = len(pixels[0])

    with open(filename,'wb') as bmp:
        # BMP HEADER identified as b'BM'
        bmp.write(b'BM')        # No encoding specified since we're writing raw binary bytes ( MAGIC BYTES SEQUENCE)

        # SIZE OF ThE FILE
        # Next 4 bytes is the size of the file. Since we do not know in advance keep a bookmark, we have the tell method to come back at a later point and write.
        size_bookmark = bmp.tell()  # Returns an integer value , for the cursor position.

        # The size of the BMP file. Littel endian , where the least significant bit is written first
        # For now placeholder values designated as b'\x00\x00\x00\x00' = 4 bytes of 0's
        bmp.write(b'\x00\x00\x00\x00')


        # Unused 4 bytes
        bmp.write(b'\x00\x00')  # Un-used 16-bit integer should be 0
        bmp.write(b'\x00\x00')  # Un-used 16-bit integer should be 0

        #STORE PIXEL CURSOR POINT
        pixel_offset_bookmark = bmp.tell()

        # Writing the PIXEL data offset ( 4 bytes = 32 bits) Keep values as 0 for now.
        bmp.write(b'\x00\x00\x00\x00')

        #IMAGE HEADER
        bmp.write(b'\x28\x00\x00\x00')  #Length of the image as 32 bit int = 40 in decimal == 28 in hexadecimal litte end-ian
        bmp.write(_int32_to_bytes(width))         # Image width in pixels
        bmp.write(_int32_to_bytes(height))        # Image height in pixels

        # Total of below is 40 bytes for gray scale images
        bmp.write(b'\x01\x00')                  # Number of image planes
        bmp.write(b'\x08\x00')                  # Bits per pixel for gray scale is 8

        bmp.write(b'\x00\x00\x00\x00')          # No compression
        bmp.write(b'\x00\x00\x00\x00')          # Zero for uncompressed images
        bmp.write(b'\x00\x00\x00\x00')          # Unused pixels per meter
        bmp.write(b'\x00\x00\x00\x00')          # Unused pixels per meter
        bmp.write(b'\x00\x00\x00\x00')          # Use whole color table
        bmp.write(b'\x00\x00\x00\x00')          # All colors are important

        # COLOR PALETTE
        # Each pixel in 8-bit bmp image is an index into the BGR color table with 256 entries
        # Grayscale requires 256 , 4 byte gray values on linear scale.
        for c in range(256):
            bmp.write(bytes((c,c,c,0)))    # Blue , Green ,Red , zero

        # Pixel data
        pixel_data_bookmark = bmp.tell()
        for row in reversed(pixels):        # BMP are written bottom to top
            row_data = bytes(row)           # Each row must have pixels with 255 , or else ValueError
            bmp.write(row_data)
            padding = b'\x00' * ((4 - (len(row) % 4))% 4) # Irrespective of width the length of each pixel row should be a multiple of 4. Why % 4 again at the end.\
                                                          # Padding for multiples of 4 bytes should be 0. If you take len(row) = 8, then if % 4 is ot used, we get \
                                                          # padding = 4,which is not necessary considering that padding should be done only for len(rows) not multiple of 4

            bmp.write(padding)

        # End of file.
        eof_bookmark = bmp.tell()

        #Length of file to be filled.
        bmp.seek(size_bookmark)
        bmp.write(_int32_to_bytes(eof_bookmark))

        # Fill in the pixel offset placeholder.
        bmp.seek(pixel_offset_bookmark)
        bmp.write(_int32_to_bytes(pixel_data_bookmark))





def _int32_to_bytes(number):
    """Convert an integer to it's binary equivalent"""
    return bytes((number & 0xff ,number >> 8 & 0xff, number >> 16 & 0xff , number >> 24 & 0xff))







write_grayscale('Gray.bmp',[[i,i,i,i] for i in range(0,256)])
