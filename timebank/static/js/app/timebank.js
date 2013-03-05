tb = (function () {
    var _header,
        _content,
        _footer;
        _headerControls,
        _contentControls,
        _footerControls;
    
    
    return {
        init : function () {
            _header = $("#header");
            _content = $("#content");
            _footer = $("#footer");
            _headerControls = {
                avatar : header.find('.avatar'),
                name : header.find('.name')
            };
            _contentControls = {
                
            };
            _footerControls = {
                
            }
        },
        get : function () {
            return {
                header : _header,
                headerControls : _headerControls,
                content : _content,
                contentControls : _contentControls,
                footer : _footer,
                footerControls : _footerControls
            }
        }
    }
})();


