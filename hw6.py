# *************** HOMEWORK 6 ***************
# GOOD LUCK!

# ********************* Helper functions ***********************
import matplotlib.pyplot as plt


def display(image):
    plt.imshow(image, cmap="gist_gray")
    plt.show()


# ************************ QUESTION 1 **************************
def load_binary_image(img_path):
    f = open(img_path, 'r')  # open the text file in 'read' mode.
    result = []  # outer list we gonna fill with lists of pixels.
    for line in f.read().splitlines():  # loop through lines of the text file.
        temp_line = []  # going to be filled with pixels (chars from the text file lines) each iterate.
        for pixel in line:  # loop through chars of the text file lines.
            temp_line.append(int(pixel))  # inserts the pixel to the temp_line as an integer.
        result.append(list(temp_line))  # inserts the temp_line to the outer list.
    f.close()  # closing the file we opened.
    return result  # returns the outer list.


# ************************ QUESTION 2 **************************
def add_padding(image, padding):
    new_image = padding * [list(len(image[0]) * [0] + (padding * 2) * [0])]  # create new list (image) and fill it with top of the frame (zeros).
    for line in image:  # loop through lines of original image (lines og pixels).
        new_image += [list(padding * [0]) + line + list(padding * [0])]  # adds zeros before and after original lines.
    new_image += padding * [list(len(image[0]) * [0] + (padding * 2) * [0])]  # adds bottom of the frame (zeros).
    return new_image  # returns the new padded image.


# ************************ QUESTION 3 **************************
def erosion(img_path, structuring_element):
    zeros_only = True  # structuring element is made of zeros only until proven otherwise.
    for row in structuring_element:  # loop through the structuring element rows.
        if 1 in row:  # if row contains 1 (no 0):
            zeros_only = False  # structuring element is not made of zeros only.
            break  # if 1 found in structuring element no need to loop anymore.
    if zeros_only:  # check whether structuring element is made of zeros only.
        return load_binary_image(img_path)  # if it is, original image is not going to be changed so we return it now.
    result = []  # outer list we gonna fill with lists of pixels.
    padding = int((len(structuring_element[0]) - 1) / 2)  # calculates the padding according to the structuring element.
    padded_img = add_padding(load_binary_image(img_path), padding)  # creates new image made of original image + padding.
    for i in range(len(padded_img) - 2):  # iterates from first row of padded image to the third row from the end.
        temp_line_result = []  # going to be filled with pixels each iterate.
        for j in range(len(padded_img[0]) - 2):  # iterates from first pixel of row to the third pixel from the end.
            turn_white = True  # each pixel will be 1 if there will be no reason not to.
            for k in range(len(structuring_element)):  # loop through kernel's rows.
                for l in range(len(structuring_element[0])):  # loop through kernel's pixels in each row.
                    if structuring_element[k][l] == 1 and padded_img[i+k][j+l] == 0:  # erosion's condition not to put 1 in the pixel.
                        turn_white = False  # pixel will not change.
                        break  # no need to keep look for a reason not to put 1, in the current line.
                if not turn_white:  # if the pixel will not change to 1.
                    break  # no need to keep look for a reason not to put 1, in the next rows.
            if turn_white:  # if the pixel need to be 1.
                temp_line_result.append(1)  # put 1 in pixel (of result image).
            else:  # if the pixel dont need to be 1, it should be 0.
                temp_line_result.append(0)  # put 0 in pixel (of result image).
        result.append(list(temp_line_result))  # inserts the temp_line_result to the outer list.
    return result  # returns the outer list.


# ************************ QUESTION 4 **************************
def dilation(img_path, structuring_element):
    zeros_only = True  # structuring element is made of zeros only until proven otherwise.
    for row in structuring_element:  # loop through the structuring element rows.
        if 1 in row:  # if row contains 1 (no 0):
            zeros_only = False  # structuring element is not made of zeros only.
            break  # if 1 found in structuring element no need to loop anymore.
    if zeros_only:  # check whether structuring element is made of zeros only.
        return load_binary_image(img_path)  # if it is, original image is not going to be changed so we return it now.
    result = []  # outer list we gonna fill with lists of pixels.
    padding = int((len(structuring_element[0]) - 1) / 2)  # calculates the padding according to the structuring element.
    padded_img = add_padding(load_binary_image(img_path), padding)  # creates new image made of original image + padding.
    for i in range(len(padded_img) - 2):  # iterates from first row of padded image to the third row from the end.
        temp_line_result = []  # going to be filled with pixels each iterate.
        for j in range(len(padded_img[0]) - 2):  # iterates from first pixel of row to the third pixel from the end.
            turn_white = False  # will not put 1 in each pixel if there will be no reason not to.
            for k in range(len(structuring_element)):  # loop through kernel's rows.
                for l in range(len(structuring_element[0])):  # loop through kernel's pixels in each row.
                    if structuring_element[k][l] == 1 and padded_img[i + k][j + l] == 1:  # dilation's condition to put 1 in the pixel.
                        turn_white = True  # will put 1 in pixel.
                        break  # no need to keep look for a reason to put 1, in the current line.
                if turn_white:  # if the pixel will be 1.
                    break  # no need to keep look for a reason to put 1, in the next rows.
            if turn_white:  # if the pixel need to be 1.
                temp_line_result.append(1)  # put 1 in pixel (of result image).
            else:  # if the pixel dont need to be 1, it should be 0.
                temp_line_result.append(0)  # put 0 in pixel (of result image).
        result.append(list(temp_line_result))  # inserts the temp_line_result to the outer list.
    return result  # returns the outer list.