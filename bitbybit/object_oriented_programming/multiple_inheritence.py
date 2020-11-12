
class Israel:

    def provide_agriculure_technology(self):
        print("We will provide you latest Agriculture Technology")


class India:

    def supply_spices(self):
        print("Spices have been supplied to you")


class Africa(India, Israel):
    pass

af = Africa()

af.supply_spices()
af.provide_agriculure_technology()

print(help(af))


class Africa(India, Israel):
    pass

af = Africa()

af.supply_spices()
af.provide_agriculure_technology()

print(help(af))

