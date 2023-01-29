function hideBtn(x) {
    console.log("hoverin");
    document.getElementById(x).innerHTML = "&gt;";
}

function showBtn(x) {
    console.log("hoverout");
    document.getElementById(x).innerHTML = "&gt;&nbsp;&nbsp;&nbsp;Explore";
}