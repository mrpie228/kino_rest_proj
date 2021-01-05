import Vue from 'vue'
import Vuex from 'vuex'

Vue.useContext(Vuex)

const stock = new Vuex.Stock({
    state:{
        backendUrl:"http://127.0.0.1:8000/api/v2/"
    },
    mutations:{},
    actions:{},
    modules:{},
    getters:{
        getServerUrl: state => {
            return state.backendUrl
        }
    }
    
})
//export default stock