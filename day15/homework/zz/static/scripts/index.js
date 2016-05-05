/**
 * Created by liwenzhou on 2016/4/13.
 */

STATUS = [
    {"id": 1, "value": "在线"},
    {"id": 2, "value": "下线"}
];
GROUP = [
    {"id": 1, "value": "开发"},
    {"id": 2, "value": "测试"},
    {"id": 3, "value": "运维"}
];
SERVICE = [
    {"id": 1, "value": "tomcat"},
    {"id": 2, "value": "MySQL"},
    {"id": 3, "value": "Nginx"},
    {"id": 4, "value": "FTP"}
];

//退出行的编辑状态
function outRowEdit(ths) {
    ths.children().each(function() {
        //判断是不是可编辑的元素
        if ($(this).attr("edit") == "true") {
            var text = $(this).children(":first").val();
            $(this).html(text);
        }
    })
}
//进入行的编辑状态
function inRowEdit(ths) {
    ths.children().each(function() {
        //判断是不是可编辑的元素
        if ($(this).attr("edit") == "true") {
            //处理select标签
            if ($(this).attr("edit-type") == "select") {
                //获得预先定义的option选项
                var optionArray = window[$(this).attr("option-key")];
                //console.log(optionArray);
                //找到当前选中的option项
                var selected_option = $(this).text();
                console.log(selected_option);
                var options = "";
                //遍历取出option
                $.each(optionArray, function(index, value) {
                    //将转换后的select中选中之前的option项
                    if (selected_option == value.value) {
                        options += "<option selected='selected'>" + value.value + "</option>";
                    } else {
                        options += "<option>" + value.value + "</option>";
                    }
                });
                var tmp = "<select onchange='batchSelect(this)'>" + options + "</select>";
                $(this).html(tmp);
            } else {
                var text = $(this).text();
                var tmp = "<input type='text' value='" + text + "' />";
                $(this).html(tmp);
            }
        }
    })
}
//全选
function checkAll() {
    $("#check-all").click(function() {
        $("tbody").find("input:checkbox").each(function() {
            if ($(this).prop("checked")) {

            } else {
                $(this).prop("checked", true);
                //判断当前的模式
                var is_edit = $("#edit").hasClass("editing");
                if (is_edit) {
                    //向上找到tr标签
                    var tr = $(this).parent().parent();
                    //遍历tr的子元素
                    inRowEdit(tr);
                }
            }
        });
    });
}
//反选
function invertCheck() {
    $("#invert-check").click(function() {
        var is_edit = $("#edit").hasClass("editing");
        $("tbody").find("input:checkbox").each(function() {
            //找到行
            var tr = $(this).parent().parent();
            if ($(this).prop("checked")) {
                $(this).prop("checked", false);
                if (is_edit) {
                    outRowEdit(tr);
                }
            } else {
                $(this).prop("checked", true);
                if (is_edit) {
                    //遍历tr的子元素
                    inRowEdit(tr);
                }
            }
        })
    })
}
//进入编辑模式
function editRecord() {
    $("#edit").click(function doEdit() {
        if ($(this).hasClass("editing")) {
            $(this).removeClass("btn-primary editing");
            $(this).html('<span class="fa fa-pencil fa-fw"></span>进入编辑模式');
            //遍历查找checkbox
            $("tbody").find("input:checkbox").each(function() {
                if ($(this).prop("checked")) {
                    var tr = $(this).parent().parent();
                    //遍历tr的子元素
                    outRowEdit(tr);
                }
            })
        } else {
            $(this).addClass("btn-primary editing");
            $(this).html('<span class="fa fa-pencil fa-fw"></span>退出编辑模式');
            //遍历查找checkbox
            $("tbody").find("input:checkbox").each(function() {
                if ($(this).prop("checked")) {
                    var tr = $(this).parent().parent();
                    //遍历tr的子元素
                    inRowEdit(tr);
                }
            })
        }
    })
}
//取消
function cancel() {
    $("#cancel").click(function() {
        var edit_button = $("#edit");
        $("tbody").find("input:checkbox").each(function() {
            if ($(this).prop("checked")) {
                $(this).prop("checked", false);
                var is_edit = edit_button.hasClass("editing");
                if (is_edit) {
                    var tr = $(this).parent().parent();
                    outRowEdit(tr);
                }
            }
        });
        edit_button.removeClass("btn-primary editing");
        edit_button.html('<span class="fa fa-pencil fa-fw"></span>进入编辑模式');
    })
}
//编辑模式下单选编辑
function optionClick() {
    $("tbody").find("input:checkbox").click(function() {
        var tr = $(this).parent().parent();
        if ($("#edit").hasClass("editing")) {
            if ($(this).prop("checked")) {
                inRowEdit(tr);
            } else {
                outRowEdit(tr);
            }
        }
    })
}
//定义一个判断Ctrl是否按下的flag
window.CTRLPRESS = false;

//按下Ctrl则把CTRLPRESS置为true
window.onkeydown = function(event) {
    if (event && event.keyCode == 17) {
        window.CTRLPRESS = true;
    }
};
//松开Ctrl则把CTRLPRESS置为false
window.onkeyup = function(event) {
    if (event && event.keyCode == 17) {
        window.CTRLPRESS = false;
    }
};
//批量操作
function batchSelect(ths) {
    if (window.CTRLPRESS) {
        //window.CTRLPRESS = false;
        //找到td在tr的索引位置
        var cur_index = $(ths).parent().index();
        //找到当前option值
        var cur_value = $(ths).val();
        //找到当前位置之后所有的tr中找出所有checkbox被选中的
        $(ths).parent().parent().nextAll().find("td input[type='checkbox']:checked").each(function() {
            //将找出来的input的上上层的tr中找到与索引位相同的children(td)，将其children(select)的值修改为相同的。
            $(this).parent().parent().children().eq(cur_index).children().val(cur_value);
        })
    }
}
//保存


//推荐方法
$(document).ready(function() {
    checkAll();
    invertCheck();
    editRecord();
    cancel();
    optionClick();
});
