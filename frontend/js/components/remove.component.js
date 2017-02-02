(function () {
    'use strict';

    angular
        .module('psbio')
        .component('remove', remove());

    function remove() {
        var template = '<md-button class="md-icon-button md-warn" ng-click="vm.remove($event)">' +
            '<md-icon>delete</md-icon>' +
            '</md-button>';
        var component = {
            template: template,
            bindings: {
                apiUrl: '<',
                onRemove: '&'
            },
            controller: RemoveController,
            controllerAs: 'vm',
        };
        return component;
    }

    RemoveController.$inject = ['$http', '$mdDialog'];

    /* @ngInject */
    function RemoveController($http, $mdDialog) {
        var vm = this;
        vm.remove = remove;

        function remove(ev) {
            var confirm = $mdDialog.confirm()
                .title('Eliminar')
                .textContent('¿Desea Eliminar el Elemento?')
                .ariaLabel('eliminar')
                .targetEvent(ev)
                .ok('Eliminar')
                .cancel('Cancelar');

            $mdDialog.show(confirm)
                .then(function () {
                    $http.delete(vm.apiUrl)
                        .then(completed, failed);
                }, function () {
                });
        }

        function completed() {
            vm.onRemove();
        }

        function failed() {
            vm.failed();
        }
    }

})();
