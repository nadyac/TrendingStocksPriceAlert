$(document).ready(function(){

 $.ajax({
      type:'get',
      url:'/getStocks',
      cache:false,
      async:'asynchronous',
      dataType:'json',
      success: function(data) {
        console.log(JSON.stringify(data))
      },
      error: function(request, status, error) {
        console.log("Error: " + error)
      }
   });
});
