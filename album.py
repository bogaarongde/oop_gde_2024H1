class User:

    def __init__(self):
        self._name = input("Add meg a neved: ")
        self._password = input("Add meg a jelszavad: ")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,newname):
        print ("Nem lehet változtatni")


    def check_password(self):
        input_password = input("Add meg a jelszavad a módosításhoz: ")
        if input_password == self._password:
            return True
        else:
            return False

class Pic:

    def __init__(self):
        self._name = ""
        self._format = ""
        self._size = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,ertek):
        self._name=ertek

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, ertek):
        self._size = ertek

    @property
    def format(self):
        return self._format

    @format.setter
    def format(self, ertek):
        self._format = ertek


class Album:

    def __init__(self,owner : User):
        self._owner = owner
        self._content = [Pic]

    def addPic(self,add_pic : Pic):
        if self._owner.check_password():
            self._content.append(add_pic)
        else:
            print("Rossz jelszó")

    @property
    def content(self):
        for picture in self._content:
            print(f"Név: {picture.name}.{picture.format}")
        return True

    @content.setter
    def content(self,ertke):
        print("így nem használd!")

my_user = User()

pic1 = Pic()

pic1.name = "kep1"
pic1.size = 20
pic1.format = "jpg"

pic2 = Pic()

pic2.name = "kep2"
pic2.size = 40
pic2.format = "png"

my_album = Album(my_user)

my_album.addPic(pic1)

my_album.addPic(pic2)

my_album.content