(function () {
    'use strict';

    angular
        .module('psbio')
        .component('crudPeriodo', crudPeriodo());

    function crudPeriodo() {
        var component = {
            templateUrl: 'templates/periodo.html',
            bindings: {},
            controller: CrudPeriodoController,
            controllerAs: 'vm',
        };
        return component;
    }

    CrudPeriodoController.$inject = ['$controller'];

    /* @ngInject */
    function CrudPeriodoController($controller) {
        var vm = this;
        vm.crudApiUrl = '/api/periodo';
        $controller('GenericCrudController', {vm: vm});
    }

})();

