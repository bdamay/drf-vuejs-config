import Vue from 'vue'

import App from './App.vue'

new Vue({
  el: '#app',
  render: h => h(App)   //renders the App on Vue div (App est un module Vue
})
Vue.config.devtools = true;
