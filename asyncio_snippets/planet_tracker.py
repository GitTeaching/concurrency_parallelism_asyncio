import ephem
import math


class PlanetTracker(ephem.Observer):
	def __init__(self):
		super(PlanetTracker, self).__init__()
		self.planets = {
			"mercury": ephem.Mercury(),
			"venus": ephem.Venus(),
			"mars": ephem.Mars(),
			"jupiter": ephem.Jupiter(),
			"saturn": ephem.Saturn(),
			"neptune": ephem.Neptune(),
			"uranus": ephem.Uranus()
		}

	def calc_planet(self, planet_name, when=None):
		convert = 180./math.pi

		if when is None:
			when = ephem.now()

		self.date = when

		if planet_name in self.planets:
			planet = self.planets[planet_name]
			planet.compute(self)
			return {
				'az': float(planet.az) * convert,
				'alt': float(planet.alt) * convert,
				'name': planet_name
			}
		else:
			raise KeyError(f"Couldn't find {planet_name} in planets dict.")


# planet_tracker = PlanetTracker()
# planet_tracker.lat = "51.4769"
# planet_tracker.long = "-0.0005"
# print(planet_tracker.calc_planet('mars'))


