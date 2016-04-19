/**
 * Created by qimi on 2016/4/17.
 */
(function(arg) {
    //提示指定错误信息
    function errorMessage(container, msg) {
        //确保同时只出现一个错误提示消息
        if (container.parent().attr("hasError") == "false") {
            var temp = "<div  id='type-error'>"+msg+"</div>";
            container.after(temp);
            container.parent().attr("hasError", "true");
        }
        //闪烁出现错误的输入框
        shake(container, "red", 2);
        //该输入框获得焦点之后去掉错误提示
        container.focus(function() {
            container.siblings().remove();
            container.parent().attr("hasError", "false");
        })
    }
    //提示不能为空
    function emptyMessage(container, msg) {
        //确保同时只出现一个错误提示消息
        if (container.parent().attr("hasError") == "false") {
            var temp = "<div id='empty-error'>"+msg+"</div>";
            container.after(temp);
            container.parent().attr("hasError", "true");
        }
        //闪烁出现错误的输入框
        shake(container, "red", 2);
        //获得焦点之后去掉错误提示
        container.focus(function() {
            container.siblings().remove();
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
    //检测输入有效性的扩展
    arg.extend({
        "checkValidity": function(form) {
            $(form).find(":submit").click(function() {
                var flag = true;
                $(form).find(":text").each(function() {
                    var name = $(this).parent().text();
                    //去掉冒号和多余的空格
                    name = name.replace(/[：,　]/g,"").trim();
                    var value = $(this).val();
                    //如果input为空
                    if (!value || value.trim() == "") {
                        emptyMessage($(this),name+"不能为空");
                        flag = false;
                        return false;
                    }
                    //判断主机名
                    var hostname = $(this).attr("hostname");
                    if (hostname) {
                        if (hostname.length > 255) {
                            flag = false;
                            errorMessage($(this), name+"过长");
                            return false;
                        }
                    }
                    //判断IP
                    var ip = $(this).attr("ip");
                    if (ip) {
                        var re_ip = /^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$/;
                        if (!re_ip.test(value)) {
                            flag = false;
                            errorMessage($(this), name+"无效");
                            return false;
                        }
                    }
                    //判断端口
                    var port = $(this).attr("port");
                    if (port) {
                        var re_port = /^(\d)+$/;
                        if (re_port.test(value)) {
                            value = parseInt(value);
                            if (value > 65535) {
                                flag = false;
                                errorMessage($(this), name+"无效");
                                return false;
                            }
                        } else {
                            flag = false;
                            errorMessage($(this), name+"必须为数字");
                            return false;
                        }
                    }
                });
                return flag;
            })
        }
    })
})($);