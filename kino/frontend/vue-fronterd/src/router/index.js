import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import OneMovie from '../views/OneMovie.vue'
import OneCategory from '../views/OneCategory.vue'
import Categories from '../views/Categories.vue'
import Profile from '../views/Profile.vue'
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/search',
    name: 'Search',
    
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
  {
    path: '/profiles/profile/:id',
    name: 'Profile',
    component: Profile,
    props:true
  },

]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
