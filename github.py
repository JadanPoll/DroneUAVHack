import math
def build_huffman_table_luminance_dc():
    # Luminance DC Value to Huffman Code mapping as given in Table K.3
    huffman_table = {
        0: '00',
        1: '010',
        2: '011',
        3: '100',
        4: '101',
        5: '110',
        6: '1110',
        7: '11110',
        8: '111110',
        9: '1111110',
        10: '11111110',
        11: '111111110',
    }

    # Count the number of codes of each length
    lengths_count = [0] * 16
    huffman_values = []

    for value, code in huffman_table.items():
        code_length = len(code)
        lengths_count[code_length - 1] += 1
        huffman_values.append(value)

    # Huffman Table Header for Luminance DC
    huffman_header = bytearray([0xFF, 0xC4, 0x00, 0x1F, 0x00])

    # Append lengths count to header
    huffman_header.extend(lengths_count)

    # Append Huffman values to header
    huffman_header.extend(huffman_values)

    return huffman_header


def build_huffman_table_chrominance_dc():
    # Chrominance DC Value to Huffman Code mapping as given in Table K.4
    huffman_table = {
        0: '00',
        1: '01',
        2: '10',
        3: '110',
        4: '1110',
        5: '11110',
        6: '111110',
        7: '1111110',
        8: '11111110',
        9: '111111110',
        10: '1111111110',
        11: '11111111110',
    }

    # Count the number of codes of each length
    lengths_count = [0] * 16
    huffman_values = []

    for value, code in huffman_table.items():
        code_length = len(code)
        lengths_count[code_length - 1] += 1
        huffman_values.append(value)

    # Huffman Table Header for Chrominance DC
    huffman_header = bytearray([0xFF, 0xC4, 0x00, 0x1F, 0x01])

    # Append lengths count to header
    huffman_header.extend(lengths_count)

    # Append Huffman values to header
    huffman_header.extend(huffman_values)

    return huffman_header


