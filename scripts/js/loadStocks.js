// ----- NOT PART OF APP ----
// reference code for making http request via AJAX instead of Angular's $http service
$(document).ready(function(){

 $.ajax({
      type:'get',
      url:'/getStocks',
      cache:false,
      async:'asynchronous',
      dataType:'json',
      success: function(data) {
      	var trendingStocks = data;
        console.log(JSON.stringify(data))
      },
      error: function(request, status, error) {
        console.log("Error: " + error)
      }
   });
});

// ---------- NOT PART OF APP, JUST HERE FOR REFERENCE -----------
