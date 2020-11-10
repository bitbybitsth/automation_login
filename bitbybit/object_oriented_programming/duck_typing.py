class Maharashtrian:

    def speak_in_marathi(self):
        print("Ram Ram Pahune")

class Gujrati:

    def speak_in_marathi(self):
        print("Jevan Zhala ka")

    def speak_in_gujrati(self):
        pass


class Andra:
    pass


def function(person):
    person.speak_in_marathi()
    # person.speak_in_gujrati()



marathi = Maharashtrian()
gujrati = Gujrati()
andh = Andra()

# function(andh)


function(gujrati)
function(marathi)