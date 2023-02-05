function searchCand() {
    var input, filter;
    input = document.getElementById("searchCand");
    filter = input.value.toUpperCase();
    cards = document.getElementsByClassName("card")
    titles = document.getElementsByClassName("card-title");
    profile = document.getElementsByClassName("jobid");
    phone = document.getElementsByClassName("phone");

    // Loop through all list items, and hide those who don't match the search query
    for (i = 0; i < cards.length; i++) {
        a = titles[i];
        b = profile[i];
        c = phone[i];
        //console.log(a.innerHTML + " " + b.innerHTML);
        if (a.innerHTML.toUpperCase().indexOf(filter) > -1 || b.innerHTML.toUpperCase().indexOf(filter) > -1 || c.innerHTML.toUpperCase().indexOf(filter) > -1) {
            cards[i].style.display = "";
        } else {    
            cards[i].style.display = "none";
        }
    }
}