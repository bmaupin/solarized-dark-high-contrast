#!/usr/bin/env python

import sys

if sys.version_info < (3, 4):
    sys.exit('ERROR: Requires Python 3.4')

from enum import Enum

def main():
    Cases = Enum('Cases', 'lower upper')
    infile_case = None
    
    if len(sys.argv) < 2:
        sys.stderr.write('ERROR: Must provide a file to modify\n')
        sys.exit('Usage: {} FILE'.format(sys.argv[0]))
    
    # Keep these in lists instead of a dict to preserve ordering so we don't 
    # overwrite our replacements
    color_codes_hex_dark = [
            'eee8d5',
            '93a1a1',
            '839496',
            '657b83',
            '586e75',
    ]
    color_codes_hex_dark_high_contrast = [
            'fdf6e3',
            'eee8d5',
            '93a1a1',
            '839496',
            '657b83',
    ]
    ''' These binary color codes are used by Eclipse preference files. I 
    generated them like this, since I wanted to actually have the codes 
    explicitly listed instead of generated on the fly for easier debugging:
    
    for code in color_codes_hex_dark:
        print "'{},{},{}',".format(int(code[0:2], 16), int(code[2:4], 16), int(code[4:6], 16))
    '''
    color_codes_bin_dark = [
        '238,232,213',
        '147,161,161',
        '131,148,150',
        '101,123,131',
        '88,110,117',
    ]
    color_codes_bin_dark_high_contrast = [
        '253,246,227',
        '238,232,213',
        '147,161,161',
        '131,148,150',
        '101,123,131',
    ]
    
    with open(sys.argv[1], 'r') as infile:
        outfile_data = infile.read()
    
    # Figure out whether the input is using upper or lower case color codes
    for color_code in color_codes_hex_dark:
        # Skip color codes that don't contain letters
        if color_code.lower() == color_code.upper():
            continue
        if outfile_data.find(color_code.lower()) != -1:
            infile_case = Cases.lower
            # Use the first one we find as the decisive case
            break
        elif outfile_data.find(color_code.upper()) != -1:
            infile_case = Cases.upper
            break
    
    for i in range(len(color_codes_hex_dark)):
        if infile_case == Cases.lower:
            outfile_data = outfile_data.replace(color_codes_hex_dark[i].lower(), color_codes_hex_dark_high_contrast[i].lower())
            outfile_data = outfile_data.replace(color_codes_hex_dark[i].upper(), color_codes_hex_dark_high_contrast[i].lower())
        elif infile_case == Cases.upper:
            outfile_data = outfile_data.replace(color_codes_hex_dark[i].lower(), color_codes_hex_dark_high_contrast[i].upper())
            outfile_data = outfile_data.replace(color_codes_hex_dark[i].upper(), color_codes_hex_dark_high_contrast[i].upper())
    
    for i in range(len(color_codes_bin_dark)):
        outfile_data = outfile_data.replace(color_codes_bin_dark[i], color_codes_bin_dark_high_contrast[i])
    
    with open('{}-high-contrast.{}'.format(*sys.argv[1].rsplit('.', 1)), 'w') as outfile:
        outfile.write(outfile_data)


if __name__ == '__main__':
    main()