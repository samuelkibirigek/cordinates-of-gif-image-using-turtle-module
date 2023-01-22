import turtle
import pandas

screen = turtle.Screen()

screen.title("Name the parts of a face Game")

image = "face_image.gif"
screen.addshape(image)
turtle.shape(image)
coor = []
parts = ["eye", "nose", "mouth", "cheeks", "forehead", "chin", "eyebrows"]


def position_coordinates_generation(x, y):
    coor.append((x, y))
    print(coor)
    if len(coor) == 7:
        face_dict = {
            "parts": parts,
            "position": coor
        }

        data = pandas.DataFrame(face_dict)
        print(data)

        data.to_csv("facial_features.csv")


# After I have created the csv file of coordinates I can comment out the code that calls the function below.
screen.onscreenclick(position_coordinates_generation)

turtle.mainloop()
