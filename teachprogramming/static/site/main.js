//$('#navbar').scrollspy();

//$('#sidebar_affix').affix();

function apply_active_anchor($a) {
    $('.sidebar-nav-container').find('.active a').each(function() {
        $a.attr('href', $a.attr('href')+$(this).attr('href'));
    });
}

function scrollTo ($el) {
    $('html, body').animate({
        scrollTop: $el.offset().top
    }, 500);
} 

// Init
$(document).ready(function() {
    // Hijack any links that are clicked
    // if they start with '#' then scroll to them smoothly and prevent the following of the actual link-page change
	$('a[href^="#"]').on('click', function(){
        var
        href  = $(this).prop('href'),
        $hash = $(href.substr(href.indexOf('#')));
        console.log($hash);
        scrollTo($hash);
        return false;
    });
});
