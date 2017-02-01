(function () {
    'use strict';

    angular
        .module('psbio')
        .component('updateInsertModal', updateInsertModal());

    function updateInsertModal() {
        var template = '<ng-transclude ng-click="vm.launchModal($event)"></ng-transclude>';
        var component = {
            template: template,
            bindings: {
                apiUrl: '<?',
                rowData: '<?',
                template: '@?',
                onSave: '&?'
            },
            controller: UpdateInsertModalController,
            controllerAs: 'vm',
            transclude: true
        };
        return component;
    }

    UpdateInsertModalController.$inject = ['$mdDialog'];
    /* @ngInject */
    function UpdateInsertModalController($mdDialog) {
        var vm = this;
        vm.launchModal = launchModal;

        function launchModal(ev) {
            vm.edit = !!vm.rowData;
            var template = '<md-dialog aria-label="Dialogo de Registro" flex>' +
                '<md-toolbar>' +
                '<div class="md-toolbar-tools">' +
                '<h2>Registro</h2>' +
                '<span flex></span>' +
                '<md-button class="md-icon-button" ng-click="vm.cancel($event)">' +
                '<md-icon>close</md-icon>' +
                '</md-button>' +
                '</div>' +
                '</md-toolbar>' +
                '<md-content ng-include="vm.template" layout="column" flex-fill></md-content>' +
                '<md-dialog-actions flex>' +
                '<md-button ng-click="vm.cancel($event)" class="md-primary md-raised">' +
                '<md-icon>close</md-icon> Cancelar' +
                '</md-button>' +
                '<md-button ng-click="vm.perform($event)" class="md-primary md-raised">' +
                '<md-icon>save</md-icon> {{ vm.performText }}' +
                '</md-button>' +
                '</md-dialog-actions>' +
                '</md-dialog>';

            $mdDialog.show({
                controller: ModalController,
                controllerAs: 'vm',
                template: template,
                targetEvent: ev,
                clickOutsideToClose: true,
                locals: {
                    rowData: {
                        template: vm.template,
                        field: vm.rowData,
                        edit: vm.edit,
                        apiUrl: vm.apiUrl
                    }
                }
            }).then(completed, failed);

            function completed(data) {
                if (data == 'saved' && vm.onSave) {
                    vm.onSave();
                }
            }

            function failed() {
            }
        }
    }

    ModalController.$inject = ['$http', '$mdDialog', 'rowData'];
    /* @ngInject */
    function ModalController($http, $mdDialog, rowData) {
        var vm = this;
        vm.performText = rowData.edit ? 'Editar' : 'Registrar';
        vm.perform = perform;
        vm.cancel = cancel;
        vm.field = rowData.field;
        vm.template = rowData.template;

        function perform(ev) {
            var request = null;
            if (rowData.edit) {
                request = $http.patch(rowData.apiUrl, vm.field);
            } else {
                request = $http.post(rowData.apiUrl, vm.field);
            }
            request.then(completed, failed);
        }

        function completed() {
            $mdDialog.hide('saved');
        }

        function failed() {

        }

        function cancel(ev) {
            $mdDialog.cancel();
        }
    }

})();
