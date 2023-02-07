//document.getElementById('main-body').addEventListener('click', closeNav);
//document.getElementById('main-body').addEventListener('click', closeUser);

function openNav() {
  document.getElementById("mySidenav").style.width = "265px";
  //document.getElementById("main-body").style.marginLeft = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  //document.getElementById("main-body").style.marginLeft = "0";
}

function openUser() {
  document.getElementById("userSidenav").style.height = "269px";
  document.getElementById("userSidenav").style.width = "237px";
  //document.getElementById("main-body").style.overflowY = "hidden";
}

function closeUser() {
  document.getElementById("userSidenav").style.height = "0";
  document.getElementById("userSidenav").style.width = "0";
  document.getElementById("main-body").style.overflowY = "scroll";
}

document.getElementById('main-body').onclick = function(e) {
  var element = document.getElementById('mySidenav'),
    style = window.getComputedStyle(element),
    width = style.getPropertyValue('width'),
    height = style.getPropertyValue('height');
    //console.log("Inside Event" + width);
    if(width !== '0px') {
      //console.log("Inside IF");
      closeNav();
    }

    element = document.getElementById('userSidenav'),
    style = window.getComputedStyle(element),
    width = style.getPropertyValue('width'),
    height = style.getPropertyValue('height');
    //console.log("Inside Event" + width);
    if(width !== '0px') {
      //console.log("Inside IF");
      closeUser();
    }
}

function myFunction() {
  alert("Clicked !");
  document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function (event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}