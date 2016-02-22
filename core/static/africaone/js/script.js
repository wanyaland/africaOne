
WebFontConfig = {
  google: {
    families: [ 'Open Sans:400,700:latin' ]
  },
  active: function() {
    //jQuery(window).trigger("debouncedresize");
  }
};
(function() {
  var wf = document.createElement('script');
  wf.src = ('https:' == document.location.protocol ? 'https' : 'http') +
  '://ajax.googleapis.com/ajax/libs/webfont/1/webfont.js';
  wf.type = 'text/javascript';
  wf.async = 'true';
  var s = document.getElementsByTagName('script')[0];
  s.parentNode.insertBefore(wf, s);
})();



function initializeMap() {
  var $mapDiv = $('#business-map');
  var mapPosn = $mapDiv.data('business-location').split(',');
  var latLngPosn = new google.maps.LatLng(mapPosn[0], mapPosn[1]);
  var map = new google.maps.Map(document.getElementById($mapDiv.attr('id')), {
    center: latLngPosn,
    zoom: 15,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  });
  var marker = new google.maps.Marker({
    position: latLngPosn,
    map: map,
    title: $mapDiv.data('title')
  });

  // Reposition on resize.
  google.maps.event.addDomListener(window, 'resize', function() {
    map.setCenter(latLngPosn);
  });

}

function loadMapScript() {
  var script = document.createElement('script');
  script.type = 'text/javascript';
  script.src = 'https://maps.googleapis.com/maps/api/js?v=3.exp&callback=initializeMap';
  document.body.appendChild(script);
}

$(window).ready( function() {
  //call maps when dom ready
  loadMapScript();
});
