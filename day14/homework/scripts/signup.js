/**
 * Created by liwenzhou on 2016/4/29.
 */

//编辑按钮的属性
function popEditPage() {
    $("a").click(function() {
        $("#pop-page").removeClass("hidden");
        //把当前值
        $(this).parent().parent().children().each(function() {
            if ($(this).attr("edit") == "true") {
                var cur_name = $(this).prop("class");
                var cur_value = $(this).text();
                $("#edit-form").children().each(function() {
                    if ($(this).attr("for") == cur_name) {
                        $(this).children(":first").val(cur_value);
                    }
                })
            }
        });
        //取消按钮绑定的事件
        $("#cancel-button").click(function() {
            $("#pop-page").addClass("hidden");
        })
    })
}

$(function() {
    popEditPage();
    //自定义的一个检测输入有效性的扩展
    $.checkValidity("#edit-form");
});