/**
 * Created by qimi on 2016/4/9.
 */

//函数声明
function func1(arg){
    console.log(arg);
    return "alex";
}

var ret = func1("1111");
console.log(ret);

//匿名函数
var f = function(arg){
    console.log("1111", arg);
};

f("2222");

//自执行函数
(function (arg){
    console.log(arg);
})("123");


//面向对象
function Foo(name, age){
    this.Name=name;
    this.Age=age;
    this.Func=function(arg){
        return this.Name + arg;
    }
}

var obj = new Foo("alex", 18);
var ret1 = obj.Func("humor");
console.log(ret1);
