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
	$http.get("/getStocks") // $http service makes request to /getStocks URI
	    .then(function(response) {
	        $scope.stocks = response.data; // Assign $scope variable stocks to the stocks JSON so that  
	    });								   // it can be passed to the view for the user to see

	 // Set alert for a desired stock symbol and set phone number where the 
	 // price alert notification will be sent.
	$scope.setAlert = function(targetSymbol, phoneNumber){
		config = {
			params:{
				alertSymbol: targetSymbol,
				toNumber:phoneNumber
			}
		}
		// Ensure that the request doesn't get send without a valid number 
		// this validation only checks for blank or undefined phone number. More
		// robust format checking should be done however. 
		if($scope.phoneNumber != "" && typeof $scope.phoneNumber != 'undefined'){
			$http.get("/setAlert",config) //make request to setAlert URI with the symbol and phone # as params
		    .then(function(response) {
		        if(response.status == 200){
		        	alert("Success");
		        }
		    });
		} else{
			alert("Please submit a phone number.")
		}
	}
});
