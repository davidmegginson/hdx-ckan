var $notificationsSignupModal = $('#notificationsSignupBemModal');
var notificationsSignupModal = bootstrap.Modal.getOrCreateInstance($notificationsSignupModal.get(0));
var $signupSubmitButton = $notificationsSignupModal.find('button[type="submit"]');
var $signupDangerAlert = $notificationsSignupModal.find('.alert-danger');
var $signupForm = $notificationsSignupModal.find('#notification-platform-form');
var $signupFormPopupSourceInput = $signupForm.find('input[name="popup_source"]');

var $verificationModal = $('#notificationsVerificationBemModal');
var verificationModal = bootstrap.Modal.getOrCreateInstance($verificationModal.get(0));

var $unsubscribeModal = $('#notificationsUnsubscribeBemModal');
var unsubscribeModal = bootstrap.Modal.getOrCreateInstance($unsubscribeModal.get(0));

var $unsubscribedModal = $('#notificationsUnsubscribedBemModal');
var unsubscribedModal = bootstrap.Modal.getOrCreateInstance($unsubscribedModal.get(0));

var $unsubscribeSubmitButton = $unsubscribeModal.find('button[type="submit"]');
var $unsubscribeDangerAlert = $unsubscribeModal.find('.alert-danger');

var $actionMenuButton = $('.notification-platform-opt-in-action-menu');
var $floatingButton = $('.notification-platform-opt-in-floating-button');

var $unsubscribeToken = $('#unsubscribe_token');
var unsubscribeToken = null;
if($unsubscribeToken.length > 0 && $unsubscribeToken.data('token').toLowerCase() !== 'none') {
  unsubscribeToken = $unsubscribeToken.data('token');
}

$(document).ready(function () {

  var onSignupSubmit = function (e) {
    e.preventDefault();

    var formDataArray = $signupForm.serializeArray(), formData = {};
    $(formDataArray).each(function (i, field) {
      formData[field.name] = field.value;
    });

    var datasetId = formData.dataset_id;
    var email = formData.email;

    $.ajax({
      url: '/notifications/subscription-confirmation',
      method: 'POST',
      headers: hdxUtil.net.getCsrfTokenAsObject(),
      data: {
        'email': email,
        'dataset_id': datasetId,
        'g-recaptcha-response': formData['g-recaptcha-response'],
      },
      success: function (data) {
        grecaptcha.reset();
        if (data.success) {
          hideAlert($signupDangerAlert);
          notificationsSignupModal.hide();

          verificationModal.show();

          hdxUtil.analytics.sendNotificationPlatformPopupInteractionEvent(
            'confirm popup',
            'subscribe to notifications',
            formData.popup_source,
            datasetId,
            formData.dataset_name,
            hdxUtil.compute.strHash(email, 'notification_platform')
          );

        }
        else {
          showAlert($signupDangerAlert, data.error.message);
        }
      },
      error: function (xhr, status, error) {
        grecaptcha.reset();
        showAlert($signupDangerAlert, 'An error occurred. Please try again later.');
        console.log(xhr);
      },
    });
    return false;
  };

  var onUnsubscribeSubmit = function (e) {
    e.preventDefault();

    var unsubscribeToken = $unsubscribeModal.data('token');
    var email = $unsubscribeModal.data('email');
    var datasetId = $unsubscribeModal.data('dataset-id');
    var datasetName = $unsubscribeModal.data('dataset-name');
    $.ajax({
      url: '/notifications/unsubscribe-confirmation',
      method: 'POST',
      headers: hdxUtil.net.getCsrfTokenAsObject(),
      data: {
        'token': unsubscribeToken
      },
      success: function (data) {
        if (data.success) {
          hideAlert($unsubscribeDangerAlert);
          unsubscribeModal.hide();
          unsubscribedModal.show();

          hdxUtil.analytics.sendNotificationPlatformPopupInteractionEvent(
            'confirm popup',
            'unsubscribe from notifications',
            null,
            datasetId,
            datasetName,
            hdxUtil.compute.strHash(email, 'notification_platform')
          );
        }
        else {
          showAlert($unsubscribeDangerAlert, data.error.message);
        }
      },
      error: function (xhr, status, error) {
        showAlert($unsubscribeDangerAlert, 'An error occurred. Please try again later.');
        console.log(xhr);
      },
    });
    return false;
  };

  var showAlert = function ($alert, text) {
    $alert.text(text).removeClass('d-none');
  };

  var hideAlert = function ($alert) {
    $alert.text('').addClass('d-none');
  };

  var displayNotificationOptinOption = function () {
    var optinLocation = hdxUtil.net.getNotificationOptinLocation();

    if (optinLocation === 'action_menu') {
      $actionMenuButton.removeClass('d-none');
    }
    else if (optinLocation === 'floating_button') {
      $floatingButton.removeClass('d-none');
    }
  };

  $signupForm.on('submit', onSignupSubmit);
  $signupSubmitButton.on('click', onSignupSubmit);

  $unsubscribeSubmitButton.on('click', onUnsubscribeSubmit);

  $actionMenuButton.on('click', function(e) {
    e.preventDefault();
    var datasetId = $(this).data('dataset-id');
    var datasetName = $(this).data('dataset-name');
    showNotificationsSignupModal('action menu', datasetId, datasetName);
    return false;
  });

  $floatingButton.on('click', function(e) {
    e.preventDefault();
    var datasetId = $(this).data('dataset-id');
    var datasetName = $(this).data('dataset-name');
    showNotificationsSignupModal('floating button', datasetId, datasetName);
    return false;
  });

  if(unsubscribeToken) {
    unsubscribeModal.show();
    var datasetId = $unsubscribeModal.data('dataset-id');
    var datasetName = $unsubscribeModal.data('dataset-name');

    hdxUtil.analytics.sendNotificationPlatformPopupInteractionEvent(
      'show popup',
      'unsubscribe from notifications',
      null,
      datasetId,
      datasetName,
      null
    );
  }
  else {
    displayNotificationOptinOption();
  }
});

var showNotificationsSignupModal = function (popupSource, datasetId, datasetName) {
  var modalShownData = hdxUtil.net.getNotificationModalData() || {};

  if (!modalShownData[datasetId] || popupSource !== 'download') {
    notificationsSignupModal.show();
    $signupFormPopupSourceInput.val(popupSource);
    hdxUtil.analytics.sendNotificationPlatformPopupInteractionEvent(
      'show popup',
      'subscribe to notifications',
      popupSource,
      datasetId,
      datasetName,
      null
    );

    if(popupSource === 'download') {
      var newData = {};
      newData[datasetId] = true;
      hdxUtil.net.updateNotificationModalData(newData);
    }
  }
};

$notificationsSignupModal.on('hide.bs.modal', function () {
  $signupFormPopupSourceInput.val('');
});
