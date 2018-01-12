cwAmazonDashControllers.controller('groupController', function($rootScope, $scope, AmazonService) {

	AmazonService.groups(function(data) {
		$scope.groups = data;
	}, function(error) {
		this.errorMessage = error;
	});

	$scope.getGroupCssClass = function(index) {
		return "group-" + (index % 3);
	};

	$scope.getNumber = function(number) {
		return new Array(parseInt(number));
	};

	$scope.hasDashButton = function(group, row, column) {
		for (var index = 0; index < group.dash_buttons.length; index++) {
			if (parseInt(group.dash_buttons[index].row) === row && parseInt(group.dash_buttons[index].column) === column) {
				return true;
			}
		}

		return false;
	}

	$scope.getImageUrl = function(group, row, column) {
		for (var index = 0; index < group.dash_buttons.length; index++) {
			if (parseInt(group.dash_buttons[index].row) === row && parseInt(group.dash_buttons[index].column) === column) {
				return group.dash_buttons[index].image_url.replace(/'/g, "");
			}
		}

		return "images/amazon_dash_white.png";
	};

});