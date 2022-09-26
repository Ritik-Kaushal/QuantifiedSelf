import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    carousel_width:100,
    active_id : [1,0,0], //index 0-> dashboard, 1->tracker, 2->logs 
  },
  getters: {
    get_carousel_width(state){
      return (state.carousel_width)
    }
  },
  mutations: {
    addClass(){
      const element = document.getElementById("main-div");
      element.classList.remove("custom-container");
      void element.offsetWidth;
      element.classList.add("custom-container");
    },
    remClass(){
      const element = document.getElementById("main-div");
      element.classList.remove("custom-container");
    },
    change_active(state,id){
      state.active_id = [0,0,0];
      state.active_id[id] = 1;
    }
  },
  actions: {
  },
  modules: {
  }
})
