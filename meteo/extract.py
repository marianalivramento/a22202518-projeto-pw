import zipfile

# Specify the path to your zip file
path_to_zip_file = "static/meteo/icons_ipma_weather.zip"

# Specify the directory where you want to extract the contents
directory_to_extract_to = "static/meteo/"

# Extract all contents of the zip file
with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
    zip_ref.extractall(directory_to_extract_to)