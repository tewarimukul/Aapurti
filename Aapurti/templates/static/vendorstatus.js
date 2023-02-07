window.onload = function() {
    showVendorMsg();
  };

function showVendorMsg() {
    applength = document.getElementById("app-pending-cards").children.length;
    applength02 = document.getElementById("app-approved-cards").children.length;

    if(applength == 0) {
        document.getElementById("empty-Vendors").style.display = "block";
    }
    else {
        document.getElementById("empty-Vendors").style.display = "none";
    }

    if(applength02 == 0) {
        document.getElementById("approved-Vendors").style.display = "block";
    }
    else {
        document.getElementById("approved-Vendors").style.display = "none";
    }
}