window.fbAsyncInit = function() {
    // init the FB JS SDK
    FB.init({
        appId : '109464542535160', // App ID from the App Dashboard
        channelUrl : 'http://lit-woodland-6028.herokuapp.com/channel', // Channel File for x-domain communication
        status : true, // check the login status upon init?
        cookie : true, // set sessions cookies to allow your server to access the session?
        xfbml : true // parse XFBML tags on this page?

    });

    FB.getLoginStatus(function(response) {
        console.log(response)
        if (response.status === 'connected') {
            console.log('connected');
            facebook.getMe();
            facebook.getFriends();
        } else if (response.status === 'not_authorized') {
            console.log('not_authorized')
        } else {
            console.log('not_logged_in');
        }
    });

    // Additional initialization code such as adding Event Listeners goes here

};

facebook = (function () {
    
    
    return {
        login : function () {
            FB.login(function(response) {
                if (response.authResponse) {
                    say('login connected');
                    testAPI();
                } else {
                    say('login canceled');
                }
            });
        },
        
        getMe : function () {
            console.log('Welcome!  Fetching your information.... ');
            FB.api('/me', function(response) {
                console.log('Good to see you, ' + response.name + '.');
            });
        },
        getFriends : function () {
            console.log('Welcome!  Fetching your information.... ');
            FB.api('/me/friends', function(response) {
                say(friends);
                console.log(response);
            });
        }
    }
})()

(function(d, debug) {
        var js, id = 'facebook-jssdk', ref = d.getElementsByTagName('script')[0];
        if (d.getElementById(id)) {
            return;
        }
        js = d.createElement('script');
        js.id = id;
        js.async = true;
        js.src = "//connect.facebook.net/en_US/all" + ( debug ? "/debug" : "") + ".js";
        ref.parentNode.insertBefore(js, ref);
    }(document, /*debug*/false));

function say(attr) {
    console.log(attr);
}