def build_huffman_table_ac():
    # AC Value to Huffman Code mapping as given
    huffman_table = {
        (0, 0): '1010',
        (0, 1): '00',
        (0, 2): '01',
        (0, 3): '100',
        (0, 4): '1011',
        (0, 5): '11010',
        (0, 6): '1111000',
        (0, 7): '11111000',
        (0, 8): '1111110110',
        (0, 9): '1111111110000010',
        (0, 10): '1111111110000011',
        (1, 1): '1100',
        (1, 2): '11011',
        (1, 3): '1111001',
        (1, 4): '111110110',
        (1, 5): '11111110110',
        (1, 6): '1111111110000100',
        (1, 7): '1111111110000101',
        (1, 8): '1111111110000110',
        (1, 9): '1111111110000111',
        (1, 10): '1111111110001000',
        (2, 1): '11100',
        (2, 2): '11111001',
        (2, 3): '1111110111',
        (2, 4): '111111110100',
        (2, 5): '1111111110001001',
        (2, 6): '1111111110001010',
        (2, 7): '1111111110001011',
        (2, 8): '1111111110001100',
        (2, 9): '1111111110001101',
        (2, 10): '1111111110001110',
        (3, 1): '111010',
        (3, 2): '111110111',
        (3, 3): '111111110101',
        (3, 4): '1111111110001111',
        (3, 5): '1111111110010000',
        (3, 6): '1111111110010001',
        (3, 7): '1111111110010010',
        (3, 8): '1111111110010011',
        (3, 9): '1111111110010100',
        (3, 10): '1111111110010101',
        (4, 1): '111011',
        (4, 2): '1111111000',
        (4, 3): '1111111110010110',
        (4, 4): '1111111110010111',
        (4, 5): '1111111110011000',
        (4, 6): '1111111110011001',
        (4, 7): '1111111110011010',
        (4, 8): '1111111110011011',
        (4, 9): '1111111110011100',
        (4, 10): '1111111110011101',
        (5, 1): '1111010',
        (5, 2): '11111110111',
        (5, 3): '1111111110011110',
        (5, 4): '1111111110011111',
        (5, 5): '1111111110100000',
        (5, 6): '1111111110100001',
        (5, 7): '1111111110100010',
        (5, 8): '1111111110100011',
        (5, 9): '1111111110100100',
        (5, 10): '1111111110100101',
        (6, 1): '1111011',
        (6, 2): '111111110110',
        (6, 3): '1111111110100110',
        (6, 4): '1111111110100111',
        (6, 5): '1111111110101000',
        (6, 6): '1111111110101001',
        (6, 7): '1111111110101010',
        (6, 8): '1111111110101011',
        (6, 9): '1111111110101100',
        (6, 10): '1111111110101101',
        (7, 1): '11111010',
        (7, 2): '111111110111',
        (7, 3): '1111111110101110',
        (7, 4): '1111111110101111',
        (7, 5): '1111111110110000',
        (7, 6): '1111111110110001',
        (7, 7): '1111111110110010',
        (7, 8): '1111111110110011',
        (7, 9): '1111111110110100',
        (7, 10): '1111111110110101',
        (8, 1): '111111000',
        (8, 2): '111111111000000',
        (8, 3): '1111111110110110',
        (8, 4): '1111111110110111',
        (8, 5): '1111111110111000',
        (8, 6): '1111111110111001',
        (8, 7): '1111111110111010',
        (8, 8): '1111111110111011',
        (8, 9): '1111111110111100',
        (8, 10): '1111111110111101',
        (9, 1): '111111001',
        (9, 2): '1111111110111110',
        (9, 3): '1111111110111111',
        (9, 4): '1111111111000000',
        (9, 5): '1111111111000001',
        (9, 6): '1111111111000010',
        (9, 7): '1111111111000011',
        (9, 8): '1111111111000100',
        (9, 9): '1111111111000101',
        (9, 10): '1111111111000110',
        (10, 1): '111111010',
        (10, 2): '1111111111000111',
        (10, 3): '1111111111001000',
        (10, 4): '1111111111001001',
        (10, 5): '1111111111001010',
        (10, 6): '1111111111001011',
        (10, 7): '1111111111001100',
        (10, 8): '1111111111001101',
        (10, 9): '1111111111001110',
        (10, 10): '1111111111001111',
        (11, 1): '1111111001',
        (11, 2): '1111111111010000',
        (11, 3): '1111111111010001',
        (11, 4): '1111111111010010',
        (11, 5): '1111111111010011',
        (11, 6): '1111111111010100',
        (11, 7): '1111111111010101',
        (11, 8): '1111111111010110',
        (11, 9): '1111111111010111',
        (11, 10): '1111111111011000',
        (12, 1): '1111111010',
        (12, 2): '1111111111011001',
        (12, 3): '1111111111011010',
        (12, 4): '1111111111011011',
        (12, 5): '1111111111011100',
        (12, 6): '1111111111011101',
        (12, 7): '1111111111011110',
        (12, 8): '1111111111011111',
        (12, 9): '1111111111100000',
        (12, 10): '1111111111100001',
        (13, 1): '11111111000',
        (13, 2): '1111111111100010',
        (13, 3): '1111111111100011',
        (13, 4): '1111111111100100',
        (13, 5): '1111111111100101',
        (13, 6): '1111111111100110',
        (13, 7): '1111111111100111',
        (13, 8): '1111111111101000',
        (13, 9): '1111111111101001',
        (13, 10): '1111111111101010',
        (14, 1): '1111111111101011',
        (14, 2): '1111111111101100',
        (14, 3): '1111111111101101',
        (14, 4): '1111111111101110',
        (14, 5): '1111111111101111',
        (14, 6): '1111111111110000',
        (14, 7): '1111111111110001',
        (14, 8): '1111111111110010',
        (14, 9): '1111111111110011',
        (14, 10): '1111111111110100',
        (15, 1): '1111111111110101',
        (15, 2): '1111111111110110',
        (15, 3): '1111111111110111',
        (15, 4): '1111111111111000',
        (15, 5): '1111111111111001',
        (15, 6): '1111111111111010',
        (15, 7): '1111111111111011',
        (15, 8): '1111111111111100',
        (15, 9): '1111111111111101',
        (15, 10): '1111111111111110',
        (15, 0): '11111111001',
    }






    # Count the number of codes of each length
    lengths_count = [0] * 16
    huffman_values = []

    for key, code in huffman_table.items():
        code_length = len(code)
        lengths_count[code_length - 1] += 1
        # Convert the (run, size) tuple to a single value (hex representation)
        huffman_values.append(((key[0] << 4) + key[1], code))

    # Sort the Huffman values by the length of the code
    huffman_values.sort(key=lambda x: len(x[1]))

    # Huffman Table Header
    huffman_header = bytearray([0xFF, 0xC4, 0x00, 0xB5, 0x10])
    # Append lengths count to header
    huffman_header.extend(lengths_count)

    # Append Huffman values to header
    for value in huffman_values:
        huffman_header.append(value[0])





    return huffman_header



