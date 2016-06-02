/**
 * Created by liwenzhou on 2016/6/1.
 */

function test() {
    console.log(1);
}

// 给用到日期的input标签添加datetimepicker
function addDatePiker() {
    $("#id_start_date, #id_graduate_date").each(function() {
        $(this).parent().addClass("date form_date");
        $(this).datetimepicker({
            format:"yyyy-mm-dd",
            weekStart: 1,
            todayBtn:  1,
            autoclose: 1,
            todayHighlight: 1,
            startView: 2,
            minView: 2,
            forceParse: 0
        })
    });
}
$(function() {
    test();
    addDatePiker();
});