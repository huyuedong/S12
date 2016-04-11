/**
 * Created by qimi on 2016/4/11.
 */
function showPic(which_pic) {
    //找到点击的图片的链接
    var source = which_pic.getAttribute("href");
    //找到图片占位符赋值给place_holder
    var place_holder = document.getElementById("placeholder");
    //用图片链接去替换图片占位符的链接
    place_holder.setAttribute("src", source);
    //找到图片的title赋值给text
    var text = which_pic.getAttribute("title");
    //找到图片描述的节点赋值给description
    var description = document.getElementById("description");
    //将text赋值给图片描述节点第一个子节点的属性
    description.firstChild.nodeValue = text;
}

function countBodyChildren() {
    var body_element = document.getElementsByTagName("body")[0];
    //alert (body_element.childNodes.length);
}
window.onload = countBodyChildren();