from producer import publish


print('Start Publishing')
publish('app2_producer', {'event': 'from_app2'})