import dynamicsort from "@/utils/sorting";
import getLastTimestamp from "@/utils/getLastTimeStamp";
// import Chart from 'chart.js'
import FetchFunction from "@/utils";

const chart_store = {
  state: () => ({
    chart_data: {}, //Chart data of a tracker
    need_to_reload_chart: true,
    chart_log_list : []
  }),
  getters: {
    get_chart_data(state) {
      return state.chart_data;
    },
    get_need_to_reload_chart_data(state) {
      return state.need_to_reload_chart_data;
    },
  },
  mutations: {
    set_chart_data(state, data) {
      state.chart_data = data;
    },
    set_need_to_reload_chart(state, what) {
      state.need_to_reload_chart = what;
    },
  },
  actions: {
    async get_chart_data({commit},obj) {
      let last_time_stamp = "";
      if (obj.duration_id == 0) {
        last_time_stamp = getLastTimestamp(1);
      } else if (obj.duration_id == 1) {
        last_time_stamp = getLastTimestamp(7);
      } else if (obj.duration_id == 2) {
        last_time_stamp = getLastTimestamp(30);
      } 
      console.log(12344,obj);
      let url =
        "http://localhost:5000/api/trackerLogs/get?tracker_id=" + obj.tracker_id;
      let init_obj = {
        method: "GET",
      };
      let res = await FetchFunction({
        url: url,
        init_obj: init_obj,
        authRequired: true,
      })
        .then(async (data) => {
          data.sort(dynamicsort("time_stamp"));
          let labels = [];
          let values = [];
          
          let value_list = []
          let title = obj.title
          if(obj.tracker_type == "Multiple Choice" || obj.tracker_type == "Boolean"){
            value_list = obj.tracker_values.split(',');
            for (let i=0;i<value_list.length;i++){
                value_list[i]=value_list[i].trim();
                title+=" "+i+":"+value_list[i]+", ";
                console.log(title)
            }
          }
          console.log(title);
          for (let each of data) {
            if (each.time_stamp > last_time_stamp) {
              labels.push(each.time_stamp);
              if(obj.tracker_type == "Multiple Choice" || obj.tracker_type == "Boolean"){
                    for (let i=0;i<value_list.length;i++){
                        if(value_list[i]==each.value.trim()){
                            values.push(i);
                        }
                    }
              }else{
                  values.push(each.value);
              }
            }
          }
          
          const chart_data = {
            labels: labels,
            datasets: [
              {
                label: title,
                backgroundColor: "rgb(255, 99, 132)",
                borderColor: "rgb(255, 99, 132)",
                data: values,
              },
            ],
          };
          commit("set_chart_data", chart_data);
        })
        .catch((e) => {
          const err = JSON.parse(e);
          if (e.error_code == "TIM" || e.error_code == "IVT") {
            dispatch("logoutUser", { root: true });
          }
        })
        .catch();
    },
    generate_chart({getters},tracker_id) {
      console.log("To string",typeof(tracker_id.toString()))
      const config = {
        type: "line",
        data: getters.get_chart_data,
        options: {},
      };

      const chart_id = "chart_id_"+tracker_id.toString();
      console.log(document.getElementById(chart_id))
      const myChart = new Chart(document.getElementById(chart_id), config);
    },
    
  },
};

export default chart_store;
