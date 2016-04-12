/**
 * Created by liwenzhou on 2016/4/12.
 */
function prepareGallery() {
    //检查浏览器是否支持getElementById方法
    if (!document.getElementById) return false;
    //检查浏览器是否支持getElementsByTagName方法
    if (!document.getElementsByTagName) return false;
    //检查文档中是否存在id为imagegallery的节点
    if (!document.getElementById("imagegallery")) return false;
    //获取到id为imagegallery的文档节点
    var gallery = document.getElementById("imagegallery");
    //找到所有的a标签
    var links = gallery.getElementsByTagName("a");
    //遍历a标签，给其添加action
    for (var i=0;i<links.length;i++) {
        links[i].onclick = function() {
            //如果showPic返回true表明运行成功此时就应该取消a标签的默认行为
            return showPic(this) ? false : true;
        };
        //把onclick事件的所有功能赋给onkeypress事件，但是此处不推荐增加onkeypress事件。onclick也支持键盘触发
        //links[i].onkeypress = links[i].onclick;
    }
}

function showPic(which_pic) {
    //检查是否存在id值为placeholder的元素
    if (!document.getElementById("placeholder")) return false;
    //找到点击的图片的链接
    var source = which_pic.getAttribute("href");
    //找到图片占位符赋值给place_holder
    var place_holder = document.getElementById("placeholder");
    //检查placeholder的img元素是否存在
    if (place_holder.nodeName != "IMG") return false;
    //用图片链接去替换图片占位符的链接
    place_holder.setAttribute("src", source);
    //如果有description，就在指定位置显示出来
    if (document.getElementById("description")) {
        //找到图片的title赋值给text,没有就将text设置为空字符串
        var text = which_pic.getAttribute("title") ? which_pic.getAttribute("title") : "";
        //找到图片描述的节点赋值给description
        var description = document.getElementById("description");
        //如果description的第一个子节点的属性是文本
        if (description.firstChild.nodeType == 3) {
            //将text赋值给图片描述节点第一个子节点的属性
            description.firstChild.nodeValue = text;
        }
    }
    return true;
}

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

addLoadEvent(prepareGallery);