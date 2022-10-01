const home_store = {
  state: () => ({
    carousel_width: 100,
  }),
  getters: {
    get_carousel_width(state) {
      return state.carousel_width;
    },
  },
  mutations: {},
  actions: {
    addClass() {
      const element = document.getElementById("main-div");
      element.classList.remove("custom-container");
      void element.offsetWidth;
      element.classList.add("custom-container");
    },
    remClass() {
      const element = document.getElementById("main-div");
      element.classList.remove("custom-container");
    },
  },
};

export default home_store;
