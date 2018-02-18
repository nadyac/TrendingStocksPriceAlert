//Define the TrendingStocks module
var app = angular.module('myApp',[]);

//Define the controller on the trendingStocks module/ The controller will be responsible
//for handling all the logic for a portion of the app that it controls
app.controller('stocksListController', function stocksListController($scope,$http){
	$http.get("/getStocks")
	    .then(function(response) {
	        $scope.stocks = response.data;
	    });

	$scope.setAlert = function(targetSymbol){
		config = {
			data:targetSymbol,
			params:{
				alertSymbol:targetSymbol,
				toNumber:"12019262482"
			}
		}
		$http.get("/setAlert",config)
	    .then(function(response) {
	        console.log(response);
	    });
	}
});