import FetchFunction from '@/utils';

const tracker_store = {
  state: () => ({
    duration_list: [
      { id: 0, duration: "Last 24 hours" },
      { id: 1, duration: "Last 7 days" },
      { id: 2, duration: "Last 30 days" },
      { id: 3, duration: "All" },
    ],
    tracker_type_list : [
      { id: 0, type: "Numeric" },
      { id: 1, type: "Multiple Choice" },
      { id: 2, type: "Time Duration" },
      { id: 3, type: "Boolean" },
    ],
    tracker_list: [],
    selected_tracker: {},
    selected_tracker_id: -1,
    selected_duration_id: 0,
    need_to_reload_trackers : true,
    ready:false,
    update_component : 0
  }),
  getters: {
    get_tracker_list(state) {
      return state.tracker_list;
    },
    get_duration_list(state) {
      return state.duration_list;
    },
    get_selected_tracker_id(state) {
      return state.selected_tracker_id;
    },
    get_selected_duration_id(state) {
      return state.selected_duration_id;
    },
    get_need_to_reload_trackers(state){
      return state.need_to_reload_trackers;
    },
    get_selected_tracker(state){
      return state.selected_tracker;
    },
    ready_to_display_tracker_cards(state){
      return state.ready;
    },
    get_tracker_type_list(state){
      return state.tracker_type_list;
    },
    get_are_trackers_available(state){
      if(state.tracker_list.length==0){
        return false;
      }
      return true;
    },
    get_update_component(state){
      return state.update_component;
    }
  },
  mutations: {
    change_selected_tracker_id(state, id) {
      state.selected_tracker_id = id;
    },
    change_selected_duration_id(state, id) {
      state.selected_duration_id = id;
      state.ready = true;
    },
    update_tracker_list(state, tracker_list) {
      state.tracker_list = tracker_list;
    },
    set_need_to_reload_trackers(state,what){
      state.need_to_reload_trackers = what;
    },
    set_selected_tracker(state,selected_tracker){
      state.selected_tracker = selected_tracker;
    },
    set_ready_to_display_tracker_cards(state,what=true){
      state.ready = what;
    },
    set_update_component(state){
      state.update_component++;
    }
  },
  actions: {
    async getTrackers({commit,dispatch}) { 
      // commit('set_ready_to_display_tracker_cards',false);
      let url = "http://localhost:5000/api/trackers/get";
      let init_obj = {
        method: "GET",
      };
      let res = await FetchFunction({
        url: url,
        init_obj: init_obj,
        authRequired: true,
      })
        .then(async (data) => {
          let tracker_list = [];
          
          for (let each of data) {
            if (this.getters.get_selected_tracker_id === -1){
              commit("change_selected_tracker_id",each.id);
              dispatch("getSelectedTrackerDetails");
            }
            let temp = {
                id: each.id,
                name: each.tracker_name,
                type: each.tracker_type,
                latest_value: (each.latest_value) || ('-'),
                last_edited:(each.last_edited) || ('-'),
                reqd_values : each.reqd_values
              }
            tracker_list.push(temp);
          }
          commit("update_tracker_list", tracker_list);
          commit("set_need_to_reload_trackers",false);
        })
        .catch((e) => {
          const err = JSON.parse(e.message);
          console.log(err.error_code)
          if(err.error_code == "TIM" || err.error_code == "IVT"){
            dispatch('logoutUser',{root:true});
          }

        }).catch();
    },
    async getSelectedTrackerDetails({commit,dispatch}) {
      let url = "http://localhost:5000/api/trackers/get?tracker_id="+this.getters.get_selected_tracker_id;
      let res = await FetchFunction({
        url:url,
        authRequired:true
      }).then((data)=>{
        commit('set_selected_tracker',data);
        dispatch('getLogs',{root:true});
      }).catch((e)=>{
        const err = JSON.parse(e.message);
          if(err.error_code == 'TIM' || err.error_code == 'IVT'){
            dispatch('logoutUser',{root:true});
          }
      }).catch();
    }
  },
};

export default tracker_store;
