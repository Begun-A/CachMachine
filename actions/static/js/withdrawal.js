$(document).ready(function () {
    var $screen = $('.screen input');
    var $keys = $('.keys button');
    var $clear = $('[name="clear-button"]');
    var count = 0;
    //keys actions
    $keys.on('click', function () {
        if (count==7){
            return
        }
        var val = this.textContent.toString();
        $screen.val($screen.val() + val);
        count = count + 1;
    });

    $clear.on('click', function(){
        count = 0
    })

});