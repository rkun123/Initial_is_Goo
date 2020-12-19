import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/room/join',
    name: 'room/join',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/User.vue')
  },
  {
    path:'/room/create',
    name:'room/create',
    component: () => import('../views/Host.vue')
  },
  {
    path:'/room/:session_id/host',
    name:'room/id/host',
    component: () => import('../views/RoomHost.vue')
  },
  {
    path:'/room/:session_id/guest',
    name:'room/id/guest',
    component: () => import('../views/RoomUser.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
