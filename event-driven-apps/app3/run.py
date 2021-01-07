from producer import publish


print('Start Publishing')
publish('app3_producer', {'event': 'from_app3'})