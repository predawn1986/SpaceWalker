//注册一个 global component
Vue.component("spacewalker",{
    template: '<h1>自定义 global component</h1>'
})

Vue.component('child', {
    // 声明 props
    props: ['message'],
    // 同样也可以在 vm 实例中像 this.message 这样使用
    template: '<span>{{message}}</span>'
})

Vue.component('todo-item', {
    props: ['todo'],
    template: '<li>{{todo.text}}</li>'
})

Vue.component('example', {
    props:{
        // 基础类型检测 ('null' 意思是任何类型都可以)
        propA: Number,
        // 多种类型
        propB: [String, Number],
        // 必传且是字符串
        propC: {
            type: String,
            required: true
        },
        // 数字，有默认值
        propD: {
            type: Number,
            default: 100
        },
        // 数组/对象的默认值应当由一个工厂函数返回
        propE: {
            type: Object,
            default: function(){
                return {message: "hello"}
            }
        },
        // 自定义验证函数
        propF: {
            validator: function(value){
                return value > 10
            }
        }
    }
})

Vue.component('button-counter', {
    template: '<button v-on:click="incrementHandler">{{counter}}</button>',
    data: function(){
        return {
            counter: 0
        }
    },
    methods: {
        incrementHandler: function(){
            this.counter += 1
            this.$emit('increment')
        }
    },
})

var Child = {
    template: '<h1>自定义 local component</h1>'
}

var vm1 = new Vue({
    el: "#app1",
    data: {
        parentMsg: "The content of father component",
        sites: [
        {text: 'github'},
        {text: 'taobao'},
        {text: 'google'},
        ]
    },
    components: {
        // <google> 将只在父模板可用
        'google': Child
    }
})

var vm2 = new Vue({
    el: "#app2",
    data: {
        parentMsg: null
    }
})

var vm3 = new Vue({
    el: "#counter-event-example",
    data: {
        total: 0
    },
    methods: {
        incrementTotal: function(){
            this.total += 1
        }
    }
})