/**
 * Created by qimi on 2016/4/9.
 */

var num = 2;

//循环
console.log("For循环：");
nameArray = ["Alex", "John", "Eric"];

//一种循环数组的方法
for(var i=0;i<nameArray.length;i++){
    console.log(i);
    console.log(nameArray[i]);
}

//另外一种循环数组的方法
for(var inx in nameArray){
    console.log(inx);
    console.log(nameArray[inx]);
}


console.log("While循环：");
while (num<10){
    if (num == 5){
        num ++;
        continue;  //跳过本次循环
    }
    if (num == 7){
    break;  //跳出循环
    }
    console.log(num);
    num ++;
}


//条件判断
console.log("if条件判断:");
if(num == 1){
    console.log("num=1");
}else if (num == 2){
    console.log("num=2");
}else if (num == 3){
    console.log("num=3");
}else {
    console.log("unknown num!");
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
        console.log("unknown num!");

}

//异常处理
console.log("异常处理:");
try{
    console.log(num=2);
}catch(e){
    console.log(e);
}finally {
    console.log("finally do something...");
}

