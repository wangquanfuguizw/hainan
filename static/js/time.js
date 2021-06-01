let t = null
t = setTimeout(time, 1000)
function addZero(num) {
    if(num < 10) {
        num = '0' + num
    }
    return num
}
function time() {
    clearTimeout(t) //清除定时器
    dt = new Date()
    let y = dt.getFullYear()
    let mt = dt.getMonth() + 1
    let day = dt.getDate()
    let h = dt.getHours()
    let m = dt.getMinutes()
    let s = dt.getSeconds()
    let xin = dt.getDay()
    let weeks = new Array("星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六")
    let week = weeks[xin]
    mt = addZero(mt)
    day = addZero(day)
    h = addZero(h)
    m = addZero(m)
    s = addZero(s)
    document.querySelector(".showTime").innerHTML = "当前时间: " + y + "年" + mt + "月" + day + "日 "+ week + " " + h + "时" + m + "分" + s + "秒"
    t = setTimeout(time, 1000)
}