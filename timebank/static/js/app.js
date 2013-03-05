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
        if (response.status === 'connected') {
            console.log('connected');
            tb.status = true;
            say(response)
            tb.response = response;
        } else if (response.status === 'not_authorized') {
            console.log('not_authorized');
            FB.login();
        } else {
            console.log('not_logged_in');
            FB.login();
        }
    });
    // Additional initialization code such as adding Event Listeners goes here

}; 
( function(d, debug) {
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



$(document).ready(function() {
    function init() {
        if (tb.status) {
            say('logined')
            tb.init();
            tb.facebook.getMe();
            tb.facebook.getFriends();        
        }
        else {
            say('not logined yet');
            setTimeout(init, 500);
        }
    }
    init();
});

function say(attr) {
    console.log(attr);
}

