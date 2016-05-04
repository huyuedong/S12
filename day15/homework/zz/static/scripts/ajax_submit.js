/**
 * Created by liwenzhou on 2016/5/3.
 */

//提示指定错误信息
function errorMessage(container, msg) {
    //确保同时只出现一个错误提示消息
    if (!container.parent().attr("hasError") || container.parent().attr("hasError") == "false") {
        var temp = '<div class="my-alert alert-danger" role="alert">'+msg+'</div>';
        container.parent().after(temp);
        //container.after(temp);
        container.parent().attr("hasError", "true");
        //container.attr("hasError", "true");
    }
    //闪烁出现错误的输入框
    shake(container, "red", 2);
    //该输入框获得焦点之后去掉错误提示
    container.focus(function() {
        container.parent().next(".my-alert").remove();
        //container.next(".my-alert").remove();
        //container.attr("hasError", "false");
        container.parent().attr("hasError", "false");
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

function get_data() {
    var data = Object();
    $(arg).find("input").each(function(){
        var name = $(this).prop("name");
        data[name] = $(this).val();
    });
    return data;
}


function check(arg) {
    var name_map = {
        email: "邮箱",
        password: "密码",
        repeat_password: "确认密码",
        hostname: "主机名",
        ip: "IP地址",
        port: "端口"
    };
    //从参数下面找到submit标签，绑定一个onclick事件
    //$(arg).find(":submit").click(function() {
        var flag = true;
        //找到form下的所有class为input-group的input标签
        $(arg).find("input").each(function() {
            //获取到内容
            var name = $(this).prop("name");
            var name_str = name_map[name];
            var value = $(this).val();
            //如果input为空
            if (!value || value.trim() == "") {
                errorMessage($(this),name_str+"不能为空");
                flag = false;
            }
            //如果是邮箱，就按照邮箱的规则匹配值
            if (name == "email") {
                var re_mail = /^([a-z.0-9]{1,26})@([a-z.0-9]{1,20})(.[a-z0-9]{1,8})$/;
                if (!re_mail.test(value)) {
                    flag = false;
                    errorMessage($(this), name_str+"无效");
                }
            }
            if (name == "password") {
                if (value.length < 6) {
                    flag = false;
                    errorMessage($(this), name_str+"必须大于6位");
                }
            }
            //判断主机名
            if (name == "hostname") {
                if (value.length > 255) {
                    flag = false;
                    errorMessage($(this), name_str+"过长");
                }
            }
            //判断IP
            if (name == "ip") {
                var re_ip = /^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$/;
                if (!re_ip.test(value)) {
                    flag = false;
                    errorMessage($(this), name_str+"无效");
                }
            }
            //判断端口
            if (name == "port") {
                var re_port = /^(\d)+$/;
                if (re_port.test(value)) {
                    value = parseInt(value);
                    if (value > 65535) {
                        flag = false;
                        errorMessage($(this), name_str+"无效");
                    }
                } else {
                    flag = false;
                    errorMessage($(this), name_str+"必须为数字");
                }
            }
        });
        return flag;
    //})
}

//function ajax_submit(submit_data) {
function ajax_submit() {
    $.ajax({
        url: "/ajax_add/",
        type: "POST",
        tradition: true,
        //data: {data: JSON.stringify(submit_data)},
        data: {"hostname": "h1", "ip": "1.1.1.1"},
        success: function(arg) {
            var callback_data = $.parseJSON(arg);
            if (callback_data.status) {
                swal("添加成功！", "success")
            } else {
                swal("添加失败！", "error")
            }
        }
    })
}
function add_record(arg) {
    $(":submit").click(function () {
        alert(arg);
        var flag = check(arg);
        console.log(flag);
        console.log(typeof(flag));
        alert(flag);
        alert(typeof(flag));
        if (flag) {
            console.log(1);
            alert("获取数据");

            //var da = get_data(arg);
            //console.log(da);
            //alert(da);
            ajax_submit();
        } else {
            alert("错误");
            return false;
        }
    });
    return false;
}


$(document).ready(function() {
   add_record("#add-form");
});