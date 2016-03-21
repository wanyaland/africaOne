
var africaone = {};

/**
 * businesses list
 */
africaone.initiateBusinesses = function() {
  var $wrapper = $('.africaone-home-wrapper .businesses-list');
  if ($wrapper.length <= 0) {
    return;
  }

  var $listItemsWrapper = $('.businesses-list-items-wrapper', $wrapper);
  var $detailsItemsWrapper = $('.businesses-full-details-wrapper', $wrapper);

  $('.business-list-item', $listItemsWrapper).click( function() {
    var $businessItem = $(this);
    var businessID = $businessItem.data('id');

    $('.business-list-item', $listItemsWrapper).removeClass('active');
    $businessItem.addClass('active');

    $('.business-full-detail-wrapper', $detailsItemsWrapper).hide();
    $('#business-full-detail-' + businessID, $detailsItemsWrapper).show();

    $wrapper.addClass('showing-details');
  });

  $('.close-btn-col .btn', $detailsItemsWrapper).click( function() {
    $wrapper.removeClass('showing-details');
  });

};

$(window).ready( function() {
  africaone.initiateBusinesses();
});