def build_huffman_table_ac_chrom():






    ac_huffman_chrominance_table = {
        (0, 0): '00',  # EOB
        (0, 1): '01',
        (0, 2): '100',
        (0, 3): '1010',
        (0, 4): '11000',
        (0, 5): '11001',
        (0, 6): '111000',
        (0, 7): '1111000',
        (0, 8): '111110100',
        (0, 9): '1111110110',
        (0, 10): '111111110100',
        (1, 1): '1011',
        (1, 2): '111001',
        (1, 3): '11110110',
        (1, 4): '111110101',
        (1, 5): '11111110110',
        (1, 6): '111111110101',
        (1, 7): '1111111110001000',
        (1, 8): '1111111110001001',
        (1, 9): '1111111110001010',
        (1, 10): '1111111110001011',
        (2, 1): '11010',
        (2, 2): '11110111',
        (2, 3): '1111110111',
        (2, 4): '111111110110',
        (2, 5): '111111111000010',
        (2, 6): '1111111110001100',
        (2, 7): '1111111110001101',
        (2, 8): '1111111110001110',
        (2, 9): '1111111110001111',
        (2, 10): '1111111110010000',
        (3, 1): '11011',
        (3, 2): '11111000',
        (3, 3): '1111111000',
        (3, 4): '111111110111',
        (3, 5): '1111111110010001',
        (3, 6): '1111111110010010',
        (3, 7): '1111111110010011',
        (3, 8): '1111111110010100',
        (3, 9): '1111111110010101',
        (3, 10): '1111111110010110',
        (4, 1): '111010',
        (4, 2): '111110110',
        (4, 3): '1111111110010111',
        (4, 4): '1111111110011000',
        (4, 5): '1111111110011001',
        (4, 6): '1111111110011010',
        (4, 7): '1111111110011011',
        (4, 8): '1111111110011100',
        (4, 9): '1111111110011101',
        (4, 10): '1111111110011110',
        (5, 1): '111011',
        (5, 2): '1111111001',
        (5, 3): '1111111110011111',
        (5, 4): '1111111110100000',
        (5, 5): '1111111110100001',
        (5, 6): '1111111110100010',
        (5, 7): '1111111110100011',
        (5, 8): '1111111110100100',
        (5, 9): '1111111110100101',
        (5, 10): '1111111110100110',
        (6, 1): '1111001',
        (6, 2): '11111110111',
        (6, 3): '1111111110100111',
        (6, 4): '1111111110101000',
        (6, 5): '1111111110101001',
        (6, 6): '1111111110101010',
        (6, 7): '1111111110101011',
        (6, 8): '1111111110101100',
        (6, 9): '1111111110101101',
        (6, 10): '1111111110101110',
        (7, 1): '1111010',
        (7, 2): '11111111000',
        (7, 3): '1111111110101111',
        (7, 4): '1111111110110000',
        (7, 5): '1111111110110001',
        (7, 6): '1111111110110010',
        (7, 7): '1111111110110011',
        (7, 8): '1111111110110100',
        (7, 9): '1111111110110101',
        (7, 10): '1111111110110110',
        (8, 1): '11111001',
        (8, 2): '1111111110110111',
        (8, 3): '1111111110111000',
        (8, 4): '1111111110111001',
        (8, 5): '1111111110111010',
        (8, 6): '1111111110111011',
        (8, 7): '1111111110111100',
        (8, 8): '1111111110111101',
        (8, 9): '1111111110111110',
        (8, 10): '1111111110111111',
        (9, 1): '111110111',
        (9, 2): '1111111111000000',
        (9, 3): '1111111111000001',
        (9, 4): '1111111111000010',
        (9, 5): '1111111111000011',
        (9, 6): '1111111111000100',
        (9, 7): '1111111111000101',
        (9, 8): '1111111111000110',
        (9, 9): '1111111111000111',
        (9, 10): '1111111111001000',
        (10, 1): '111111000',
        (10, 2): '1111111111001001',
        (10, 3): '1111111111001010',
        (10, 4): '1111111111001011',
        (10, 5): '1111111111001100',
        (10, 6): '1111111111001101',
        (10, 7): '1111111111001110',
        (10, 8): '1111111111001111',
        (10, 9): '1111111111010000',
        (10, 10): '1111111111010001',
        (11, 1): '111111001',
        (11, 2): '1111111111010010',
        (11, 3): '1111111111010011',
        (11, 4): '1111111111010100',
        (11, 5): '1111111111010101',
        (11, 6): '1111111111010110',
        (11, 7): '1111111111010111',
        (11, 8): '1111111111011000',
        (11, 9): '1111111111011001',
        (11, 10): '1111111111011010',
        (12, 1): '111111010',
        (12, 2): '1111111111011011',
        (12, 3): '1111111111011100',
        (12, 4): '1111111111011101',
        (12, 5): '1111111111011110',
        (12, 6): '1111111111011111',
        (12, 7): '1111111111100000',
        (12, 8): '1111111111100001',
        (12, 9): '1111111111100010',
        (12, 10): '1111111111100011',
        (13, 1): '11111111001',
        (13, 2): '1111111111100100',
        (13, 3): '1111111111100101',
        (13, 4): '1111111111100110',
        (13, 5): '1111111111100111',
        (13, 6): '1111111111101000',
        (13, 7): '1111111111101001',
        (13, 8): '1111111111101010',
        (13, 9): '1111111111101011',
        (13, 10): '1111111111101100',
        (14, 1): '11111111100000',
        (14, 2): '1111111111101101',
        (14, 3): '1111111111101110',
        (14, 4): '1111111111101111',
        (14, 5): '1111111111110000',
        (14, 6): '1111111111110001',
        (14, 7): '1111111111110010',
        (14, 8): '1111111111110011',
        (14, 9): '1111111111110100',
        (14, 10): '1111111111110101',
        (15, 0): '1111111010',  # ZRL
        (15, 1): '111111111000011',
        (15, 2): '1111111111110110',
        (15, 3): '1111111111110111',
        (15, 4): '1111111111111000',
        (15, 5): '1111111111111001',
        (15, 6): '1111111111111010',
        (15, 7): '1111111111111011',
        (15, 8): '1111111111111100',
        (15, 9): '1111111111111101',
        (15, 10): '1111111111111110',
    }


        # Count the number of codes of each length
        
    lengths_count = [0] * 16
    huffman_values = []

    for key, code in ac_huffman_chrominance_table.items():
        code_length = len(code)
        lengths_count[code_length - 1] += 1
        # Convert the (run, size) tuple to a single value (hex representation)
        huffman_values.append(((key[0] << 4) + key[1], code))

    # Sort the Huffman values by the length of the code
    huffman_values.sort(key=lambda x: len(x[1]))

    # Huffman Table Header
    huffman_header = bytearray([0xFF, 0xC4, 0x00, 0xB5, 0x11])
    # Append lengths count to header
    huffman_header.extend(lengths_count)

    # Append Huffman values to header
    for value in huffman_values:
        huffman_header.append(value[0])

    return huffman_header






