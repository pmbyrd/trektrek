console.log("search.js loaded successfully")
$(document).ready(function() {
    $("#search-form").on("submit", function(event) {
        event.preventDefault();
        let search = $("#search").val();
        console.log(search);
        
    });
});