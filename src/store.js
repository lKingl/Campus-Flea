import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    uid: 0,
    is_login: false
  },
  mutations: {
    setUid (state, id) {
      state.uid = id
    },
    changeLoginStatus (state) {
      state.is_login = !state.is_login
    }
  },
  actions: {

  }
})
