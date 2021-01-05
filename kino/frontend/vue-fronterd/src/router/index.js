import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import OneMovie from '../views/OneMovie.vue'
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/search',
    name: 'Search',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Search.vue'),
  },
  {
    path:'/:url',
    name:'OneMovie',
    component:OneMovie,
    props: true,
  }

]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
