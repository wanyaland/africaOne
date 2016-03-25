
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

/**
 * validate form
 */
africaone.initialiseBusinessForm = function() {
  var $form = $('form#create-business-form');
  $form.attr('novalidate', 'novalidate');

  // initialize the validator function
  //validator.message['date'] = 'not a real date';

  // validate a field on "blur" event, a 'select' on 'change' event & a '.reuired' classed multifield on 'keyup':
  $form
      .on('blur', 'input[required], input.optional, select.required', validator.checkField)
      .on('change', 'select.required', validator.checkField)
      .on('keypress', 'input[required][pattern]', validator.keypress);

  $('.multi.required', $form)
      .on('keyup blur', 'input', function () {
        validator.checkField.apply($(this).siblings().last()[0]);
      });

  $form.submit(function (e) {
    e.preventDefault();
    var submit = true;
    var $this = $(this);
    if (!validator.checkAll($(this))) {
      submit = false;
    }
    if (submit)
      this.submit();
    return false;
  });

  //hours functionality
  var $hoursDisplayWrapper = $('.hours-wrapper', $form);
  var $hoursElem = $('.hours.hidden', $hoursDisplayWrapper).detach().removeClass('hidden');
  var $hoursForm = $('.hours-select', $form);
  var $weekdaySelect = $('.weekday', $hoursForm);
  var $startHourSelect = $('.hours-start', $hoursForm);
  var $endHourSelect = $('.hours-end', $hoursForm);
  $('.btn', $hoursForm).click( function() {
    var $newHoursElem = $hoursElem.clone();
    $('.weekday', $newHoursElem).text($('option:selected', $weekdaySelect).text());
    $('.start', $newHoursElem).text($('option:selected', $startHourSelect).text());
    $('.end', $newHoursElem).text($('option:selected', $endHourSelect).text());
    $('input', $newHoursElem).val($weekdaySelect.val() + ' ' + $startHourSelect.val() + ' ' + $endHourSelect.val());
    $('.remove-hours', $newHoursElem).click( function() {
      $newHoursElem.remove();
      return false;
    });
    var $nextOption = $('option:selected', $weekdaySelect).next();
    $newHoursElem.appendTo($hoursDisplayWrapper);
    if ($nextOption.length <= 0) {
      $nextOption = $('option:first-child', $weekdaySelect);
    }
    $weekdaySelect.val($nextOption.attr('value'));
    //$nextOption.attr('selected', 'selected'); //not working after first loop
  });

  //phone mask
  $('#business-phone', $form).inputmask();

  //autocomplete categories
  var $categoriesSelect = $('#business-category', $form);
  var $chosenCategoriesWrapper = $('.chosen-categories-wrapper', $form);
  var $chosenCategoryElem = $('.chosen-category', $chosenCategoriesWrapper).detach().removeClass('hidden');
  var arrow = '<i class="category-spacer fa fa-angle-right"></i>';
  var checkMaxCategoriesNo = function() {
    var maxNo = 3;
    if ($('.chosen-category', $chosenCategoriesWrapper).length >= maxNo) {
      $categoriesSelect.prop('disabled', true);
    } else {
      $categoriesSelect.prop('disabled', false);
    }
  };
  $categoriesSelect.autocomplete({
    serviceUrl: 'http://local.dev/plainphp/africaone_categories.php',
    appendTo: '#categories-autocomplete-container',
    showNoSuggestionNotice: true,
    noSuggestionNotice: 'No categories found with this criteria. Please try again.',
    beforeRender: function(container) {
      $('.autocomplete-suggestion', $(container)).each( function(index, elem) {
        var $row = $(elem);
        $row.html($row.html().replace(' > ', arrow));
      });
    },
    onSelect: function (suggestion) {
      var $newChosenCategoryElem = $chosenCategoryElem.clone();
      $('span', $newChosenCategoryElem).html(suggestion.value.replace(' > ', arrow));
      $('input', $newChosenCategoryElem).val(suggestion.data);
      $('.remove-category', $newChosenCategoryElem).click( function() {
        $newChosenCategoryElem.remove();
        checkMaxCategoriesNo();
        return false;
      });
      $newChosenCategoryElem.appendTo($chosenCategoriesWrapper);
      checkMaxCategoriesNo();
      $categoriesSelect.val('').focus();
    }
  });

  //map latitude and longitude picker
  var $mapWrapper = $('#business-location-map', $form);
  var $searchBtn = $('.search-btn', $form);
  var $locationDiv = $('.business-location-name', $form);
  var $locationNameInput = $('.gllpLocationName', $form);
  var locationText = 'Please pick your location on the map above by moving the marker OR double clicking on the map.';
  $('.gllpSearchField', $mapWrapper).on("keypress", function(e) {
    if (e.keyCode == 13) {
      $searchBtn.click();
      return false; // prevent the button click from happening
    }
  });
  $(window).on('location_changed', function(e, node) {
    var locationName = $locationNameInput.val();
    var textStr = '';
    if (locationName) {
      textStr = 'Business Location: ' + locationName;
      $locationDiv.removeClass('bg-primary').addClass('bg-success');
    } else {
      textStr = locationText;
      $locationDiv.addClass('bg-primary').removeClass('bg-success');
    }
    $locationDiv.text(textStr);
  });

};

$(window).ready( function() {
  africaone.initiateBusinesses();
  africaone.initialiseBusinessForm();
});
