import FetchFunction from "../utils";
import router from "@/router";

const user_store = {
  state: () => ({
    loggedIn: localStorage.getItem("jwt_token") ? true : false,

  }),

  getters: {
    jwt_token(state) {
      if (state.loggedIn === true) {
        console.log("Getting JWT Token : ", localStorage.getItem("jwt_token"));
        return localStorage.getItem("jwt_token");
      } else {
        return null;
      }
    },
    get_login_status(state) {
      return state.loggedIn;
    },


  },
  mutations: {
    login(state) {
      state.loggedIn = true;
    },
    logout(state) {
      state.loggedIn = false;
    },


  },
  actions: {
    logoutUser({ commit }) {
      // localStorage.removeItem("jwt_token");
      commit("logout");
      router.push({ name: "Main" });
    },

  },
};

export default user_store;
