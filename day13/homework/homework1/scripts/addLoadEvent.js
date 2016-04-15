/**
 * Created by liwenzhou on 2016/4/12.
 */
//addLoadEvent函数
function addLoadEvent(func) {
    var old_onload = window.onload;
    if (typeof old_onload != "function") {
        window.onload = func;
    }else {
        window.onload = function () {
            old_onload();
            func()
        }
    }
}