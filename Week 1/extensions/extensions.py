gif = "gif"
jpg = "jpg"
jpeg = "jpeg"
png = "png"
pdf = "pdf"
txt = "txt"
zipp = "zip"

x = str(input("File name: "))
y = x.lower()

if gif in y:
    print("image/gif")
elif jpg in y:
    print("image/jpg")
elif jpeg in y:
    print("image/jpeg")
elif png in y:
    print("image/png")
elif pdf in y:
    print("application/pdf")
elif txt in y:
    print("text/plain")
elif zipp in y:
    print("application/zip")
else:
    print("application/octet-stream")