def build_sof_segment(width, height, num_components, quantization_table_selectors, sampling_factors, precision=8):
    # SOF Header
    sof_header = bytearray([0xFF, 0xC0])

    # Length (high byte, low byte)
    length = 8 + 3 * num_components
    sof_header.extend((length >> 8).to_bytes(1, byteorder='big'))
    sof_header.extend((length & 0xFF).to_bytes(1, byteorder='big'))

    # Precision
    sof_header.append(precision)

    # Image Dimensions
    sof_header.extend((height >> 8).to_bytes(1, byteorder='big'))
    sof_header.extend((height & 0xFF).to_bytes(1, byteorder='big'))
    sof_header.extend((width >> 8).to_bytes(1, byteorder='big'))
    sof_header.extend((width & 0xFF).to_bytes(1, byteorder='big'))

    # Number of Components
    sof_header.append(num_components)

    # Component Parameters
    for i in range(num_components):
        component_id = i + 1
        quantization_selector = quantization_table_selectors[i]
        horizontal_factor, vertical_factor = sampling_factors[i]

        sof_header.append(component_id)  # Component ID
        sof_header.append((horizontal_factor << 4) | vertical_factor)  # Sampling factors
        sof_header.append(quantization_selector)  # Quantization table selector

    return sof_header



def build_sos_segment(num_components, huffman_table_selectors):
    # SOS Header
    sos_header = bytearray([0xFF, 0xDA])

    # Length (high byte, low byte)
    length = 6 + 2 * num_components
    sos_header.extend((length >> 8).to_bytes(1, byteorder='big'))
    sos_header.extend((length & 0xFF).to_bytes(1, byteorder='big'))

    # Number of Components
    sos_header.append(num_components)

    # Component Parameters
    for i in range(num_components):
        component_id = i + 1
        dc_selector, ac_selector = huffman_table_selectors[i]

        sos_header.append(component_id)  # Component ID
        sos_header.append((dc_selector << 4) | ac_selector)  # Huffman table selectors

    # Start of spectral selection (first DCT coefficient)
    sos_header.append(0x00)

    # End of spectral selection (last DCT coefficient)
    sos_header.append(0x3F)

    # Successive approximation bit position (high, low)
    sos_header.append(0x00)


    return sos_header


