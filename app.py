import os
message = os.getenv('SECRET_MSG', 'No secret message found!')
print('=' * 30)
print(f'MESSAGE FROM A FRIEND: {message}')
print('=' * 30)
