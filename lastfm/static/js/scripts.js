$(document).ready(function() {
  
  var locationDiv = $('#location');

  $('button#get_location').on( "click", function() {
    
    getLocation();

  });

  console.log(locationDiv);
  
  function getLocation() {
    if (navigator.geolocation) {
      console.log('There is geolocation');
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        locationDiv.text("Geolocation is not supported by this browser.");

    }
  };

  function showPosition(position) {
      locationDiv.html("Latitude: " + position.coords.latitude + 
      "<br>Longitude: " + position.coords.longitude); 
  };

});