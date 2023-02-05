function onCheck() {
    var checkedValue = null;
    var inputElements = document.getElementsByClassName('accept-me');
    //console.log(inputElements[0].value);
    if (inputElements[0].checked) {
        //console.log(inputElements[0].value);
        document.getElementById('sign-up').disabled = false;
    }
    else {
        document.getElementById('sign-up').disabled = true;
    }
}