import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Planner from '@/components/Planner'
import NewPlanner from '@/components/NewPlanner'
import Login from '@/components/Login'
import store from '@/store'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    }, {
      path: '/planners/:id',
      name: 'Planner',
      component: Planner
    },{
      path: '/planners',
      name: 'NewPlanner',
      component: NewPlanner,
      beforeEnter (to, from, next) {
        if (!store.getters.isAuthenticated) {
          next('/login')
        } else {
          next()
        }
      }
    }, {
      path: '/login',
      name: 'Login',
      component: Login
    }
  ]
})
