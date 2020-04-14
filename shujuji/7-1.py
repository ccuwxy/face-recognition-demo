import cv2

data = cv2.imread("olivettifaces.gif")

data = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)

faces = {}
label = 0
count = 1
pic_list = []
for row in range(20):
    for column in range(20):
        pic_list.append(data[row * 57:(row + 1) * 57, column * 47: (column + 1) * 47])
        if count % 10 == 0 and count != 0:
            faces[label] = pic_list
            label += 1
            pic_list = []
        count += 1
print(len(faces))

