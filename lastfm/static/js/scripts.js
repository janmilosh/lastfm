$(document).ready(function() {
  
  var locationText = $('#location');
  var useSubmit = $('#use_submit');
  var hiddenInput = $('#set_location');

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
      var location = data.results[0].address_components[2].long_name + ', ' + data.results[0].address_components[5].long_name;
      useSubmit.hide().fadeIn(1000);
      locationText.hide().fadeIn(1000);
      locationText.text('Location: ' + location);
      hiddenInput.attr('value', location);
      useSubmit.html('<input type="submit" value="Use">').fadeIn();
    });
  };
});