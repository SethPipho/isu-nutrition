import Vue from 'vue'
import axios from 'axios'

import App from './App.vue'
import router from './router'

import DiningCenters from './components/DiningCenters.vue'

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
