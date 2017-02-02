(function () {
    angular
        .module('psbio')
        .config(function ($stateProvider, $httpProvider) {
            var persona = {
                name: 'personal',
                url: '/personal',
                template: '<crud-persona></crud-persona>'
            };
            var dospositivo = {
                name: 'dispositivo',
                url: '/dispositivo',
                template: '<crud-dispositivo></crud-dispositivo>'
            };
            var horario = {
                name: 'horario',
                url: '/horario',
                template: '<crud-horario></crud-horario>'
            };
            var registro = {
                name: 'registro',
                url: '/registro',
                template: '<crud-registro></crud-registro>'
            };
            $stateProvider.state(persona);
            $stateProvider.state(dospositivo);
            $stateProvider.state(horario);
            $stateProvider.state(registro);

            $httpProvider.defaults.xsrfCookieName = 'csrftoken';
            $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        });
})();