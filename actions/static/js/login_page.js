$(document).ready(function () {
    var $screen = $('.screen input');
    var $keys = $('.keys button');
    var $clear = $('[name="clear-button"]');
    var $ok_button = $('[name="ok-button"]');
    var $exit = $('[name="exit-button"]');
    var count = 0;

    $exit.hide();

    //keys actions
    $keys.on('click', function () {
        //enter the card number
        if ($screen[0].getAttribute('id') == 'number') {
            if (count == 16) {
                $("[id='number-error']").show();
                setTimeout(function () {
                    $("[id='number-error']").hide()
                }, 2000);
                return
            }
            count = count + 1;
            var val = this.textContent.toString();
            $screen.val($screen.val() + val);
            if (count % 4 == 0 && count != 0 && count / 4 != 4) {
                $screen.val($screen.val() + '-')
            }
            if (count == 16) {
                $ok_button[0].disabled = false;
                return
            }
        }
        //enter the pin
        if ($screen[0].getAttribute('id') == 'pin') {
            if (count == 4) {
                $("[id='pin-error']").show();
                setTimeout(function () {
                    $("[id='pin-error']").hide()
                }, 2000);
                return
            }
            count = count + 1;
            var val = this.textContent.toString();
            $screen.val($screen.val() + val);
            if (count == 4) {
                $ok_button[0].disabled = false;
                return
            }
        }

    });

    $clear.on('click', function () {
        count = 0;
        $("[id='number-error']").hide();
        $("[id='pin-error']").hide();
        $ok_button[0].disabled = true;
    });

    $exit.on('click', function(){
        window.location.reload();
    });

    $ok_button.on('click', function (event) {
        // request with card number
        if ($screen[0].getAttribute('id') == 'number') {
            var number = $('input[id=number]').val();
            $.ajax({
                type: "POST",
                url: "",
                dataType: "json",
                data: {
                    'number': number,
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
                },
                success: function (data) {
                    var success = data['success'];
                    if (!success) {
                        var error = data['message'];
                        alert(error);


                    }

                    if (success) {
                        $("[id='number-error']").hide();
                        $("[id='success-message']").show();
                        $ok_button[0].disabled = true;
                        count = 0;
                        $screen.val("");
                        $exit.show();
                        $screen[0].setAttribute('id', 'pin');
                        $screen[0].setAttribute('type', 'password');
                        $("[id='number-requezt']").hide();
                        $("[id='pin-requezt']").show();

                        setTimeout(function () {
                            $("[id='success-message']").hide();
                        }, 2000);
                    }
                }

            });//end ajax
        }
        //request with pin
        if ($screen[0].getAttribute('id') == 'pin') {
            var pin = $('input[id=pin]').val();
            $.ajax({
                type: "POST",
                url: "",
                dataType: "json",
                data: {
                    'pin': pin,
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
                },
                success: function (data) {
                    var success = data['success'];
                    if (!success) {
                        var error = data['message'];
                        count = 0;
                        $screen.val('');
                        alert(error);

                    }
                    if (success) {
                        window.location.href = data["redirect"];
                    }
                }

            });//end ajax
        }
    });


});