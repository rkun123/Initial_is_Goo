import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    username: "",
    userid: "",
    hand: "0",
    hostname:"",
    hostid:"",
    roomname: "",
    roomid: "",
    is_win: true,
    users: [],

  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
