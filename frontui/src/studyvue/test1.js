var vm = new Vue({
    el: '#app',
    data: {
        checked: false,
        checkedNames: [],
        checkedArr: ["Runoob", "Taobao", "Google"]
    },
    methods: {
        changeAllChecked: function() {
            if (this.checked) {
                this.checkedNames = this.checkedArr
            } else {
                this.checkedNames = []
            }
        }
    },
    watch: {
        "checkedNames": function() {
            if (this.checkedNames.length == this.checkedArr.length) {
                this.checked = true
            } else {
                this.checked = false
            }
        }
    }
})