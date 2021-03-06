var app = angular.module("app", ['ngRoute']);

// this is changing the {{ }} to [[ ]] because django gets confused
app.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
})

app.config(function($routeProvider) {
    $routeProvider
        .when('/', {
            templateUrl: static_url + 'home/js/partials/partial1.html',
            controller: 'RouteController1'
        })

        .when('/howitworks', {
            templateUrl: static_url + 'home/js/partials/partial2.html',
            controller: 'RouteController2'
        })

        .when('/surprise', {
            templateUrl: static_url + 'home/js/partials/partial3.html',
            controller: 'RouteController3'
        })

        .when('/faqs', {
            templateUrl: static_url + 'home/js/partials/partial4.html',
            controller: 'RouteController4'
        })

        .when('/route5', {
            templateUrl: static_url + 'home/js/partials/partial5.html',
            controller: 'RouteController5'
        })

        .otherwise({
            redirectTo: '/'
        });
});