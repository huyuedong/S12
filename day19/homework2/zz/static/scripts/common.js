/**
 * Created by liwenzhou on 2016/5/25.
 */

function addActive() {
    $("#sidebar-collapse").find("ul > li:first").addClass("active");
    $("#sidebar-collapse").find("ul > li > a").bind("click", function() {
    console.log($(this));
    console.log(this);
    $(this).parent("li").addClass("active");
    console.log($(this).parent("li"));
    console.log($(this).parent("li").siblings());
    $(this).parent("li").siblings().removeClass("active");
});
}

$(document).ready(function() {
    addActive();
});