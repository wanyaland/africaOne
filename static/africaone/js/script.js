
WebFontConfig = {
  google: {
<<<<<<< HEAD
<<<<<<< HEAD
    families: [ 'Open Sans:400,700:latin' ]
=======
    families: [ 'Open Sans:300,400,500,600,700:latin' ]
>>>>>>> theming
=======
    families: [ 'Open Sans:300,400,500,600,700:latin' ]
>>>>>>> 6769cd1bea8dcd5a70a9d1f05ea170b2e02c3f2f
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

<<<<<<< HEAD
<<<<<<< HEAD
$(window).ready( function() {
  //call maps when dom ready
  loadMapScript();
=======
=======
>>>>>>> 6769cd1bea8dcd5a70a9d1f05ea170b2e02c3f2f
var africaOne = {};

//home page
africaOne.initiateHomePage = function() {

  //check for home page wrapper
  var $homePageWrapper = $('.home-page-wrapper.full-page-wrapper');
  if ($homePageWrapper.length <= 0) return;

  //banner slider
  var $bannerWrapper = $('.home-banner-reviews-wrapper');
  var bannerSlider = $bannerWrapper.unslider({
    autoplay: true,
    arrows: false,
    delay: 10000
  });
  $('.banner-review-start', $bannerWrapper).append('<div class="banners-arrow"><div class="slider-btn slider-btn-prev"><div class="arrow grey"></div><div class="arrow white"></div></div><div class="slider-btn slider-btn-next"><div class="arrow grey"></div><div class="arrow white"></div></div></div>');
  $('.slider-btn-next', $bannerWrapper).click ( function() {
    bannerSlider.unslider('next');
  });
  $('.slider-btn-prev', $bannerWrapper).click ( function() {
    bannerSlider.unslider('prev');
  });

};

$(window).ready( function() {

  //call maps when dom ready
  if ($('#business-map').length) {
    loadMapScript();
  }

  //home page
  africaOne.initiateHomePage();

<<<<<<< HEAD
>>>>>>> theming
=======
>>>>>>> 6769cd1bea8dcd5a70a9d1f05ea170b2e02c3f2f
});
