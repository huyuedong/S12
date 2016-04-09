/**
 * Created by qimi on 2016/4/9.
 */

var num = 2;

//循环

console.log("While循环：");
while (num<10){
    num += 1;
    if (num == 5){
        continue;
    }
    console.log(num);
    if (num == 7){
    break;
    }
}


//条件判断
console.log("if条件判断:");
if(num == 1){
    console.log("num=1")
}else if (num == 2){
    console.log("num=2")
}else if (num == 3){
    console.log("num=3")
}else {
    console.log("num unknow!")
}

//switch判断
console.log("switch判断：");
switch (num){
    case 1:
        console.log("num=1");
        break;
    case 2:
        console.log("num=2");
        break;
    case 3:
        console.log("num=3");
        break;
    default:
        console.log("unknow num!");

}

//异常处理
console.log("异常处理:");
try{
    console.log(num=2);
}catch(e){
    console.log(e)
}finally {
    console.log("finally do something...")
}

