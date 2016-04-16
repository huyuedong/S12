/**
 * Created by liwenzhou on 2016/4/13.
 */
//function stripeTables () {
//    if (!document.getElementsByTagName) return false;
//    var tables = document.getElementsByTagName("table");
//    var odd, rows;
//    for (var i=0;i<tables.length;i++) {
//        odd = false;
//        rows = tables[i].getElementsByTagName("tr");
//        if (rows.length < 1) return false;
//        for (var j=0;j<rows.length;j++) {
//            if (odd == true) {
//                rows[j].style.backgroundColor = "#EFF9A0";
//                odd = false;
//            } else {
//                odd = true;
//            }
//        }
//    }
//}
//为奇数行（第1,3,5行...）添加背景
function stripeTables() {
    $("tbody tr:nth-child(even)").addClass("tr_alt");

}
//鼠标悬停在表格的某一行时，该行文本加黑加粗
//function highlightRows () {
//    if (!document.getElementsByTagName) return false;
//    var rows = document.getElementsByTagName("tr");
//    for (var i=0;i<rows.length;i++) {
//        rows[i].onmouseover = function() {
//            this.style.fontWeight = "bold";
//        };
//        rows[i].onmouseout = function() {
//            this.style.fontWeight = "normal";
//        }
//    }
//}
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

//简写方法
$(function() {
   stripeTables();
});
//推荐方法
$(document).ready(function() {
   highlightRows();
});