# Function to build the default quantization table
def build_default_quantization_table():
    # Standard quantization table from the JPEG standard (Luminance table)
    luminance_quant_table = [
        16, 11, 10, 16, 24, 40, 51, 61,
        12, 12, 14, 19, 26, 58, 60, 55,
        14, 13, 16, 24, 40, 57, 69, 56,
        14, 17, 22, 29, 51, 87, 80, 62,
        18, 22, 37, 56, 68, 109, 103, 77,
        24, 35, 55, 64, 81, 104, 113, 92,
        49, 64, 78, 87, 103, 121, 120, 101,
        72, 92, 95, 98, 112, 100, 103, 99
    ]

    # Standard quantization table from the JPEG standard (Chrominance table)
    chrominance_quant_table = [
        17, 18, 24, 47, 99, 99, 99, 99,
        18, 21, 26, 66, 99, 99, 99, 99,
        24, 26, 56, 99, 99, 99, 99, 99,
        47, 66, 99, 99, 99, 99, 99, 99,
        99, 99, 99, 99, 99, 99, 99, 99,
        99, 99, 99, 99, 99, 99, 99, 99,
        99, 99, 99, 99, 99, 99, 99, 99,
        99, 99, 99, 99, 99, 99, 99, 99
    ]

    # Create quantization table header
    qt_header = bytearray()

    # Add luminance table
    qt_header.extend([0xFF, 0xDB, 0x00, 0x43, 0x00])  # DQT marker, length (67 bytes), and table ID
    qt_header.extend(luminance_quant_table)

    # Add chrominance table
    qt_header.extend([0xFF, 0xDB, 0x00, 0x43, 0x01])  # DQT marker, length (67 bytes), and table ID
    qt_header.extend(chrominance_quant_table)
    
    return qt_header

