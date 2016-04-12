/**
 * Created by liwenzhou on 2016/4/12.
 */
//当window触发onload事件时，执行prepareLinks函数
window.onload = prepareLinks;
//定义prepareLinks函数
function prepareLinks() {
    //如果不支持浏览器不支持getElementsByTagName就退出
    if (!document.getElementsByTagName) return false;
    //找到所有的a标签
    var links = document.getElementsByTagName("a");
    //遍历a便签，如果class属性等于popup，就执行popUp方法
    for (var i = 0;i<links.length;i++) {
        if (links[i].getAttribute("class") == "popup") {
            links[i].onclick = function() {
                popUp(this.getAttribute("href"));
                return false;
            }
        }
    }
}
function popUp(winUrl) {
    window.open(winUrl, "popUp", "width=320,height=480");
}