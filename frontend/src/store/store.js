import Vue from "vue";
import Vuex from "vuex";
import user_store from "./user_store";
import summary_store from "./summary_store";
import home_store from "./home_store";
import tracker_store from "./tracker_store"
import tracker_logs_store from "./tracker_logs_store";
import chart_store from "./chart_store";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    user_store: user_store,
    home_store: home_store,
    summary_store: summary_store,
    tracker_store : tracker_store,
    tracker_logs_store : tracker_logs_store,
    chart_store : chart_store
  },
});
