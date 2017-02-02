(function () {
    'use strict';

    angular
        .module('psbio')
        .component('fieldSelect', fieldSelect());

    function fieldSelect() {
        var template = '<md-select ng-model="vm.model" md-on-open="vm.init()" >' +
            '<md-option ng-value="option.id" ng-repeat="option in vm.options">{{ option.name }}</md-option>' +
            '</md-select>';
        var component = {
            template: template,
            bindings: {
                apiUrl: '<',
                field: '@',
                model: '='
            },
            controller: FieldSelectController,
            controllerAs: 'vm',
        };
        return component;
    }

    FieldSelectController.$inject = ['$http'];

    /* @ngInject */
    function FieldSelectController($http) {
        var vm = this;
        vm.$onInit = init;
        vm.options = [];
        vm.init = init;

        function init() {
            $http.get(vm.apiUrl + '?size=1000')
                .then(completed, failed);
        }

        function completed(result) {
            vm.options = [];
            for (var i in result.data.results) {
                vm.options.push({
                    id: result.data.results[i].id,
                    name: result.data.results[i][vm.field]
                });
            }
        }

        function failed() {

        }
    }

})();
