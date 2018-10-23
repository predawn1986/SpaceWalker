var vm = new Vue({
    el: "#app",
    data: {
        counter: 0,
        name: 'vue.js'
    },
    // 在 methods 对象中定义方法
    methods: {
        greet: function(event) {
            // this 在方法里指当前 vue 实例
            alert('Hello, ' + this.name + '!')
            // event 是原生 DOM 事件
            if (event) {
                alert(event.target.tagName)
            }
        }
    }
})