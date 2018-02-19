//Define the TrendingStocks app which will contain all controllers and services for our app
var app = angular.module('myApp',[]);

// Define the controller on the trendingStocks module. The controller will be responsible
// for handling all the logic for a portion of the app that it controls.
// This app only has one controller, stocksListController.
app.controller('stocksListController', function stocksListController($scope,$http){
	//make get request to localhost:8000/getStocks. Server will respond with JSON object with the stocks
	$scope.phoneNumber="";
	$scope.setPhoneNumber = function(number){
		$scope.phoneNumber = number;
		console.log("set phone number to " + $scope.phoneNumber)
	}
	$http.get("/getStocks") 
	    .then(function(response) {
	        $scope.stocks = response.data; // Assign $scope variable stocks to the stocks JSON so that  
	    });								   // it can be passed to the view for the user to see

	$scope.setAlert = function(targetSymbol, phoneNumber){
		config = {
			data:targetSymbol,
			params:{
				alertSymbol: targetSymbol,
				toNumber:phoneNumber
			}
		}

		if($scope.phoneNumber != "" && typeof $scope.phoneNumber != 'undefined'){
			$http.get("/setAlert",config)
		    .then(function(response) {
		        console.log(response);
		    });
		} else{
			alert("Please submit a phone number.")
		}
	}
});