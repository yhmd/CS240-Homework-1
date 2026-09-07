# CS 240 — Assignment 1
## Converter and Pixel System

**Student:** Younes Hamedi
**Course:** CS 240 — Computer Organization
**Module:** Information as Bits

## Project Description

The objective of this assignment is to represent different forms of information using characters, number bases, and pixels.
The project contains four Python programs:

1. an ASCII character-to-decimal converter;
2. a converter between binary, decimal, octal, and hexadecimal;
3. a program that reads an image and writes its pixel information to a text file;
4. a program that reads the text file and reconstructs the image.

The project also contains a program that tests several 8-bit boundary values.

## Project Files

* `ascii_converter.py`: converts the characters of a word into decimal ASCII values.
* `base_converter.py`: converts numbers between binary, decimal, octal, and hexadecimal.
* `image_to_pixels.py`: reads `smiley.png`, displays the RGB pixel values, and creates `awesome_picture.txt`.
* `pixels_to_image.py`: reads `awesome_picture.txt`, displays the image using the letters R, B, and Y in the console, and creates `smiley2.png`.
* `boundary_tests.py`: tests the required 8-bit boundary values.
* `smiley.png`: original image.
* `awesome_picture.txt`: text representation of the image.
* `smiley2.png`: reconstructed image.

## Requirements

The programs require:

* Python 3;
* the Pillow library.

Pillow can be installed with the following command:

```bash
python -m pip install Pillow
```

## Running the Programs

All the programs and images must be placed in the same folder.

### ASCII-to-Decimal Converter

```bash
python ascii_converter.py
```

This program reads a word and displays the decimal value of each character.

### Number-Base Converter

```bash
python base_converter.py
```

This program asks for the original base and the number to convert. It then displays its binary, decimal, octal, and hexadecimal representations.

### Image-to-Pixel Conversion

```bash
python image_to_pixels.py
```

This program reads `smiley.png`, displays its RGB pixel values, and saves the color codes in `awesome_picture.txt`.

### Image Reconstruction

```bash
python pixels_to_image.py
```

This program must be executed after `image_to_pixels.py` because it uses the `awesome_picture.txt` file.

It displays a representation of the image using the letters R, B, and Y in the console and then saves the reconstructed image as `smiley2.png`.

### Boundary Tests

```bash
python boundary_tests.py
```

This program tests the required 8-bit boundary values.

## Tests Performed

I executed and verified all five programs in Spyder:

* the ASCII converter;
* the number-base converter;
* the image-to-text-file conversion;
* the reconstruction of the image from the text file;
* the boundary-value tests.

### Normal Tests

The ASCII converter was tested with the word `Younes` and displayed the decimal value of each character.
The number-base converter was tested with the decimal value `69` and displayed its binary, decimal, octal, and hexadecimal representations.
The image programs were tested by transforming `smiley.png` into a text representation and then reconstructing the image as `smiley2.png`.

### Boundary Tests

The following tests were performed using 8-bit values:

* zero: `00000000` represents `0`;
* largest unsigned value: `11111111` represents `255`;
* negative two's-complement value: `11111111` represents `-1`.

## Challenges Encountered

My first difficulty involved running the programs. I initially tried to use Visual Studio Code, but I was unable to correctly configure the Python terminal and the path to my files. I therefore decided to use Spyder to run and verify the programs.
I also had difficulties with conversions between binary, decimal, octal, and hexadecimal. In particular, I had to understand the original base of a number before displaying its different representations.
Finally, working with images required me to pay attention to the image dimensions and pixel coordinates. The width corresponds to the `x` axis, the height corresponds to the `y` axis, and the loops must correctly process the rows and columns of the image.

## Sources and Collaboration

The examples started in class with the instructor helped me understand the direction of the assignment and the general structure of the programs, especially for reading and reconstructing an image.
I also discussed the assignment with several classmates to remember the material presented in class and compare our understanding of the instructions.
ChatGPT was used as an aid to better understand the instructions, explain and debug the number-base converter for Question 2, and identify some programming errors.
I reviewed, executed, and verified the programs in Spyder.

## Generated Files

The image programs generate the following files:

* `awesome_picture.txt`;
* `smiley2.png`.

The text file provides a representation of the colors using the letters R, B, and Y. The reconstructed image can then be compared with the original image.

## License

This project was created for educational purposes as part of the CS 240 course at San Diego State University.
