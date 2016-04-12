/**
 * Created by liwenzhou on 2016/4/12.
 */
function creatP() {
    var para = document.createElement("p");
    var text = document.createTextNode("This is ");
    var emphasis = document.createElement("em");
    var test2 = document.createTextNode("my");
    var text3 = document.createTextNode(" contens.");
    para.appendChild(text);
    emphasis.appendChild(test2);
    para.appendChild(emphasis);
    para.appendChild(text3);
    var testdiv = document.getElementById("testdiv");
    testdiv.appendChild(para);
}

function addLoadEvent(func) {
    var old_onload = window.onload;
    if (typeof old_onload != "function") {
        window.onload = func;
    }else {
        window.onload = function () {
            old_onload();
            func();
        }
    }
}

addLoadEvent(creatP());