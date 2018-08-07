$( document ).ready(function(){

    let search_values;
    $.getJSON('/suggestions', function(result) {
        search_values = result;
      $("#autocomplete").autocomplete({
         minLength:1,   
         delay:100,   
         source: search_values
      });
      });
   });



// <script>
// // Displays search results underneath the search form w/out reloading!
// $(document).ready(function() {
//     document.getElementById("search").onclick = function (event) {
//         event.preventDefault();
//         var data= $('form').serialize(); //serializes form data for use
//         console.log(data)
//         $.post('/kartitem', data, function (result){
//             $("#results").html(result);
//             //Add failure clauses for no keyword && no search by values!
//         });
//         //on click, after loading of results, scrollls to top of #results div
//         $('html, body').animate({
//         scrollTop: $("#results").offset().top}, 1500);
//     };
// });
// </script>