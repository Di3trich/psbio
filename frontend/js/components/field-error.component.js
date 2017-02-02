(function () {
    'use strict';

    angular
        .module('psbio')
        .component('fieldError', fieldError());

    function fieldError() {
        var template = '<div ng-repeat="error in vm.errorData" class="error">' +
            '{{ error }}' +
            '</div>';
        var component = {
            template: template,
            bindings: {
                errorData: '<'
            },
            controller: FieldErrorController,
            controllerAs: 'vm',
        };
        return component;
    }

    FieldErrorController.$inject = [];

    /* @ngInject */
    function FieldErrorController() {
        var vm = this;
    }

})();


