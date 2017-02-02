(function () {
    'use strict';

    angular
        .module('psbio')
        .component('crudDispositivo', crudDispositivo());

    function crudDispositivo() {
        var component = {
            templateUrl: 'templates/dispositivo.html',
            bindings: {},
            controller: CrudDispositivoController,
            controllerAs: 'vm',
        };
        return component;
    }

    CrudDispositivoController.$inject = ['$controller'];

    /* @ngInject */
    function CrudDispositivoController($controller) {
        var vm = this;
        vm.crudApiUrl = '/api/dispositivo/';
        $controller('GenericCrudController', {vm: vm});
    }

})();
