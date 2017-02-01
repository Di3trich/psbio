(function () {
    angular
        .module('psbio')
        .config(function ($stateProvider, $httpProvider) {
            var persona = {
                name: 'personal',
                url: '/personal',
                template: '<crud-persona></crud-persona>'
            };
            var encuesta = {
                name: 'encuesta',
                url: '/encuesta',
                template: '<crud-encuesta></crud-encuesta>'
            };
            var periodo = {
                name: 'periodo',
                url: '/periodo',
                template: '<crud-periodo></crud-periodo>'
            };
            $stateProvider.state(persona);
            $stateProvider.state(encuesta);
            $stateProvider.state(periodo);

            $httpProvider.defaults.xsrfCookieName = 'csrftoken';
            $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        });
})();