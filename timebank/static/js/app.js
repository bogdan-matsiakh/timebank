require(
    ['app/fb', 'app/main'],
    function( tb ){
        FB.getLoginStatus(function(response) {
                        if (response.status === 'connected') {
                            console.log('connected');
                            tb.facebook.getMe();
                            tb.facebook.getFriends();
                        } else if (response.status === 'not_authorized') {
                            console.log('not_authorized')
                        } else {
                            console.log('not_logged_in');
                        }
                    });
    }
);