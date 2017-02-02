(function () {
    'use strict';

    angular
        .module('psbio')
        .component('crudRegistro', crudRegistro());

    function crudRegistro() {
        var component = {
            templateUrl: 'templates/registro.html',
            bindings: {},
            controller: CrudRegistroController,
            controllerAs: 'vm',
        };
        return component;
    }

    CrudRegistroController.$inject = ['$controller'];

    /* @ngInject */
    function CrudRegistroController($controller) {
        var vm = this;
        vm.crudApiUrl = '/api/registro/';
        $controller('GenericCrudController', {vm: vm});
    }

})();
