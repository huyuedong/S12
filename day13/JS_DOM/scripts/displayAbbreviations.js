/**
 * Created by qimi on 2016/4/12.
 */
function displayAbbreviations () {
    if (!document.getElementsByTagName) return false;
    if (!document.createElement) return false;
    if (!document.createTextNode) return false;
    //找到所有缩略词
    var abbreviations = document.getElementsByTagName("abbr");
    if (abbreviations.length < 1) return false;
    var defs = [];
    //遍历缩略词
    for (var i=0;i<abbreviations.length;i++) {
        //如果没有abbr属性就跳出本次循环
        if (abbreviations[i].childNodes.length < 1) continue;
        var definition = abbreviations[i].getAttribute("title");
        var key = abbreviations[i].lastChild.nodeValue;
        defs[key] = definition
    }
    //创建定义列表
    var dlist = document.createElement("dl");
    //遍历定义
    for (key in defs) {
        var definition = defs[key];
        //创建定义标题
        var dtitle = document.createElement("dt");
        var dtitle_text = document.createTextNode(key);
        dtitle.appendChild(dtitle_text);
        //创建定义描述
        var ddesc = document.createElement("dd");
        var ddesc_text = document.createTextNode(definition);
        ddesc.appendChild(ddesc_text);
        //把它们添加到定义列表
        dlist.appendChild(dtitle);
        dlist.appendChild(ddesc);
        if (dlist.childNodes.length < 1) return false;
    }
    //创建标题
    var header = document.createElement("h2");
    var header_text = document.createTextNode("Abbreviations");
    header.appendChild(header_text);
    //把标题添加到页面主体
    document.body.appendChild(header);
    //把定义列表添加到页面主体
    document.body.appendChild(dlist);
}
function displayCitations () {
    if (!document.getElementsByTagName) return false;
    if (!document.createElement) return false;
    if (!document.createTextNode) return false;
    //取得所有引用
    var quotes = document.getElementsByTagName("blockquote");
    //遍历引用
    for (var i=0;i<quotes.length;i++) {
        //如果没有cita属性，跳出本次循环
        if (!quotes[i].getAttribute("cite")) {
            continue;
        }
        //保存cita属性
        var url = quotes[i].getAttribute("cite");
        //取得引用中的所有元素节点
        var quoteChildren = quotes[i].getElementsByTagName("*");
        //如果没有元素节点，退出本次循环
        if (quoteChildren.length < 1) continue;
        //得到引用中的最后一个元素节点
        var elem = quoteChildren[quoteChildren.length - 1];
        //创建标记
        var link = document.createElement("a");
        var linl_text = document.createTextNode("source");
        link.appendChild(linl_text);
        link.setAttribute("href", url);
        var superscript = document.createElement("sup");
        superscript.appendChild(link);
        //把标记添加到引用中的最后一个元素节点
        elem.appendChild(superscript);
    }
}
function displayAccessKeys () {
    if (!document.getElementsByTagName) return false;
    if (!document.createElement) return false;
    if (!document.createTextNode) return false;
    var links = document.getElementsByTagName("a");
    var akeys = new Array();
    for (var i=0;i<links.length;i++) {
        var current_link = links[i];
        if (!current_link.getAttribute("accesskey")) continue;
        //得到快捷键
        var key = current_link.getAttribute("accesskey");
        //得到链接文本
        var text = current_link.lastChild.nodeValue;
        //添加到数组
        akeys[key] = text;
    }
    //创建列表
    var list = document.createElement("ul");
    for (key in akeys) {
        var text = akeys[key];
        //创建列表项的字符串
        var str = key + ": " + text;
        //创建列表项
        var item = document.createElement("li");
        var item_text = document.createTextNode(str);
        item.appendChild(item_text);
        //把列表项添加到列表中
        list.appendChild(item);
    }
    //创建标题
    var header = document.createElement("h3");
    var heafer_text = document.createTextNode("AccessKeys");
    header.appendChild(heafer_text);
    //把标题添加到页面主体
    document.body.appendChild(header);
    document.body.appendChild(list);
}

addLoadEvent(displayAbbreviations);
addLoadEvent(displayCitations);
addLoadEvent(displayAccessKeys);