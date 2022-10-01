import FetchFunction from "@/utils";
const summary_store = {
  state: () => ({
    active_id: [1, 0, 0,0,0], //index 0-> dashboard, 1->tracker, 2->logs
    ready_to_display_summary : false,
    need_to_reload_summary : true,
    card_data : {}
  }),
  getters: {
    get_active_id_status(state,id){
        return state.active_id[id];
    },
    get_ready_to_display_summary(state){
      return state.ready_to_display_summary;
    },
    get_need_to_reload_summary(state){
      console.log("Here")
      return state.need_to_reload_summary;
    },
    get_card_data(state){
      return state.card_data;
    },
  },
  mutations: {
    change_active(state, id) {
      state.active_id = [0, 0, 0,0,0];
      state.active_id[id] = 1;
    },
    set_ready_to_display_summary(state,what=true){
      state.ready_to_display_summary = what;
    },
    set_need_to_reload_summary(state,what){
      state.need_to_reload_summary = what;
    },
    set_card_data(state,data){
      state.card_data = data;
    },
  },
  actions: {
    async getDataSummary({state,commit,dispatch}){
      console.log("In getDataSummary");
      let url = "http://localhost:5000/api/dataSummary/get";
      let res = await FetchFunction({url:url,authRequired:true}).then(async (data)=>{
        const res = {
          tracker_count: data.no_of_trackers,
          count_edited: data.no_of_times_edited,
          last_edited_date: (data.last_edited_date) || '-',
          last_edited_time: (data.last_edited_time)  || '-',
        };
        console.log(res);
        commit('set_card_data',res);
        commit('set_need_to_reload_summary',false);
        dispatch('getTrackers',{root:true});
        console.log("Card data = "+state.card_data);
      }).catch((e)=>{
        console.log(e)
        dispatch('logoutUser',{root:true});
      })
      
    }
  },
};

export default summary_store;
