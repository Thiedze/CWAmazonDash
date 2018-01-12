var cwAmazonDashService = angular.module('cwAmazonDashService', [ 'ngResource' ]);

cwAmazonDashService.factory('AmazonService', [ '$resource', function($resource) {
	return $resource('../rest/v1/:action', {}, {
		groups : {
				method : 'GET',
				params : {
					action : 'groups'
				},
				isArray : true
		}
	});
} ]);