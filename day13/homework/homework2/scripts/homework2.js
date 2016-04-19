/**
 * Created by liwenzhou on 2016/4/18.
 */
//为奇数行（第1,3,5行...）添加背景
function stripeTables() {
    $("tbody tr:nth-child(even)").addClass("tr_alt");

}
//鼠标悬停在表格的某一行时，该行文本加黑加粗
function highlightRows() {
    $("tr").hover(
        function() {
            $(this).css("fontWeight", "bold");
        },
        function() {
            $(this).css("fontWeight", "normal");
        }
    );
}
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
    stripeTables();
    highlightRows();
    popEditPage();
    //自定义的一个检测输入有效性的扩展
    $.checkValidity("#edit-form");
});