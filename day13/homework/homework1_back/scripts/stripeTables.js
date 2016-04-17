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
        if ($("input:checked").length > 0) {
            $("input:checked").parent().siblings().has("div").each(function() {
                var tr_id = $(this).parents("tr").prop("id");
                $(this).children().each(function() {
                    var old_value = $(this).text();
                    if ($(this).parent().prop("class") != "state") {
                        $(this).replaceWith("<input type='text' value=" + old_value + ">");
                    } else {
                        //给select生成一个id，方便后面查找
                        var current_id = tr_id+"-select";
                        $(this).replaceWith("<select id='"+current_id+"' name='state'></select>");
                        $("<option></option>").val("0").text("在线").appendTo($("#"+current_id));
                        $("<option></option>").val("1").text("下线").appendTo($("#"+current_id));
                        //$("#"+current_id+" option[text='"+old_value+"']").attr("selected", true);
                        $("#"+current_id+" option:contains('"+old_value+"')").attr("selected", true);
                        //this.find("option:contains('"+old_value+"')").attr("selected", true);
                    }
                })
            });
            //$("#select-page").addClass("hidden");
            $("#select-page").hide();
            $("#edit-page").show();
            //$(".button-set").append("<ul id='edit-page'></ul>");
            //$("#edit-page").append("<li><button id='cancel' type='button'>取消</button></li>");
            //$("#edit-page").append("<li><button id='save' type='button'>保存</button></li>");
        } else {
            shake($("tbody .option"),"red",2);
        }
    })
}
//闪烁提示
function shake(ele,cls,times) {
    var i = 0,t=null,o=ele.prop("class")+ " ",c="",times=times||2;
    if (t) return;
    t = setInterval(function() {
        i++;
        c = i%2 ? o+cls : o;
        ele.prop("class", c);
        if (i==2*times) {
            clearInterval(t);
            ele.removeClass(cls);
        }
    }, 500);
}
//取消
function cancel() {
    $("#cancel").click(function() {
        alert("1");
        $("#select-page").show();
        $("#edit-page").hide();
    })
}
//保存
function save() {
    var input_value = $("form input").val();
    var select_value = $("form select").val();
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
