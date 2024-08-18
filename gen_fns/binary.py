# ---------- Binary Encoding/Decoding Script ----------

# ----- Convert Binary Input to Decimal Output -----

def b2d(binary_string):

    decimal_number = int(binary_string, 2)
    return decimal_number

# ----- Convert Decimal Input to Binary Output -----

def d2b(decimal_number):

    binary_string = bin(decimal_number)[2:]
    return binary_string

# ----- Decimal Decoder -----

def decoder(decimal_value):

    classification_types = ['IR AGN', 'X-ray AGN', 'Radio AGN', 'Optical AGN', 'Gamma AGN']

    binary_string = format(decimal_value, '0' + str(len(classification_types)) + 'b')
    
    results = []
    
    # -- Unpack Binary String --

    for i, bit in enumerate(binary_string):

        if bit == '1':

            results.append(classification_types[i])
    
    # -- Create Readable Output --
            
    classification_info = ', '.join(results) if results else 'No AGN type'
    
    return classification_info
