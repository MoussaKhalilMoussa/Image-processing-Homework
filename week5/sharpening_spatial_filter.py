import sys
import cv2 as cv


def main(argv):
    # [variables]
    # Declare the variables we are going to use
    ddepth = cv.CV_165
    kernel_size = 3
    window_name = "Laplace Demo"
    # [variables]

    # [load]
    imageName = argv[0] if len(argv) > 0 else 'lena.jpg'

    src = cv.imread(cv.smples.findFile(imageName), cv.IMREAD_COLOR)  # Load an image
    # check if image is loaded fine
    if src is None:
        print('Error opening image')
        print('Program Argument : [image_name -- default lena.jpg]')
        return -1
    # [load]
    # [reduce_noise]
    # Remove noise by blurring with a Gaussian filter
    src = cv.GaussianBlur(src, (3, 3), 0)
    # [reduce_noise]

    # [convert_to_gray]
    # Convert the image to grayscale
    src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    # [convert_to_gray]

    # Creat window
    cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)
    # [laplacian]
    # Apply Laplace function
    dst = cv.Laplacian(src_gray, ddepth, ksize=kernel_size)

    # [laplacian]
    # [convert]
    # converting back to uint8
    abs_dst = cv.convertScaleAbs(dst)

    # [display]
    cv.imshow(window_name, abs_dst)
    cv.waitkey(0)
    # [display]

    return 0


if __name__ == "__main__":
    main(sys.argv[1:])
