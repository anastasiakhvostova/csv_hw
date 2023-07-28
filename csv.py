import requests
import time
base_url = 'http://api.open-notify.org/iss-now.json'
while True:
    params = {
                'q': 'length',
                'units': 'width', }
    response = requests.get(url=base_url, params=params)
    data = response.json()
    result = f"{data['iss_position']['longitude']}; {data['iss_position']['latitude']}\n"
    print(result, end='')
    with open(f'location/location.csv', 'a') as file:
        file.write(result)

    time.sleep(5)
