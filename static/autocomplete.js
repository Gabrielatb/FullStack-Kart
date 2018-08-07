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


