import numpy as np
import imageio as io
import matplotlib.pyplot as plt


def invert_colors(image):
    """
    Takes a color image (image), and returns
    a copy of it with inverted colors.
    """

    new = np.zeros(image.shape, dtype=int)
    # Subtracts values of image from 255 (the definition of inversion)
    new[:, :, :] = 255 - image[:, :, :]

    return new


def blur(image, patch):
    """
    Performs a blur on an image specified as a numpy array given a patch size.
    Creates a square kernal with size patch x patch.
    Returns blurred result.
    """

    image_height, image_width = image.shape
    # Kernal creation, essentially allows computing average of values in image.
    kernal = 1 / (patch ** 2) * np.ones((patch, patch), dtype=int)

    result_height = image_height - patch + 1
    result_width = image_width - patch + 1

    result = np.zeros((result_height, result_width))
    # Sliding window for loop
    for i in range(result_height):
        for j in range(result_width):
            window = image[i:i+patch, j:j+patch]
            result[i, j] = np.sum(window * kernal)

    result = result.astype(np.uint8)

    return result


def template_match(image, template):
    """
    Finds the location of template in image.
    Returns a new array with similarities computed utilizing
    a de-mean process prior to summation.
    """

    template_height, template_width = template.shape
    image_height, image_width = image.shape
    result_height = image_height - template_height + 1
    result_width = image_width - template_width + 1

    # Calculation of template mean and subtraction between actual and mean.
    template_mean = np.mean(template)
    template_sub = template - template_mean
    result = np.zeros((result_height, result_width))

    for i in range(result_height):
        for j in range(result_width):
            window = image[i:i + template_height, j: j + template_width]
            window_mean = np.mean(window)
            window_sub = window - window_mean

            result[i, j] = np.sum(template_sub * window_sub)

    return result


def find_xy(result):
    """
    Given the result of template_match, finds the position (x, y) with
    the highest similarity.
    """
    ij = np.unravel_index(np.argmax(result), result.shape)
    return ij[::-1]


def plot_result(image, template, result, output_file='match.png'):
    """
    Given an image, a template, and the result of
    template_match(image, template), makes a plot showing the result
    of the match.

    Saves result to given file path
    """
    x, y = find_xy(result)

    plt.figure(figsize=(8, 3))
    ax1 = plt.subplot(1, 3, 1)
    ax2 = plt.subplot(1, 3, 2)
    ax3 = plt.subplot(1, 3, 3, sharex=ax2, sharey=ax2)

    ax1.imshow(template, cmap=plt.cm.gray)
    ax1.set_axis_off()
    ax1.set_title('template')

    ax2.imshow(image, cmap=plt.cm.gray)
    ax2.set_axis_off()
    ax2.set_title('image')
    # highlight matched region
    template_height,  template_width = template.shape
    rect = plt.Rectangle((x, y), template_width, template_height,
                         edgecolor='r', facecolor='none')
    ax2.add_patch(rect)

    ax3.imshow(result)
    ax3.set_axis_off()
    ax3.set_title('`template_match`\nresult')
    # highlight matched region
    ax3.autoscale(False)
    ax3.plot(x, y, 'o', markeredgecolor='r', markerfacecolor='none',
             markersize=10)
    plt.savefig(output_file)


def main():
    image = 'images/puppy.png'
    image = io.imread(image)
    invert = invert_colors(image)
    plt.imshow(invert)
    plt.savefig('invert_puppy.png')

    blur_image = io.imread('images/gray_puppy.png')

    blur_30 = blur(blur_image, 30)
    plt.imshow(blur_30, cmap=plt.cm.gray)
    plt.savefig('blur30.png')

    template = blur_image[355:435, 200:276]
    result_template = template_match(blur_image, template)
    plot_result(blur_image, template, result_template)


if __name__ == '__main__':
    main()
