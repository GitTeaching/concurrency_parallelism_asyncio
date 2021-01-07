from producer import publish


print('Start Publishing')
publish('app1_producer', {'event': 'from_app1'})