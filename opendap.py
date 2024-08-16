import netCDF4 as nc
import xarray as xr

url = "http://oceandata.sci.gsfc.nasa.gov/opendap/MODISA/L3SMI/2024/0101/AQUA_MODIS.20240101.L3m.DAY.CHL.chlor_a.4km.NRT.nc"


da = xr.open_dataset(url,decode_times=False)
print('data read!')
da.to_netcdf(path='opendap.nc' ,mode='w',format='NETCDF4',  engine='netcdf4')
"""
def download_netcdf_from_opendap(url, local_filename):
    # Open the dataset from the OPeNDAP server
    dataset = xr.open_dataset(url, engine='netcdf4')  # Use 'pydap' if preferred
    
    # Print information about the dataset (optional)
    print(dataset)

    # Save the dataset to a local NetCDF file
    dataset.to_netcdf(local_filename)

# Example usage
local_filename = 'local_dataset.nc'                            # Local file name for saving
download_netcdf_from_opendap(url, local_filename)
"""