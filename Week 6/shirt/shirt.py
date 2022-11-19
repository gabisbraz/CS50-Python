from PIL import Image, ImageOps
import sys

def main():
	image = image_valid()
	edit_image(image)

def image_valid():
	try:
#if the user does not specify exactly two command-line arguments
		if len(sys.argv) < 3:
			sys.exit("Too few command-line arguments")
		if len(sys.argv) > 3:
			sys.exit("Too many command-line arguments")

#if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively
		ends = (".jpg", ".jpeg", ".png")
		if sys.argv[1].endswith(ends) == False or sys.argv[2].endswith(ends) == False:
			sys.exit("Invalid input")

#if the input’s name does not have the same extension as the output’s name, or
		end_before = sys.argv[1].split(".")
		end_after = sys.argv[2].split(".")
		if end_before[1] != end_after[1]:
			sys.exit("Input and output have different extensions ")

#if the specified input does not exist.
		image = Image.open(sys.argv[1])

	except(FileNotFoundError):
		sys.exit("Invalid input")

	else:
		return sys.argv[1], sys.argv[2]


def edit_image(image):
	before = image[0]
	after = image[1]

	img1 = Image.open(before)
	img2 = Image.open("shirt.png")

	img1 = ImageOps.fit(img1, (600, 600))

	img2 = img2.convert("RGBA")

	img1.paste(img2, img2)
	img1.save(after)

	#print(img1)
	#print(img2)

main()