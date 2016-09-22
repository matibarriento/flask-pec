// Empty JS for your own code to be here

function toggleMenu(current_menu){
    $(".nav.nav-pills>li").removeClass("active")
    $("#" + current_menu).addClass("active")
}
