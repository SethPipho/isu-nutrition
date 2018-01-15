import Vue from 'vue'
import Router from 'vue-router'

import DiningCenters from './../components/DiningCenters'
import Menu from './../components/Menu'

Vue.use(Router)

export default new Router({
  routes:  [
    { path: '/', component: DiningCenters},
    { path: '/:diningCenterName', component: Menu},
  ]
})
