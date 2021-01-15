import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export default new Vuex.Store({
  state: {
    authUser: {},
    isAuthenticated: false,
    jwt: localStorage.getItem('token'),
    endpoints: {

      obtainJWT: 'https://127.0.0.1:8000/api/v2/token/',
      refreshJWT: 'https://127.0.0.1:8000/api/v2/token_refresh/',
      baseUrl: 'https://127.0.0.1:8000/api/v2/'
    }
  },

  mutations: {
    setAuthUser(state, {
      authUser,
      isAuthenticated
    }) {
      Vue.set(state, 'authUser', authUser)
      Vue.set(state, 'isAuthenticated', isAuthenticated)
    },
    updateToken(state, newToken) {

      localStorage.setItem('token', newToken);
      state.jwt = newToken;
    },
    removeToken(state) {

      localStorage.removeItem('token');
      state.jwt = null;
    }
  }
})