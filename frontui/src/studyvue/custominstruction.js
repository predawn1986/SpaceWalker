// 注册一个全局自定义指令 v-focus
Vue.directive('focus', {
    // 当帮顶元素插入到 DOM 中
    inserted: function(el){
        // 聚焦元素
        el.focus()
    }
})

Vue.directive('space',{
    bind: function(el, binding, vnode){
        var s = JSON.stringify
        el.innerHTML = 
            'name:' + s(binding.name) + '<br>' +
            'value:' + s(binding.value) + '<br>' +
            'expression:' + s(binding.expression) + '<br>' +
            'argument:' + s(binding.argument) + '<br>' +
            'modifiers:' + s(binding.modifiers) + '<br>' +
            'vnode keys:' + Object.keys(vnode).join(', ')
    }
})

Vue.directive('google', function(el, binding){
    // 简写方式设置文本及背景颜色
    el.innerHTML = binding.value.text
    el.style.backgroundColor = binding.value.color
})

var vm = new Vue({
    el: "#app",
    data: {
        message: "vue.js 学习"
    }
})