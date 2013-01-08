//$('#navbar').scrollspy();

//$('#sidebar_affix').affix();

function apply_active_anchor($a) {
    $('.sidebar-nav-container').find('.active a').each(function() {
        $a.attr('href', $a.attr('href')+$(this).attr('href'));
    });
}