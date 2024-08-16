import requests

def download_obdaac(url, local_filename):
    try:
    # Send a GET request to the URL
        with requests.get(url, stream=True, verify=False) as response:
            # Check if the request was successful
            response.raise_for_status()
            # Open a local file with the desired name
            with open(local_filename, 'wb') as file:
                # Write the content to the file in chunks
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
        print(f"File downloaded as {local_filename}")
        return True
    except:
        return False
        print('File not found.')
fname="AQUA_MODIS.20240101_20240131.L3m.MO.CHL.chlor_a.4km.NRT.nc"
#fname="AQUA_MODIS.20240902.L3m.DAY.CHL.chlor_a.4km.NRT.nc"
url = 'https://oceandata.sci.gsfc.nasa.gov/ob/getfile/'+fname+'?appkey=fb95de75edd756ef103e91b2ec74c2dda74a3f93'  # Replace with the URL of the file
local_filename = fname         # Replace with the desired local filename
download_obdaac(url, local_filename)