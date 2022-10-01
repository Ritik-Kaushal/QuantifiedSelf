import getLastTimestamp from "../utils/getLastTimeStamp";
import FetchFunction from "@/utils";

const tracker_logs_store = {
  state: () => ({
    selected_tracker_all_logs: [],
    reqd_duration_logs: [],
    need_to_reload_logs: true,
    ready_to_display_logs: false,
  }),
  getters: {
    get_selected_tracker_all_logs(state) {
      return state.selected_tracker_all_logs;
    },
    get_reqd_duration_logs(state) {
      return state.reqd_duration_logs;
    },
    need_to_reload_logs(state) {
      return state.need_to_reload_logs;
    },
    get_ready_to_display_logs(state) {
      return state.ready_to_display_logs;
    },
  },
  mutations: {
    set_selected_tracker_all_logs(state, logs) {
      state.selected_tracker_all_logs = logs;
    },
    set_reqd_duration_logs(state, logs) {
      state.reqd_duration_logs = logs;
    },
    set_need_to_reload_logs(state, what) {
      state.need_to_reload_logs = what;
    },
    set_ready_to_display_logs(state, what) {
      state.ready_to_display_logs = what;
    },
  },
  actions: {
    async getLogs({ commit, dispatch, getters, rootGetters }) {
      const tracker_id = rootGetters.get_selected_tracker_id;
      if (tracker_id == -1) {
        await dispatch("getTrackers", { root: true });
      } else {
        let url =
          "http://localhost:5000/api/trackerLogs/get?tracker_id=" + tracker_id;
        console.log("Url :" + url);
        let init_obj = {
          method: "GET",
        };
        let res = await FetchFunction({
          url: url,
          init_obj: init_obj,
          authRequired: true,
        })
          .then(async (data) => {
            let logs = [];

            for (let each of data) {
              let temp = {
                id: each.id,
                time_stamp: each.time_stamp,
                value: each.value,
                note: each.note,
              };
              logs.push(temp);
            }
            commit("set_selected_tracker_all_logs", logs);
            await dispatch("update_logs_of_duration");
            commit("set_need_to_reload_logs", false);
            console.log(1005);
          })
          .catch((e) => {
            const err = JSON.parse(e);
            if (e.error_code == "TIM" || e.error_code == "IVT") {
             dispatch('logoutUser',{root:true});
            }
          }).catch();
      }
    },
    update_logs_of_duration({ getters, commit, rootGetters }) {
      console.log(1003);
      let duration_id = rootGetters.get_selected_duration_id;
      let logs = getters.get_selected_tracker_all_logs;
      if (duration_id == 0) {
        var last_time_stamp = getLastTimestamp(1);
        let selected_logs = logs.filter(
          (log_obj) => log_obj.time_stamp >= last_time_stamp
        );

        commit("set_reqd_duration_logs", selected_logs);
      } else if (duration_id == 1) {
        var last_time_stamp = getLastTimestamp(7);
        let selected_logs = logs.filter(
          (log_obj) => log_obj.time_stamp >= last_time_stamp
        );
        commit("set_reqd_duration_logs", selected_logs);
      } else if (duration_id == 2) {
        var last_time_stamp = getLastTimestamp(30);
        let selected_logs = logs.filter(
          (log_obj) => log_obj.time_stamp >= last_time_stamp
        );
        commit("set_reqd_duration_logs", selected_logs);
      } else {
        commit("set_reqd_duration_logs", logs);
      }
      console.log(1004);
    },
  },
};

export default tracker_logs_store;
