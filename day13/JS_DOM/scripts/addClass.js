/**
 * Created by liwenzhou on 2016/4/13.
 */
//为元素节点追加class属性
function addClass(element, value) {
    if (!element.className) {
        element.className = value
    } else {
        newClassName = element.className;
        newClassName += " ";
        newClassName += value;
        element.className = newClassName;
    }
}