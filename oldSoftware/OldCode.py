       #In pixel image
        # sizes = self.size(image)
        #Old code for creating a 2d array of pixels that get pixel to ansci code from an image
        # ansi_codes = []
        # for x in range(sizes[1]):
        #     row = []
        #     for y in range(sizes[0]):
        #         r, g, b = image.getpixel((y, x))
        #         if (r,g,b) in pixel_to_ansicode:
        #             row.append(pixel_to_ansicode[(r,g,b)] + ' ')
        #             if scaleRatio:
        #                 row.append(pixel_to_ansicode[(r,g,b)] + ' ')
        #         else:
        #             row.append(self.rgb_to_anscii(*(r,g,b)) + ' ')
        #             if scaleRatio:
        #                 row.append(self.rgb_to_anscii(*(r,g,b)) + ' ')
        #     ansi_codes.append(row)