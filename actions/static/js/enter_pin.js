jQuery(document).ready(function () {
    var $screen = jQuery('.screen').find('input');
    var $keys = jQuery('.keys button');
    var $clear = jQuery('[name="clear-button"]');
    var $number_error = jQuery("[name='message-error']");
    var $ok_button = jQuery('[name="ok-button"]');
    var count = 0;

    $keys.on('click', function () {
        if (count == 4) {
            $number_error.show();
            setTimeout(function(){$number_error.hide()}, 4000);
            return
        }
        count = count + 1;
        var val = this.textContent.toString();
        $screen.val($screen.val() + val);
        if (count == 4) {
            console.log($ok_button.enabled);
            $ok_button[0].disabled = false;
            return
        }
    });

    $clear.on('click', function () {
        count = 0;
        $number_error.hide();
        $ok_button[0].disabled = true;
    });


});