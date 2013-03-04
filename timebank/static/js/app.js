say('in');
requirejs.config({
    //By default load any module IDs from js/lib
    baseUrl: 'js/lib',
    //except, if the module ID starts with "app",
    //load it from the js/app directory. paths
    //config is relative to the baseUrl, and
    //never includes a ".js" extension since
    //the paths config could be for a directory.
    paths: {
        app: '../app'
    }
});
requirejs(['app/fb', 'app/main'],
function   (tb) {
    say('in app');
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
});
