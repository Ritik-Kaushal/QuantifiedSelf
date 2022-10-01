<template>
  <div v-if="$store.getters.get_ready_to_display_summary" :key="$store.getters.get_card_data.tracker_count">
    <div v-if="$store.getters.get_are_trackers_available">
      <div class="row">
        <div class="col-md-12 fw-bold fs-5 text-center">Dashboard</div>
      </div>
      <hr class="dropdown-divider" />
      <SummaryCards />
      <SummaryTable :trackers="$store.getters.get_tracker_list" />
      <hr class="dropdown-divider" />
      <Trendlines/>

    </div>
    <div v-else>
      <NoTrackerDashboard />
    </div>
  </div>
</template>

<script>
import TrendLines from "../components/trendlines.vue";
import SummaryCards from "../components/SummaryPageComponent/SummaryCards.vue";
import SummaryTable from "../components/SummaryPageComponent/SummaryTable.vue";
import NoTrackerDashboard from "@/components/no_trackers_dashboard.vue";
import Trendlines from "../components/trendlines.vue";

export default {
  name: "SummaryDetails",
  data() {
    return {
      cardData: {},
    };
  },
  async mounted() {
    if(this.$store.getters.get_login_status){
      this.$store.commit('set_ready_to_display_summary',false);
      this.$store.commit("change_active", 0);
      if(this.$store.getters.get_need_to_reload_summary){
        
        await this.$store.dispatch('getDataSummary');
      }
      this.$store.commit('set_ready_to_display_summary',true); 
    }
    else{
      this.$router.push({name : 'Main'});
    }
    
  },
  components: {
    SummaryCards,
    SummaryTable,
    NoTrackerDashboard,
    TrendLines,
    Trendlines
},
};
</script>
