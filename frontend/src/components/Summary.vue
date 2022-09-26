<template>
  <div>
    <div class="row">
      <div class="col-md-12 fw-bold fs-5 text-center">Dashboard</div>
    </div>
    <hr class="dropdown-divider" />
    <SummaryCards :input_dict="cardData" />
    <SummaryTable :trackers="trackers_list" />
  </div>
</template>

<script>
import SummaryCards from "./SummaryPageComponent/SummaryCards.vue";
import SummaryTable from "./SummaryPageComponent/SummaryTable.vue";
export default {
  name: "SummaryDetails",
  data() {
    return {
      cardData: {},
      trackers_list: [],
    };
  },
  mounted() {
    this.update_active();
    // Data will be fetched from api
    // say response is as follows :===> res for cards, tarckers_data for trackers_list
    const res = {
      tracker_count: 5,
      count_edited: 52,
      last_edited_date: "27 August 2022",
      last_edited_time: "08.05.07",
    };
    this.cardData = res;
    // id, name, type,lastest_value,last_edited
    const tarckers_data = [
      {
        id: 0,
        name: "Runninng",
        type: "Numerical",
        latest_value: "23",
        last_edited: "25 Aug",
      },
      {
        id: 1,
        name: "Walking",
        type: "Numerical",
        latest_value: "23",
        last_edited: "25 Aug",
      },
      {
        id: 2,
        name: "Jogging",
        type: "Numerical",
        latest_value: "23",
        last_edited: "25 Aug",
      },
    ];
    this.trackers_list = tarckers_data;

  },
  components: {
    SummaryCards,
    SummaryTable,
  },
  methods: {
    update_active() {
      this.$store.commit("change_active", 0);
    },
  },
};
</script>
