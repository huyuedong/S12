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
function popEditPage() {
    $("a").click(function(ths) {
        $("#pop-page").removeClass("hidden");
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