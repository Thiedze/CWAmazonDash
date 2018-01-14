cwAmazonDashControllers.controller('cwAmazonDashController', function($scope, $timeout, AmazonService) {

	$scope.showSnackbar = false;

	AmazonService.groups(function(data) {
		$scope.groups = data;
	}, function(error) {
		this.errorMessage = error;
	});

	$scope.getGroupCssClass = function(index) {
		return "group-" + (index % 3);
	};

	$scope.getButtonCssClass = function(index) {
		return "add_button-" + ((index) % 3);
	}

	$scope.getNumber = function(number) {
		return new Array(parseInt(number));
	};

	$scope.getDashButton = function(group, row, column) {
		for (var index = 0; index < group.dash_buttons.length; index++) {
			if (parseInt(group.dash_buttons[index].row) === row && parseInt(group.dash_buttons[index].column) === column) {
				return group.dash_buttons[index];
			}
		}

		return null;
	};

	$scope.hasDashButton = function(group, row, column) {
		var dashButton = $scope.getDashButton(group, row, column);

		if (dashButton != null) {
			return true;
		} else {
			return false;
		}
	};

	$scope.getDashButtonTitle = function(group, row, column) {
		var dashButton = $scope.getDashButton(group, row, column);

		if (dashButton != null) {
			return dashButton.title;
		} else {
			return "No dash button configured";
		}
	};

	$scope.getDashButtonPrice = function(group, row, column) {
		var dashButton = $scope.getDashButton(group, row, column);

		if (dashButton != null) {
			return dashButton.price;
		} else {
			return null;
		}
	};

	$scope.getImageUrl = function(group, row, column) {
		var dashButton = $scope.getDashButton(group, row, column);

		if (dashButton != null) {
			return dashButton.image_url;
		} else {
			return "images/amazon_dash_white.png";
		}
	};

	$scope.addToCart = function(group, row, column) {
		var dashButton = $scope.getDashButton(group, row, column);

		if (dashButton != null) {

		} else {
			$scope.snackbarMessage = "No DashButton configured.";
			$scope.showSnackbar = true;

			$scope.startSnackbarTimeout();
		}
	};

	$scope.startSnackbarTimeout = function() {
		$timeout(function() {
			if ($scope.showSnackbar == true) {
				$scope.showSnackbar = false;
				$scope.snackbarMessage = null;
			}
		}, 3000);
	};

	$scope.getColumnClass = function(columns) {
		return "col-lg-" + (12 / parseInt(columns));
	};

	$scope.getGroupClass = function(columns) {
		return "col-lg-" + (parseInt(columns) * 2);
	};

	$('.popover-dismiss').popover({
		trigger : 'focus'
	})

});