/**
 * Created by liwenzhou on 2016/4/13.
 */
function getNextElement (node) {
    if (node.nodeType == 1) {
        return node;
    }
    if (node.nextSibling) {
        return getNextElement(node.nextSibling);
    }
    return null;
}
//对函数进行抽象：为指定tag的下一个元素节点增加className:theClass
function styleHeaderSibling (tag, theClass) {
    if (!document.getElementsByTagName) return false;
    var headers = document.getElementsByTagName(tag);
    var elem;
    for (var i=0;i<headers.length;i++) {
        //找到下一个元素节点
        elem = getNextElement(headers[i].nextSibling);
        //为该元素赋予样式
        addClass(elem, theClass);
        //elem.style.fontWeight = "bold";
        //elem.style.fontSize = "1.2em";
    }
}

//addLoadEvent(styleHeaderSibling);
addLoadEvent(function() {
    styleHeaderSibling("h1", "intro");
});