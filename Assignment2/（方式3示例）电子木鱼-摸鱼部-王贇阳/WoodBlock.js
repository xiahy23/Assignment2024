// 更改鼠标样式
document.body.style.cursor = "url(./res/cursor.ico),auto";

// 通过id获取HTML元素
const woodBlock = document.getElementById("WoodBlock");
const audio = document.getElementById("audio");
const alt_audio = document.getElementById("alt_audio");

// 要用到的神奇妙妙变量
let imgWidth = woodBlock.style.width;
let imgHeight = woodBlock.style.height;
let mobile = false;
let cnt = 0;

// 页面加载完毕后执行
// 适配移动端，并监听鼠标事件
window.onload = function () {
    // 小屏幕时缩小图片大小
    let width = window.innerWidth;
    let height = window.innerHeight;
    if (width < 500) {
        imgWidth = width - 180;
        imgHeight = (width - 180) * 0.76;
        woodBlock.style.width = imgWidth + "px";
        woodBlock.style.height = imgHeight + "px";
        mobile = true;
    }
    else {
        woodBlock.style.width = "435px";
        woodBlock.style.height = "330px";
    }

    // 鼠标或手指进入和离开时改变图片大小
    woodBlock.onmouseenter = !mobile ? function (event) {
        event.preventDefault();
        woodBlock.style.scale = "1.05";
    } : null;
    woodBlock.onmouseleave = !mobile ? function (event) {
        event.preventDefault();
        woodBlock.style.scale = "1";
    } : null;

    // 鼠标或手指点击时播放音效
    !mobile ? woodBlock.onmousedown = function (event) {
        event.preventDefault();
        woodBlock.style.scale = "1.0";
        woodBlock.onmouseup = function (event) {
            event.preventDefault();
            woodBlock.style.scale = "1.05";
        };
        audio.currentTime = 0;
        audio.play();
        MeritsPlus();
    } : woodBlock.ontouchstart = function (event) {
        event.preventDefault();
        woodBlock.style.scale = "1.0";
        audio.currentTime = 0;
        audio.play();
        MeritsPlus();
        woodBlock.ontouchend = function (event) {
            event.preventDefault();
            woodBlock.style.scale = "1.05";
        };
    };

    // 这个语句可以在控制台输出一段文字！很适合用来调试！
    // 快按F12打开控制台看看吧
    console.log("页面加载完毕");
};

// 功德+1
function MeritsPlus() {
    // 创建一个元素，显示功德+1
    let merits = document.createElement("p");
    merits.innerHTML = "功德+1";
    // 设置元素样式
    merits.style.position = "absolute";
    merits.style.top = !mobile ? "calc(50% - 180px)" : "calc(50% - " + (imgHeight / 2 + 75) + "px)";
    merits.style.left = !mobile ? "calc(50% + 180px)" : "calc(50% + " + (imgWidth / 2 - 15) + "px)";
    merits.style.fontSize = "24px";
    merits.style.color = "white";
    merits.style.fontWeight = "bold";
    // 添加元素到页面
    document.getElementById("main").appendChild(merits);
    // 功德+1
    cnt++;
    // 更新页面显示的总功德值
    document.getElementById("cnt").innerHTML = "功德：" + cnt;
    // 移动功德+1元素
    let t = 0;
    // 每16ms更新一次样式
    setInterval(() => {
        merits.style.opacity = 1 - 0.02 * t;
        merits.style.top = !mobile ? "calc(50% - 180px - " + 2 * t + "px)" : "calc(50% - " + (imgHeight / 2 + 75) + "px - " + 2 * t + "px)";
        t++;
    }, 16);
    // 2秒后删除功德+1元素
    setTimeout(() => {
        document.getElementById("main").removeChild(merits);
    }, 2000);
}

// “设置”按钮功能
const setting = document.getElementById("setting");
setting.onclick = function (event) {
    event.preventDefault();
    alert("功能尚未开放");
}
