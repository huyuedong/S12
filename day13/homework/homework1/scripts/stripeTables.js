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
//全选
function checkAll() {
    $("#check-all").click(function() {
        $("form input").each(function() {
            $(this).prop("checked", true);
        });
    });
}
//反选
function invertCheck() {
    $("#invert-check").click(function() {
        $("form input").each(function() {
            if ($(this).prop("checked")) {
                $(this).prop("checked", false);
            } else {
                $(this).prop("checked", true);
            }
        })
    })
}
//取消

//进入编辑模式
function editRecord() {
    $("#edit").click(function() {
        //$("input:ckecked").parent().siblings().has("div").each(function() {
        $("input:checked").each(function() {
            console.log(1);
            //$(this).parents().siblings().has("div").children().each(function() {
            //    var old_value = $(this).text();
            //    console.log(old_value);
                //$(this).replaceWith("<input type='text'>")
            //})
        })
    })
}

//简写方法
$(function() {
    stripeTables();
});
//推荐方法
$(document).ready(function() {
    highlightRows();
    checkAll();
    invertCheck();
    editRecord();
});
