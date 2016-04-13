/**
 * Created by liwenzhou on 2016/4/13.
 */
function prepareSlideshow () {
    if (!document.createElement) return false;
    if (!document.getElementById) return false;
    if (!document.getElementsByTagName) return false;
    if (!document.getElementById("linklist")) return false;
    //创建div元素
    var slideshow = document.createElement("div");
    slideshow.setAttribute("id", "slideshow");
    //创建img元素
    var preview = document.createElement("img");
    preview.setAttribute("src","img/topic1.png");
    preview.setAttribute("alt","building blocks of web design");
    preview.setAttribute("id","preview");
    //把创建的img元素添加到div下
    slideshow.appendChild(preview);
    //找到id为linklist的元素节点
    var link = document.getElementById("linklist");
    //把创建的div添加到link后面
    insertAfter(slideshow, link);
    //if (!document.getElementById("preview")) return false;
    //var preview = document.getElementById("preview");
    //preview.style.position = "absolute";
    //preview.style.left = "0px";
    //preview.style.top = "0px";
    ////取得列表中的所有元素
    //var link = document.getElementById("linklist");
    var links = link.getElementsByTagName("a");
    links[0].onmouseover = function() {
        moveElement("preview", -100, 0, 10);
    };
    links[1].onmouseover = function() {
        moveElement("preview", -200, 0, 10);
    };
    links[2].onmouseover = function() {
        moveElement("preview", -300, 0, 10);
    };
    for (var i=0;i<links.length;i++) {
        links[i].onmouseout = function() {
            moveElement("preview", 0, 0, 10);
        }
    }
}
addLoadEvent(prepareSlideshow);