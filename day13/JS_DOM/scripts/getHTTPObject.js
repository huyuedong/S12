/**
 * Created by liwenzhou on 2016/4/12.
 */
//function getHTTPObject() {
//    if (typeof XMLHttpRequest == "undefined") {
//        XMLHttpRequest = function () {
//            try {
//                return new ActiveXObject("Msxml2.XMLHTTP.6.0");
//            }
//            catch (e) {
//            }
//            try {
//                return new ActiveXObject("Microsoft.XMLHTTP");
//            }
//            catch (e) {
//            }
//            try {
//                return new ActiveXObject("Msxml2.XMLHTTP");
//            }
//            catch (e) {
//            }
//            return false;
//    };
//    return new XMLHttpRequest();
//}
//
//function getHTTPObject() {
//    try {return new XMLHttpRequest();}
//    catch (e) {}
//    try {return new ActiveXObject("Msxml2.XMLHTTP");}
//    catch (e) {}
//    try {return new ActiveXObject("Microsoft.XMLHTTP");}
//    catch (e) {}
//    return false;
//}
function getHTTPObject() {
    var xmlHttpObject = null;
    try { xmlHttpObject = new XMLHttpRequest();}
    catch (e) {}
    try { xmlHttpObject = new ActiveXObject("Msxml2.XMLHTTP");}
    catch (e) {}
    try { xmlHttpObject = new ActiveXObject("Microsoft.XMLHTTP");}
    catch (e) {}
    return xmlHttpObject;
}