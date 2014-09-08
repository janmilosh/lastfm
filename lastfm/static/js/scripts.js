$(document).ready(function() {
  
  var locationText = $('#location');
  var useSubmit = $('#use_submit');
  var hiddenLocationInput = $('#set_location');
  var hiddenCityInput = $('#set_city');
  var hiddenStateInput = $('#set_state');
  var hiddenLatInput = $('#set_lat');
  var hiddenLonInput = $('#set_lon');

  //Click 'get my location' button to get location based on IP address
  //This returns the latitude and longitude.
  //With google maps reverse lookup, get the street address for the IP address
  $('button#get_location').on( "click", function() {
    getLocation();
  });
  
  function getLocation() {
    if (navigator.geolocation) {
      locationText.hide().fadeIn(1000);
      useSubmit.hide();
      locationText.text('Getting your location...this takes a minute.');
      navigator.geolocation.getCurrentPosition(showPosition);
    } else {
      locationText.fadeIn();
      locationText.text('Geolocation is not supported by this browser. Please enter City, State');
    }
  };

  function showPosition(position) {
    var API_KEY = 'AIzaSyDe1fq7oib8shkDokkXzJ8H1txRTLjR8k8'; //Google api key
    var lat = position.coords.latitude;
    var lon = position.coords.longitude;

    $.get('https://maps.googleapis.com/maps/api/geocode/json?latlng=' + lat + ',' + lon + '&location_type=ROOFTOP&result_type=street_address&key=' + API_KEY, function(data) {
      var city = data.results[0].address_components[2].long_name;
      var state = data.results[0].address_components[5].long_name;
      var location = city + ', ' + state;
      
      useSubmit.hide().fadeIn(1000);
      locationText.hide().fadeIn(1000);
      locationText.text('Location: ' + location);
      
      hiddenCityInput.attr('value', city);
      hiddenStateInput.attr('value', state);
      hiddenLocationInput.attr('value', location);
      hiddenLatInput.attr('value', lat);
      hiddenLonInput.attr('value', lon);
      useSubmit.html('<input type="submit" value="Use">').fadeIn();
    });
  };
});