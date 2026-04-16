def encode_caesar(text: str, shift: int) -> str:
    """
    Encode a given text using the Caesar cipher.
    """
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


def decode_caesar(text: str, shift: int) -> str:
    """
    Decode a Caesar cipher–encoded text.
    """
    return encode_caesar(text, -shift)


def read_text(path: str) -> str:
    """
    Read the entire content of a text file.
    """
    with open(path, "r") as file:
        return file.read()


def write_text(path: str, text: str) -> None:
    """
    Write text to a file.
    """
    with open(path, "w") as file:
        file.write(text)


def main():
    input_file = "encoded.txt"
    output_file = "decoded.txt"
    shift = 3

    encoded_text = read_text(input_file)
    decoded_text = decode_caesar(encoded_text, shift)

    write_text(output_file, decoded_text)

    print("Decoding complete!")
    print("Decoded text saved to:", output_file)


if __name__ == "__main__":
    main()