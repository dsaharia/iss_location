# iss_location
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

This is a simple script which fetches the current co-ordinates of the International Space Station and converts the co-ordinates to address.
----
> API's Used -
    * http://api.open-notify.org/iss-now.json
    * http://api.open-notify.org/astros.json

## Libraries Used -
* Urllib (Requests) - To fetch the location and other API's.
* JSON - To parse the JSON which will be returned by the API response.
* Reverse-Geocoder - To get the address from the co-ordinates.[LINK](https://github.com/thampiman/reverse-geocoder)
