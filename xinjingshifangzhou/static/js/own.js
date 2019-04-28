

function checkConcat() {
    var words = document.getElementById("words").value;
    var phone = document.getElementById('phone').value;
    re = /^1[34578]\d{9}$/;

    if (!re.test(phone) && !words) {
        alert("手机号码有误请重填！留言为空");
    } else if (!re.test(phone)) {
        alert("手机号码有误请重填!");
    } else if (!words) {
        alert("留言为空");
    }
}