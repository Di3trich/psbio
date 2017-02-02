(function () {
    'use strict';

    angular
        .module('psbio')
        .component('crudHorario', crudHorario());

    function crudHorario() {
        var component = {
            templateUrl: 'templates/horario.html',
            bindings: {},
            controller: CrudHorarioController,
            controllerAs: 'vm',
        };
        return component;
    }

    CrudHorarioController.$inject = ['$controller'];

    /* @ngInject */
    function CrudHorarioController($controller) {
        var vm = this;
        vm.crudApiUrl = '/api/horario/';
        $controller('GenericCrudController', {vm: vm});
    }

})();
