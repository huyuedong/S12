/**
 * Created by liwenzhou on 2016/5/3.
 */

function ajax_submit(submit_data) {
    $.ajax({
        url: "/ajax_add/",
        type: "POST",
        tradition: true,
        data: submit_data,
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

$(document).ready(function() {
    $(":submit").click(function(){
        if($.checkValidity("#add-form")){
            var data = $("#add-form").serializeArray();
            ajax_submit(data);
        }
        //禁用默认的submit
        return false;
    })
});