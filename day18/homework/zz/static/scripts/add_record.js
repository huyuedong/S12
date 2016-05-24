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
            swal({
                title: "确定要提交吗？",
                //text: "Submit to run ajax request",
                type: "info",
                showCancelButton: true,
                closeOnConfirm: false,
                showLoaderOnConfirm: true
            },

                ajax_submit(data)
                //function(){
                //    setTimeout(function(){
                //        var data = $("#add-form").serializeArray();
                //        if (ajax_submit(data)) {
                //            swal("添加成功！", "success")
                //        } else {
                //            swal("添加失败！", "error")
                //        }
                //    }, 2000);
                //}
            );
        }
        //禁用默认的submit
        return false;
    })
});

