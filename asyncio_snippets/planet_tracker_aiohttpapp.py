from planet_tracker import PlanetTracker
from aiohttp import web

import asyncio


__all__ = ["app"]


routes = web.RouteTableDef()


# Testing route: http://localhost:8000/
@routes.get('/')
async def hello(request):
    return web.FileResponse("./planet_tracker_index.html")


# Testing route: http://localhost:8000/planets/mars?long=145.05&lat=-39.754&elevation=0
@routes.get("/planets/{name}")
async def get_planet_ephmeris(request):
	planet_name = request.match_info['name']
	data = request.query
	geo_location_data = {}
	try:
		geo_location_data = {
			'long': str(data['long']),
			'lat': str(data['lat']),
			'elevation': float(data['elevation'])
		}
	except KeyError as err:
		geo_location_data = {
			'long': '-0.0005',
			'lat': '51.4769',
			'elevation': 0.0
		}

	planet_tracker = PlanetTracker()
	planet_tracker.lat = geo_location_data['lat']
	planet_tracker.long = geo_location_data['long']
	planet_tracker.elevation = geo_location_data['elevation']
	planet_data = planet_tracker.calc_planet(planet_name)

	return web.json_response(planet_data)


app = web.Application()
app.add_routes(routes)

# Serving "static" assets like CSS and JavaScript - discouraged - just for testing
app.router.add_static('/', './')

# The web.run_app function runs our app in a blocking manner - non concurrent
# web.run_app(app, host="localhost", port=8000)


# For concurrent run :
# run_app() provides a simple blocking API for running an Application.
# For starting the application asynchronously or serving on multiple HOST/PORT, AppRunner exists
async def start_async_app():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "localhost", 8000)
    await site.start()
    return runner, site

loop = asyncio.get_event_loop()
runner, site = loop.run_until_complete(start_async_app())

# To stop serving, call AppRunner.cleanup()
try:
    loop.run_forever()
except KeyboardInterrupt as err:
    loop.run_until_complete(runner.cleanup())