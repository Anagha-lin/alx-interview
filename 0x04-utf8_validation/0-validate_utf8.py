#!/usr/bin/python3
def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    
    :param data: List of integers, where each integer represents a byte (8 bits)
    :return: True if data is a valid UTF-8 encoding, otherwise False
    """
    # Number of bytes remaining in the current UTF-8 character
    bytes_to_process = 0

    # Masks to identify byte patterns
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Extract the 8 least significant bits of the byte
        byte = byte & 0xFF

        if bytes_to_process == 0:
            # Count how many 1's are in the leading part of the byte
            mask = 1 << 7
            while mask & byte:
                bytes_to_process += 1
                mask = mask >> 1

            # If no 1's are found, it's a single-byte character
            if bytes_to_process == 0:
                continue

            # UTF-8 characters can only be 2 to 4 bytes long
            if bytes_to_process == 1 or bytes_to_process > 4:
                return False

        else:
            # Check if the byte starts with '10'
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the number of bytes left to process
        bytes_to_process -= 1

    # If all bytes were correctly processed, bytes_to_process should be 0
    return bytes_to_process == 0

