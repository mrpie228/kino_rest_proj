import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import OneMovie from '../views/OneMovie.vue'
import OneCategory from '../views/OneCategory.vue'
import Categories from '../views/Categories.vue'
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
  },
  {
    path:'/&category=:name',
    name:'OneCategory',
    component: OneCategory,
    props: true,
  },
  {
    path: '/categories',
    name: 'Categories',
    component: Categories,
    props:true
  },

]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
