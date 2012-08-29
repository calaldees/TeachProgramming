
//!function ($) {

//    $(function(){  
        var $window = $(window);
        
        // side bar
        $('.affix_sidebar').affix({
          offset: {
            top: function () { return $window.width() <= 980 ? 100 : 100 }
          , bottom: 0
          }
        });
        
        console.log('Hello');
        
        // make code pretty
        //window.prettyPrint && prettyPrint();
//    });
    
//}