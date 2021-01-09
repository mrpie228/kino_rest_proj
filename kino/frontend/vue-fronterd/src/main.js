import { createApp } from 'vue';

import App from './App';
import Vue from 'vue'

import router from './router';

import axios from 'axios';
import VueAxios from 'vue-axios';

createApp(App).use(router).mount('#app')

Vue.use(axios,VueAxios)

new Vue({
    el:'#app',
    router,
    components:{App},
    template: '<App/>',
    axios
});