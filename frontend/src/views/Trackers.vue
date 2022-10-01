<template>
  <div v-if="$store.getters.ready_to_display_tracker_cards">
    <div v-if="$store.getters.get_are_trackers_available">
      <DropDown :key="this.$store.getters.get_selected_duration_id"/>
      <Tracker_Details />
      <TrackerTrendline :key="this.$store.getters.get_selected_duration_id"/>
    </div>
    <div v-else>
      <NoTracker/>
    </div>
  </div>
</template>

<script>
import DropDown from "../components/dropdown.vue";
import Tracker_Details from "../components/tracker_details.vue";
import NoTracker from "../components/no_trackers_page.vue";
import TrackerTrendline from "../components/tracker_trendline.vue"
export default {
  name: "TrackersDetails",
  components: {
    DropDown,
    Tracker_Details,
    NoTracker,
    TrackerTrendline
  },
  async mounted() {
    this.$store.commit("change_active", 1);
    if(this.$store.getters.get_need_to_reload_trackers){
      await this.$store.dispatch("getTrackers");
    }
    this.$store.commit('set_ready_to_display_tracker_cards');
  }
};
</script>