import os
import tkinter as tk
from tkinter import filedialog
import json
select=1





class YourClass:
    def __init__(self):
        self.salmon = b""  # Initialize salmon as empty bytes
        self.payload_raw_list = []  # Initialize payload_raw_list

    def select_file_and_collate_bytes(self):
        root = tk.Tk()
        #root.withdraw()  # Hide the root window

        # Open the file dialog
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])

        # Collate bytes if file selected
        if file_path:
            self.collate_bytes_from_json(file_path)

    def collate_bytes_from_json(self, file_path):
        if not file_path:
            return

        # Open and read the file
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Extract payload raw values
        self.payload_raw_list = [
            (item['_source']['layers']['udp']['udp.payload'].replace(':', "")[0x40:0x42], 
             item['_source']['layers']['udp']['udp.payload'].replace(':', '')[(0x60 - 0x2A + 2) * 2:])
            for item in data
            if '_source' in item and 'layers' in item['_source'] and 'udp' in item['_source']['layers'] and
            'udp.payload' in item['_source']['layers']['udp'] and 
            item['_source']['layers']['udp']['udp.payload'].replace(':', "")[0x00:0x04] == "9301"
        ]


        print("Done 1")

        # Convert hexadecimal strings to bytes and collate
        self.salmon = b''.join(self.hex_string_to_bytes(payload) for _, payload in self.payload_raw_list)

        print("Done 2")

    def hex_string_to_bytes(self, hex_string):
        return bytes.fromhex(hex_string)
    
    def get_collated_bytes(self):
        collated_bytes = []
        current_bytes = bytearray()

        for marker, payload in self.payload_raw_list:
            if marker == "00":
                if current_bytes:
                    collated_bytes.append(current_bytes)

                current_bytes = bytearray()

            current_bytes.extend(self.hex_string_to_bytes(payload))

        if current_bytes:
            collated_bytes.append(current_bytes)

        return collated_bytes if collated_bytes else None

    def save_collated_bytes_to_file(self, json_file_path):
        default_save_path = os.path.join(os.getcwd(), "collated_bytes2.txt")

        # Write collated bytes to file with sections based on packet number
        with open(default_save_path, 'w') as file:
            for index, (marker, payload) in enumerate(self.payload_raw_list, start=1):
                hex_string = self.hex_string_to_bytes(payload).hex()
                file.write(f"Packet {index}, Marker {marker}:\n{hex_string}\n\n")
        
        print("Wrote!")


def save_image_as_jpeg(image_bytes, output_filename):
    # Print the byte array as hexadecimal string
    #print("JPEG Image:", image_bytes.hex())

    # Save the byte array as a JPEG file
    with open(output_filename, 'wb') as jpeg_file:
        jpeg_file.write(image_bytes)

from moviepy.editor import ImageSequenceClip

def save_image_as_jpeg(image_bytes, filename):
    with open(filename, 'wb') as f:
        f.write(image_bytes)

# Function to create a video from an array of JPEG images
def create_video_from_images(image_bytes_array, output_video_filename, fps=24):
    # Save each JPEG image in the array to a file
    image_filenames = []
    for i, image_bytes in enumerate(image_bytes_array):
        filename = f'image_{i}.jpg'
        save_image_as_jpeg(image_bytes, filename)
        image_filenames.append(filename)
    
    # Create a video clip from the saved images
    clip = ImageSequenceClip(image_filenames, fps=fps)
    clip.write_videofile(output_video_filename, codec='libx264')




import cv2
from threading import Thread, Lock
import numpy as np
import time
import mediapipe as mp


