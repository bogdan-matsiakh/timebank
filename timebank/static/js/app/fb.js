define(
    'app/facebook',
    ['app/main'],
    function( tb ){
        tb.facebook = (function () {
            var _getMe = function () {
                console.log('Welcome!  Fetching your information.... ');
                    FB.api('/me', function(response) {
                        console.log('Good to see you, ' + response.name + '.');
                        _meGetted(response)
                    });
            },
                _meGetted = function (response) {
                    _getPhoto()
                },
                _getPhoto = function () {
                    say('getting photo;')
                    FB.api('/me?fields=picture', function(response) {
                        say(response);
                    });
                },
                _getFriends = function () {
                    console.log('Getting list of friends ');
                    FB.api('/me/friends', function(response) {
                        _friendsGetted(response);
                    });
                },
                _getFriend = function (id) {
                    console.log('Getting friend ');
                    FB.api('/me/friends/' + id, function(response) {
                        _friendGetted(response);
                    });
                },
                _friendsGetted =function (response) {
                    _getFriend(response.data[0].id);
                },
                _friendGetted =function (response) {
                    say('friend')
                    say(response)
                }
            
            return {
                login : function () {
                    FB.login(function(response) {
                        if (response.authResponse) {
                            say('login connected');
                        } else {
                            say('login canceled');
                        }
                    });
                },
                
                getMe : function () {
                    _getMe();
                },
                getFriends : function () {
                    _getFriends();
                },
                getFriend : function (id) {
                    return _getFriend(id);
                }
            }
        })();
        
        return tb;
    }
);