class AsyncVideoStreamer:
    def __init__(self):
        self.queue = []
        self.lock = Lock()
        self.running = True

    def start_stream(self):
        stream_thread = Thread(target=self.stream_images_as_video)
        stream_thread.start()

    def feed_frame(self, jpeg_data):
        with self.lock:
            self.queue.append(jpeg_data)

    def stop(self):
        self.running = False




    def stream_images_as_video(self, use_yolov7=False, use_mediapipe=False, use_canny=False):
        cv2.namedWindow('Video Stream', cv2.WINDOW_NORMAL)

        while self.running or len(self.queue) > 0:
            if self.queue:
                with self.lock:
                    jpeg_data = self.queue.pop(0)
                time.sleep(0.03) #Simulate 24 fps
                frame = cv2.imdecode(np.frombuffer(jpeg_data, np.uint8), cv2.IMREAD_COLOR)

                if frame is not None:

                    cv2.imshow('Video Stream', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.running = False
                    break

        time.sleep(5)
        cv2.destroyAllWindows()
video_streamer = AsyncVideoStreamer()
video_streamer.start_stream()


"""
for _ in range(100):
ret, frame = cap.read()
if not ret:
    break

# Convert frame to JPEG data
_, jpeg_data = cv2.imencode('.jpg', frame)

# Feed JPEG data to the video streamer
video_streamer.feed_frame(jpeg_data.tobytes())

cap.release()
"""

if __name__ == "__main__":

    # Example usage
    your_instance = YourClass()
    your_instance.select_file_and_collate_bytes()
    


    # Constants and Configurations
    width = 640
    height = 360
    num_components = 3
    quantization_table_selectors = [0, 1, 1]
    huffman_table_selectors = [(0, 0), (1, 1), (1, 1)]
    sampling_factors = [(1, 1), (1, 1), (1, 1)]

    # Building Huffman Tables and Segments
    huffman_header_dc = build_huffman_table_luminance_dc()
    huffman_header_dc_chrom = build_huffman_table_chrominance_dc()
    huffman_header_ac = build_huffman_table_ac()
    huffman_header_ac_chrom = build_huffman_table_ac_chrom()
    sof_segment = build_sof_segment(width, height, num_components, quantization_table_selectors, sampling_factors)
    sos_segment = build_sos_segment(num_components, huffman_table_selectors)
    quant_segment = build_default_quantization_table()

    # Calculate and Print Byte Sizes
    print("Number of bytes (AC Segment):", hex(int(len(huffman_header_ac.hex()) / 2)))
    print("Number of bytes (AC Chrom Segment):", hex(int(len(huffman_header_ac_chrom.hex()) / 2)))

    # Constructing the Image Byte Array
    image_bytes = bytearray(b'\xFF\xD8')  # Start of Image (SOI) marker
    image_bytes.extend(quant_segment)
    image_bytes.extend(huffman_header_dc)
    image_bytes.extend(huffman_header_dc_chrom)
    image_bytes.extend(huffman_header_ac)
    image_bytes.extend(huffman_header_ac_chrom)
    image_bytes.extend(sof_segment)
    image_bytes.extend(sos_segment)
    image_bytes_eoi = bytearray(b'\xFF\xD9')  # End of Image (EOI) marker

    # Collating Image Frames
    image_frame_array = []
    print("Started Processing Frames")
    for data in your_instance.get_collated_bytes():

        total_bytes = bytearray()
        total_bytes.extend(image_bytes)  # Start of Image and segments
        total_bytes.extend(data)         # Image data
        total_bytes.extend(image_bytes_eoi)  # End of Image
        image_frame_array.append(total_bytes)

    # Feeding Frames to Video Streamer
    for jpeg_data in image_frame_array:
        video_streamer.feed_frame(jpeg_data)
    video_streamer.stop()

    # Output video file name
    output_video_filename = "output_video.mp4"
    print(f"Video saved as: {output_video_filename}")

    # Create the video
    #create_video_from_images(image_frame_array, output_video_filename)
